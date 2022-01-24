import logging
from http import HTTPStatus

import requests
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from furl import furl
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

logger = logging.getLogger(__name__)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields didn\'t match.'})

        return attrs

    def validate_email(self, value):
        if not settings.EMAIL_VERIFICATION:
            return value

        response = requests.get(furl(settings.EMAIL_HUNTER_URL).add({
            'api_key': settings.EMAIL_HUNTER_KEY,
            'email': value
        }).url)

        logger.info(f'Email hunter response status code: {response.status_code}')

        if response.status_code == HTTPStatus.OK and response.json()['data']['result'] == 'undeliverable':
            raise serializers.ValidationError('Undeliverable email')

        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

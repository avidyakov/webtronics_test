import pytest
import requests
from django.contrib.auth import get_user_model
from furl import furl
from mimesis import Person, Text
from mimesis.enums import Locale
from rest_framework_simplejwt.tokens import RefreshToken

from post_app.models import Post


@pytest.fixture
def user_pass():
    person = Person(Locale.RU)
    return person.password()


@pytest.fixture
def user(user_pass):
    person = Person(Locale.RU)
    user = get_user_model().objects.create(
        first_name=person.first_name(),
        last_name=person.last_name(),
        email=person.email(),
        username=person.username()
    )

    user.set_password(user_pass)
    user.save()

    return user


@pytest.fixture
def post(user):
    text = Text()
    return Post.objects.create(
        title=text.title(),
        description=text.text(),
        author=user
    )


@pytest.fixture
def session():
    return requests.Session()


@pytest.fixture
def login_session(user):
    s = requests.Session()
    refresh = RefreshToken.for_user(user)
    s.headers.update({'Authorization': f'Bearer {refresh.access_token}'})
    return s


@pytest.fixture
def url():
    return furl('http://0.0.0.0:8000')

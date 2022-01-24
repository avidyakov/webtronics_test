from http import HTTPStatus

from django.urls import reverse
from mimesis import Person


def test_user_signup(session, url):
    person = Person()
    password = person.password()

    response = session.post((url / reverse('user:create')).url, {
        'first_name': person.first_name(),
        'last_name': person.last_name(),
        'email': person.email(),
        'password': password,
        'password2': password,
        'username': person.username()
    })
    assert response.status_code == HTTPStatus.CREATED

from http import HTTPStatus

import pytest
from django.urls import reverse
from mimesis import Text


@pytest.mark.django_db
def test_post_create(user, login_session, url):
    text = Text()
    response = login_session.post(
        (url / reverse('post:post-list')).url,
        {'title': text.title(), 'description': text.text()}
    )
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_post_like(login_session, post, url):
    response = login_session.post((url / reverse('post:post-like', args=[post.id])).url)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_post_unlike(login_session, post, url):
    response = login_session.delete((url / reverse('post:post-like', args=[post.id])).url)
    assert response.status_code == HTTPStatus.NO_CONTENT

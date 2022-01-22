from django.urls import path

from user_app.views import UserCreateAPIView

app_name = 'user_app'

urlpatterns = [
    path('', UserCreateAPIView.as_view())
]

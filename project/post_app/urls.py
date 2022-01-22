from rest_framework.routers import DefaultRouter

from post_app.views import PostViewSet

app_name = 'post_app'

router = DefaultRouter()
router.register('', PostViewSet, basename='post')

urlpatterns = [
    *router.urls
]

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(title='API', default_version='v1'),
   public=True,
   permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('post/', include('post_app.urls', namespace='post')),
    path('user/', include('user_app.urls', namespace='user')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
]

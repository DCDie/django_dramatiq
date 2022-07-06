from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Project API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('task/', include('apps.task.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('jwt/', include([
        path('token/', TokenObtainPairView.as_view(), name='token_obtain-pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    ])),
]


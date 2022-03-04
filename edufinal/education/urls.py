"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls.static import static
from education.settings import common, production
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="EDUCATION API",
      default_version='v1',
      description="EDUCATION Api docs confidentails",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@EDUCATION.com"),
      license=openapi.License(name="EDUCATION License"),
   ),
   public=True,   
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/', include('auth_user_app.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]

if settings.DEBUG:
    urlpatterns += static(common.STATIC_URL, document_root=common.STATIC_ROOT)
    urlpatterns += static(common.MEDIA_URL, document_root=common.MEDIA_ROOT)
else:
    urlpatterns += static(common.STATIC_URL, document_root=common.STATIC_ROOT)
    urlpatterns += static(production.MEDIA_URL, document_root=common.MEDIA_ROOT)
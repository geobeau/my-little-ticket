"""Root URLs."""

from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()

schema_view = get_swagger_view(title='My Little Ticket')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'swagger/', schema_view),
    path(r'api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path(r'admin/', admin.site.urls),
    path(r'accounts/', include('allauth.urls')),
    path(r'health/', include('health_check.urls')),
    path(r'', include('django_prometheus.urls')),
    path(r'', include('my_little_ticket.tickets.urls'),)
]
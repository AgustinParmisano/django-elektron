"""elektron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from devices import views as device_views
from data import views as data_views
from tasks import views as task_views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'devices', device_views.DeviceViewSet)
router.register(r'users', device_views.UserViewSet)
router.register(r'data', data_views.DataViewSet)
router.register(r'tasks', task_views.TaskViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import url, include
from devices import views
from data import views
from tasks import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'data', views.DataViewSet)
router.register(r'tasks', views.TasksViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('devices.urls')),
    url(r'^', include('tasks.urls')),
    url(r'^', include('data.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='elektron')),
]
"""

from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^datatasks$', views.DataTaskIndexView.as_view(), name='datatask_index'),
    url(r'^datetimetasks$', views.DateTimeTaskIndexView.as_view(), name='datatimetask_index'),
    url(r'^datatasks/(?P<pk>[0-9]+)/$', views.DataTaskDetailView.as_view(), name='datatask_detail'),
    url(r'^datetimetasks/(?P<pk>[0-9]+)/$', views.DateTimeTaskDetailView.as_view(), name='datatimetask_detail'),
    url(r'^create$', csrf_exempt(views.CreateView.as_view()), name='create'),
    url(r'^devices/(?P<pk>[0-9]+)/datetimetask$', csrf_exempt(views.DatetimeTaskDeviceView.as_view()), name='device_datetimetask'),
    url(r'^devices/(?P<pk>[0-9]+)/datatask$', csrf_exempt(views.DataTaskDeviceView.as_view()), name='device_datatask'),
]

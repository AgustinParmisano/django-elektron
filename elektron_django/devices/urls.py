from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'devices'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^recognition$', views.RecognitionView.as_view(), name='recognition'),
    url(r'^create$', csrf_exempt(views.CreateView.as_view()), name='create'),
    url(r'^data$', csrf_exempt(views.DeviceMacDataView.as_view()), name='data_device_mac'),
    url(r'^task$', csrf_exempt(views.DeviceMacTaskView.as_view()), name='task_device_mac'),
    url(r'^(?P<pk>[0-9]+)/data$', csrf_exempt(views.DeviceDataView.as_view()), name='data'),
    url(r'^(?P<pk>[0-9]+)/tasks$', csrf_exempt(views.DeviceTaskView.as_view()), name='task'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$', csrf_exempt(views.DeviceDataDatesView.as_view()), name='data_dates'),
]

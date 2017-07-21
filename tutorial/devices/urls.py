from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from devices import views

urlpatterns = [
    url(r'^devices/$', views.device_list),
    url(r'^devices/(?P<pk>[0-9]+)/$', views.device_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

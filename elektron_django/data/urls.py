from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'data'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create$', csrf_exempt(views.CreateView.as_view()), name='create'),
]

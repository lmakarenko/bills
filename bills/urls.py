from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.counter_data_list, name='counter_data_list'),
    url(r'^counter/(?P<pk>[0-9]+)/$', views.counter_data_by, name='counter_data_by'),
]

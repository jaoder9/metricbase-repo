from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.newmetric, name='newmetric'),
    url(r'^metrics/(?P<pk>\d+)/$', views.showmetric, name='showmetric'),
    url(r'', views.allmetrics, name='index'),
    url(r'^metrics/$', views.allmetrics, name='allmetrics'),

]

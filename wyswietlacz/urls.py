from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^projects/$', 'wyswietlacz.views.projects'),
    url(r'^choice/$', 'wyswietlacz.views.choice'),
    url(r'^detail/(?P<pk>\d+)/$', 'wyswietlacz.views.project_detail', name="project_detail"),
    url(r'^developers/$', 'wyswietlacz.views.developers'),
    url(r'^createdev/$', 'wyswietlacz.views.createdev'),
    url(r'^createproject/$', 'wyswietlacz.views.createproject'),
    url(r'^tasks/$', 'wyswietlacz.views.tasks'),
    url(r'^createtask/$', 'wyswietlacz.views.createtask'),
    )
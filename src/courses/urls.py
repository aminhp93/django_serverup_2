from django.conf.urls import url
from django.contrib import admin

from .views import HomeView
from videos.views import (
        CourseListView, 
        CourseDetailView, 
        CourseCreateView,
        CourseUpdateView,
        CourseDeleteView,
    )

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video_detail'),
    url(r'^create/$', CourseCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CourseUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CourseDeleteView.as_view(), name='delete'),
] 

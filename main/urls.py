from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^style/$', views.ShowImageController),
    url(r'^vidplayer/$', views.VideoPlayerController , name="vid_player"),

 ]

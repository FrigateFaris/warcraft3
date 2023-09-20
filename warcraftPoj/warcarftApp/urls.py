from django.urls import path, include
from warcarftApp.views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('audios/', AudiosView.as_view(), name='audio'),
    path('videos/', VideoView.as_view(), name='video'),
    path('photo/', ScreensListView.as_view(), name='screen'),
    path('audios/replicas/', ReplicasListView.as_view(), name='replicas'),
    path('audios/music/', MusicListView.as_view(), name='musics'),
    path('video/game_process', GameProcessPageView.as_view(), name='game_process'),
    path('video/cinematic', CinematicPageView.as_view(), name='cinematic'),
]


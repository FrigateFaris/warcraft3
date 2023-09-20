from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView, ListView
from warcarftApp.models import *


class StartPageView(TemplateView):
    template_name = 'warcarftApp/startPage.html'


class AboutPageView(TemplateView):
    template_name = 'warcarftApp/about.html'


class AudiosView(TemplateView):
    template_name = 'warcarftApp/audios.html'


class VideoView(TemplateView):
    template_name = 'warcarftApp/videos.html'


class GameProcessPageView(ListView):
    template_name = 'warcarftApp/videos/gameProcess.html'
    model = GameProcess
    context_object_name = 'game_process'


class CinematicPageView(ListView):
    template_name = 'warcarftApp/videos/cinematics.html'
    model = Cinematic
    context_object_name = 'cinematics'


class ScreensListView(ListView):
    template_name = 'warcarftApp/screens.html'
    model = Screens
    context_object_name = 'screens'


class ReplicasListView(ListView):
    template_name = 'warcarftApp/audios/replicas.html'
    model = Replicas
    context_object_name = 'replicas'


class MusicListView(ListView):
    template_name = 'warcarftApp/audios/music.html'
    model = Musics
    context_object_name = 'musics'

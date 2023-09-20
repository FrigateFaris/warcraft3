from django.db import models


# Create your models here.
class Screens(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photo/')

    def __str__(self):
        return f'{self.title}'


class GameProcess(models.Model):
    title = models.CharField(max_length=250)
    game_process_video = models.FileField(upload_to='video/')

    def __str__(self):
        return f'{self.title}'


class Cinematic(models.Model):
    title = models.CharField(max_length=250)
    cinematic_video = models.FileField(upload_to='video/')

    def __str__(self):
        return f'{self.title}'


class Replicas(models.Model):
    title = models.CharField(max_length=250)
    replicas = models.FileField(upload_to='audio/')

    def __str__(self):
        return f'{self.title}'


class Musics(models.Model):
    title = models.CharField(max_length=250)
    musics = models.FileField(upload_to='audio/')

    def __str__(self):
        return f'{self.title}'

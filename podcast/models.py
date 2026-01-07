from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title


from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey('Episode', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'episode')  # منع التكرار

    def __str__(self):
        return f"{self.user.username} - {self.episode.title}"

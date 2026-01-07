from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcast, Episode, Favorite
from django.contrib import messages


# الصفحة الرئيسية
def home(request):
    podcasts = Podcast.objects.all()
    return render(request, "podcast/index.html", {
        "podcasts": podcasts
    })


# صفحة الحلقات
def episodes(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    episodes = Episode.objects.filter(podcast=podcast)

    if request.method == "POST":
        episode_id = request.POST.get("episode_id")
        episode = get_object_or_404(Episode, id=episode_id)

        Favorite.objects.get_or_create(
            user=request.user,
            episode=episode
        )
        return redirect(request.path)

    return render(request, "podcast/episodes.html", {
        "podcast": podcast,
        "episodes": episodes
    })


# صفحة المفضلة
def favorite(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "podcast/favorite.html", {
        "favorites": favorites
    })

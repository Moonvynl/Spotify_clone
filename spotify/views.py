from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views import View
from .models import *
from django.urls import reverse_lazy
from .forms import *
import time
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json


class SideBar(TemplateView):
    template_name = "spotify/sidebar.html" 

    def get(self, request, *args, **kwargs):
        playlists = Playlist.objects.filter(user = request.user.id)
        return render(request, "spotify/sidebar.html", {"playlists": playlists})


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        my_playlists = Playlist.objects.filter(user = request.user.id)
        if request.user.is_authenticated:
            return render(request, "spotify/main.html", {"playlists": my_playlists})
        else:
            return render(request, "spotify/non_auth_main.html")


class UserProfile(TemplateView):
    def get(self, request, *args, **kwargs):
        playlists = Playlist.objects.filter(user = request.user.id)
        return render(request, "spotify/user_profile.html", {'playlists': playlists})


class AuthorDetailsView(DetailView):
    model = CustomUser
    template_name = "spotify/author_details.html"
    context_object_name = 'author'

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        songs = Song.objects.filter(artist=self.object)
        user_playlists = Playlist.objects.filter(user=self.request.user)
        context['songs'] = songs
        context['user_playlists'] = user_playlists
        return context


class SongsView(ListView):
    model = Song
    context_object_name = "songs"
    template_name = "spotify/main.html"  


class PlaylistDetail(DetailView, UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "spotify/playlist_detail.html"

    def get_success_url(self):
        return reverse_lazy('spotify:playlist-detail', kwargs={'pk': self.object.id})

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_playlists'] = Playlist.objects.filter(user=self.request.user)
        return context


class Search(View):
    def get(self, request, *args, **kwargs):
        user_playlists = Playlist.objects.filter(user=request.user.id)
        query = request.GET.get('query')
        songs = None
        playlists = None
        if query:
            songs = Song.objects.filter(title__icontains=query)
            playlists = Playlist.objects.filter(title__icontains=query)
        print(songs)
        print(playlists)
        return render(request,
                    'spotify/search.html', 
                    {'songs': songs, 'playlists': playlists, 'user_playlists': user_playlists})


class CreatePlaylist(View):
    def get(self, request, *args, **kwargs):
        playlist = Playlist.objects.create(
            title="New Playlist",
            user = request.user)
        playlist.save()
        return render(request, 'spotify/playlist_detail.html', {'playlist': playlist})


def add_song_to_playlist(request, pk):
    song = Song.objects.get(pk=pk)
    playlist_id = request.POST.get('playlist_id')
    playlist = Playlist.objects.get(pk=playlist_id)
    playlist.songs.add(song)
    playlist.save()

    return render(request, 'spotify/playlist_detail.html', {'playlist':playlist})


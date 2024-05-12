from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user-profile/', UserProfile.as_view(), name='user-profile'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('spotify:home')), name='logout'),
    path('sidebar/', SideBar.as_view(), name='sidebar'),
    path('songs/', SongsView.as_view(), name='songs'),
    path('playlist/<int:pk>/', PlaylistDetail.as_view(), name='playlist-detail'),
    path('playlist/create/', CreatePlaylist.as_view(), name='playlist-create'),
    path('search/', Search.as_view(), name='search'),
    path('add-song-to-playlist/<int:pk>/', add_song_to_playlist, name='add-song-to-playlist'),
    path('author-detail/<int:pk>/', AuthorDetailsView.as_view(), name='author-detail'),
]

app_name = 'spotify'
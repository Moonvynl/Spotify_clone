from django import forms
from .models import *
from auth_system.models import CustomUser

class AddSongToPlaylistForm(forms.Form):
    song = forms.ModelChoiceField(queryset=Song.objects.all(), empty_label=None)

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title','img'] 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'avatar']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }
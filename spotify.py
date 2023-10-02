
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, environ

env = environ.Env()
environ.Env.read_env()


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=env("SPOTIFY_CLIENT_ID"),
                                                           client_secret=env("SPOTIFY_CLIENT_SECRET")))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
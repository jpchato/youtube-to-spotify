import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Spotify client ID and client secret from environment variables
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Authenticate with the Spotify Web API
print(spotify_client_id, spotify_client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="https://open.spotify.com/", scope="playlist-modify-private"))

# Search for tracks on Spotify and retrieve track URIs
spotify_tracks = []
videos = ['Current Joys - A Different Age', 'Stumble On Tapes: Hollows', 'Friends of Clay - Flowers and Daggers (Official Music Video)', 'Son Little - "Lay Down"', 'Ativin - Haunt Blue (Official Video)', 'Men I Trust - Show Me How', 'Pachyman - Goldline', 'Low Hum - Comatose', 'Emelia Austin - Desire To Reveal', 'A Circle Town', 'Current Joys - Fear', 'Blondie', 'New Flesh', 'Ralph Taylor - Caught in A Moment', 'Bedroom - In My Head (Official Audio)', 'Stumble On Tapes - Surf Curse', 'Lauren Early - Lemon', 'Punch', 'Current Joys - Alabama', 'Dayglow - Can I Call You Tonight? (Official Video)']
for video_info in videos:
    results = sp.search(q=video_info, type="track", limit=1)
    if results["tracks"]["items"]:
        spotify_tracks.append(results["tracks"]["items"][0]["uri"])

print(spotify_tracks)

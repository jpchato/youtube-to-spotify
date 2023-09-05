import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="https://open.spotify.com/",
        scope="user-top-read"
    ))

def get_top_tracks(sp, time_range, limit):
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    return top_tracks["items"]

def main():
    sp = authenticate_spotify()

    time_ranges = ["short_term", "medium_term", "long_term"]
    limit = 50

    for time_range in time_ranges:
        top_tracks = get_top_tracks(sp, time_range, limit)
        print(f"Top {limit} tracks for {time_range.replace('_', ' ')}:")
        for idx, track in enumerate(top_tracks, start=1):
            artists = ", ".join([artist["name"] for artist in track["artists"]])
            print(f"{idx}. {track['name']} - {artists}")

if __name__ == "__main__":
    main()

import os
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def retrieve_youtube_videos(api_key, playlist_id, max_results=10):
    max_results = min(max_results, 50)  # Limit max_results to 50
    youtube_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults={max_results}"

    response = requests.get(youtube_url)
    data = response.json()

    # Extract video information from the response
    videos = []
    for item in data["items"]:
        video_info = item["snippet"]["title"]
        videos.append(video_info)
    
    return videos

def search_spotify_tracks(videos, sp):
    # Search for tracks on Spotify and retrieve track URIs
    spotify_tracks = []
    for video_info in videos:
        results = sp.search(q=video_info, type="track", limit=1)
        if results["tracks"]["items"]:
            spotify_tracks.append(results["tracks"]["items"][0]["uri"])
    
    return spotify_tracks

def create_spotify_playlist(playlist_name, playlist_description, user_id, spotify_tracks, sp):
    # Create a new playlist on Spotify
    new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

    # Add tracks to the new playlist
    sp.playlist_add_items(new_playlist["id"], spotify_tracks)

    print("Playlist created and tracks added.")

def main():
    load_dotenv()

    # Retrieve the YouTube API key from the environment variables
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    if not youtube_api_key:
        raise ValueError("YouTube API key not found in environment variables.")

    # Continue with the rest of the script
    playlist_id = input("Enter YouTube playlist ID: ")  # Prompt for YouTube playlist ID

    # Prompt for max_result with default value
    max_result = input("Enter the number of videos to retrieve (default is 10, max is 50): ")
    try:
        max_result = int(max_result)
    except ValueError:
        max_result = 10  # Use default if input is not a valid number
    max_result = min(max_result, 50)  # Limit max_result to 50

    # Prompt for playlist_name with default value
    playlist_name = input("Enter playlist name (default is 'Converted YoutubeMix'): ")
    if not playlist_name:
        playlist_name = "Converted YoutubeMix"
    playlist_name = playlist_name[:100]  # Limit playlist name to 100 characters

    videos = retrieve_youtube_videos(youtube_api_key, playlist_id, max_result)

    # Retrieve Spotify client ID and client secret from environment variables
    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    # Authenticate with the Spotify Web API
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="YOUR_REDIRECT_URI", scope="playlist-modify-private"))

    spotify_tracks = search_spotify_tracks(videos, sp)

    # Continue with the rest of the script
    playlist_description = "This playlist contains tracks from a converted YouTube mix."
    user_id = sp.me()["id"]
    create_spotify_playlist(playlist_name, playlist_description, user_id, spotify_tracks, sp)

if __name__ == "__main__":
    main()

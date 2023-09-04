import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the YouTube API key from the environment variables
youtube_api_key = os.getenv("YOUTUBE_API_KEY")
if not youtube_api_key:
    raise ValueError("YouTube API key not found in environment variables.")

# Continue with the rest of the script
playlist_id = "RDn1h1AOeVQ38"
max_results = 20
youtube_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={youtube_api_key}&maxResults={max_results}"

response = requests.get(youtube_url)
data = response.json()

# Extract video information from the response
print(data)
videos = []
for item in data["items"]:
    video_info = item["snippet"]["title"]
    videos.append(video_info)

print(videos)

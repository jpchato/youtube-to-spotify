# YouTube to Spotify Playlist Converter

This script allows you to convert a YouTube playlist to a Spotify playlist. It retrieves video titles from a YouTube playlist, searches for corresponding tracks on Spotify, and creates a new Spotify playlist with those tracks.

## Prerequisites

Before using this script, you'll need the following:

- YouTube API key: Obtain a YouTube API key by following the instructions here: https://developers.google.com/youtube/registering_an_application.
- Spotify API credentials: Create a Spotify application and obtain the client ID and client secret from the Spotify Developer Dashboard: https://developer.spotify.com/dashboard/applications.
- Python environment: Ensure you have Python installed, and use a virtual environment (`venv`) for managing dependencies.

## Setup

1. Clone this repository:
    -   git clone https://github.com/your-username/youtube-to-spotify-converter.git
    - cd youtube-to-spotify-converter


2. Install dependencies:
    - pip install -r requirements.txt


3. Create a `.env` file in the project root directory with the following content:

    - YOUTUBE_API_KEY=your_youtube_api_key
    - SPOTIFY_CLIENT_ID=your_spotify_client_id
    - SPOTIFY_CLIENT_SECRET=your_spotify_client_secret


Replace `your_youtube_api_key`, `your_spotify_client_id`, and `your_spotify_client_secret` with your actual API keys and credentials.

## Usage

Run the script by executing the following command in the terminal:

    - python3 convert_youtube_playlist_to_spotify_playlist.py


Follow the prompts to provide the YouTube playlist ID, specify the maximum number of videos to retrieve, and set the playlist name for Spotify.

## Notes

- The script limits the number of videos retrieved to 50 due to Spotify API limitations.
- The playlist name is limited to 100 characters to ensure compatibility with Spotify.
- Make sure to configure your redirect URI in the Spotify Developer Dashboard.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

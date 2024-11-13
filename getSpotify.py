import spotipy
import csv
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'id'
CLIENT_SECRET = 'secret'
REDIRECT_URI = 'http://localhost:8888/callback'

SCOPE = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def export_playlists_to_csv():
    playlists = sp.current_user_playlists()

    with open('spotify_playlists.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Playlist Name', 'Track Name', 'Artists', 'Album', 'Release Date', 'Duration (ms)', 'Popularity', 'Track ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for playlist in playlists['items']:
            playlist_name = playlist['name']
            playlist_id = playlist['id']

            results = sp.playlist_tracks(playlist_id)
            tracks = results['items']

            for item in tracks:
                track = item['track']
                track_name = track['name']
                artists = ', '.join([artist['name'] for artist in track['artists']])
                album_name = track['album']['name']
                release_date = track['album']['release_date']
                duration_ms = track['duration_ms']
                popularity = track['popularity']
                track_id = track['id']

                writer.writerow({
                    'Playlist Name': playlist_name,
                    'Track Name': track_name,
                    'Artists': artists,
                    'Album': album_name,
                    'Release Date': release_date,
                    'Duration (ms)': duration_ms,
                    'Popularity': popularity,
                    'Track ID': track_id
                })

    print("Data exported to spotify_playlists.csv")

export_playlists_to_csv()
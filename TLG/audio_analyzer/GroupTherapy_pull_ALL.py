import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

# Storing my Spotify API credentials - delete before commit!
CLIENT_ID = ''
CLIENT_SECRET = ''

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create a list to store albums and their songs
album_list = []

def episode_lookup():
    # Defining artist URI
    artist_uri = "spotify:artist:7HXnQUEKHiWvUqSIR9ydOC"  # Replace with the artist's URI

    # Search for the albums by the artist using Spotify API
    albums = sp.artist_albums(artist_uri, album_type='album', limit=50)  # Adjust the limit as needed

    # Check if there are albums in the response
    if 'items' in albums:
        count = 0
        for album in albums['items']:
            if count == 3:
                break
            album_data = {
                "Album Name": album['name'],
                "Album URI": album['uri'],
                "Release Date": album['release_date'],
                "Songs": []
            }
            get_album_tracks(album_data)
            album_list.append(album_data)
            count += 1
    else:
        print(f"No albums found for the artist")

def get_album_tracks(album_data):
    # Retrieve tracks from the album using the album URI
    album_tracks = sp.album_tracks(album_data["Album URI"])

    track_data_list = []
    for track in album_tracks['items']:
        track_data = {
            "Track Name": track['name'],
            "Track Data": {
                "Artist Name": [artist['name'] for artist in track['artists']],
                "Artist URI": track['artists'][0]['uri'],  # Assuming the first artist is the primary one
                "Track URI": track['uri'],
                "Spotify ID": track['id'],
                "Analysis Data": get_track_analysis(track['uri'])
                # Add more track-specific data here
            }
        }
        track_data_list.append(track_data)

    album_data["Songs"] = track_data_list

def get_track_analysis(track_uri):
    # Retrieve audio analysis data for the track
    audio_features = sp.audio_features([track_uri])[0]  # Pass a list with a single URI and access the first element
    
    # Extract the relevant analysis data you need
    audio_features_data = {
        'Key': audio_features['key'],
        'Mode': audio_features['mode'],
        'Danceability': audio_features['danceability'],
        'Energy': audio_features['energy'],
        'Loudness': audio_features['loudness'],
        'Speechiness': audio_features['speechiness'],
        'Acousticness': audio_features['acousticness'],
        'Instrumentalness': audio_features['instrumentalness'],
        'Liveness': audio_features['liveness'],
        'Valence': audio_features['valence'],
        'Tempo': audio_features['tempo']
        # Add more analysis data here
    }
    return audio_features_data

episode_lookup()

# Save the album data as a JSON file
filename = 'album_data_2.json'
def write_album_data_to_file(album_list, filename):
    with open(filename, 'w') as f:
        json.dump(album_list, f, indent=4)

write_album_data_to_file(album_list, filename)


"""with open('album_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(album_list, json_file, ensure_ascii=False, indent=4)

print("Data saved as album_data.json")"""

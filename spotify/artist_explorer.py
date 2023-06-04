import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

<<<<<<< HEAD
# storing my Spotify API credentials - delete before commit!
CLIENT_ID = 
CLIENT_SECRET = 
=======
# Storing my Spotify API credentials - delete before commit!
CLIENT_ID = '349309ae5ef349eb85096837bc86547b'
CLIENT_SECRET = '2c5d4880a00a4bba80c915b55ccb54b5'
>>>>>>> cddf393 (formatting and bokeh improvements)

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Defining CSV and field names
csv_file = '50_tracks.csv'
field_names = ['Artist Name', 'Artist URI', 'Track Name', 'Track URI', 'Album',
               'Key', 'Mode', 'Danceability', 'Energy', 'Loudness', 'Speechiness',
               'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Embed Code']

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()


def artist_lookup():
    # Prompt the user for an artist name
    user_artist = input("Enter an artist: ")

    # Search for the artist using Spotify API
    results = sp.search(q='artist:' + user_artist, type='artist', limit=1)

    # Get the artist URI from the search results
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_uri = artist['uri']
        top_tracks(artist_uri, user_artist)
        related_artists(artist_uri)
    else:
        print("Artist not found.")


def top_tracks(artist_uri, user_artist):
    results = sp.artist_top_tracks(artist_uri)
    tracks = results['tracks']

    print("\n\nThe top 10 tracks for the artist are...\n")
<<<<<<< HEAD
    with open(csv_file, 'a', newline='') as file: # opening our csv to append
        writer = csv.DictWriter(file, fieldnames=field_names) # using writer to write to csv
=======
    with open(csv_file, 'a', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
>>>>>>> cddf393 (formatting and bokeh improvements)
        for track in tracks:
            track_uri = track['uri'][14:]
            track_info = sp.track(track_uri)
            audio_features = sp.audio_features(track_uri)

            # Perform Spotify oEmbed lookup
            oembed_api_url = (f'https://open.spotify.com/oembed?url=https://open.spotify.com/track/{track_uri}&format=json')
            response = requests.get(oembed_api_url)

            if response.status_code == 200:
                oembed_data = response.json()
                embedded_html = oembed_data['html']
            else:
                embedded_html = ''

            writer.writerow({
                'Artist Name': user_artist,
                'Artist URI': artist_uri[15:],
                'Track Name': track['name'],
                'Track URI': track_uri,
                'Album': track_info['album']['name'],
                'Key': audio_features[0]['key'],
                'Mode': audio_features[0]['mode'],
                'Danceability': audio_features[0]['danceability'],
                'Energy': audio_features[0]['energy'],
                'Loudness': audio_features[0]['loudness'],
                'Speechiness': audio_features[0]['speechiness'],
                'Acousticness': audio_features[0]['acousticness'],
                'Instrumentalness': audio_features[0]['instrumentalness'],
                'Liveness': audio_features[0]['liveness'],
                'Valence': audio_features[0]['valence'],
                'Tempo': audio_features[0]['tempo'],
                'Embed Code': embedded_html
            })

            print(f"{track['name']}")


def related_artists(artist_uri):
    print("\nAnd 4 related artists... ")
    related = sp.artist_related_artists(artist_uri)
    related_artists_uris = []
    for artist in related['artists'][:4]:
        print(artist['name'])
        artist_uri = artist['uri']
        related_artists_uris.append(artist_uri)
        top_tracks(artist_uri, artist['name'])


artist_lookup()

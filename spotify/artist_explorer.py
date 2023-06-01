import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# storing my Spotify API credentials - delete before commit!
CLIENT_ID = 
CLIENT_SECRET = 

# authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# defining CSV and field names
csv_file = '50_tracks.csv'
field_names = ['Artist Name', 'Artist URI', 'Track Name', 'Track URI', 'Album',
               'Key', 'Mode', 'Danceability', 'Energy', 'Loudness', 'Speechiness',
               'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']

with open(csv_file, 'w', newline='') as file: # opening our csv to append
        writer = csv.DictWriter(file, fieldnames=field_names) # using writer to write to csv
        writer.writeheader() # writing the header

def artist_lookup():
    # prompt the user for an artist name
    user_artist = input("Enter an artist: ")

    # search for the artist using Spotify API
    results = sp.search(q='artist:' + user_artist, type='artist', limit=1)

    # get the artist URI from the search results
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_uri = artist['uri'] # last two lines will save the 0th/first item from results as the artist_uri
        top_tracks(artist_uri, user_artist) # pass artist_uri, user_artist as arguments to top_tracks function
        related_artists(artist_uri) # pass artist_uri to related_artists function
    else:
        print("Artist not found.") # if results doesn't return artists, items, else

def top_tracks(artist_uri, user_artist):
    results = sp.artist_top_tracks(artist_uri) # takes the artist_uri as an argument for top tracks
    tracks = results['tracks'] # pulls just tracks from the results

    print("\n\nThe top 10 tracks for the artist are...\n")
    with open(csv_file, 'a', newline='') as file: # opening our csv to append
        writer = csv.DictWriter(file, fieldnames=field_names) # using writer to write to csv
        for track in tracks:
            track_uri = track['uri'][14:] # pulls just the uri, drops the first 14 characters (spotify:track:)
            track_info = sp.track(track_uri) # gets additional track info for each track from track_uri
            audio_features = sp.audio_features(track_uri) # gets audio features, defined as  below, for each track

            writer.writerow({
                'Artist Name': user_artist,
                'Artist URI': artist_uri[15:], # dropping 15 characters here
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
                'Tempo': audio_features[0]['tempo']
            }) # might want to modify some values here, but this is good for now

            print(f"{track['name']}")

def related_artists(artist_uri): # creating a function to find related artists
    print("\nAnd 4 related artists... ")
    related = sp.artist_related_artists(artist_uri) # passing artist_uri into sp.artist_related_artists
    related_artists_uris = []
    for artist in related['artists'][:4]:
        print(artist['name'])
        artist_uri = artist['uri']
        related_artists_uris.append(artist_uri) # appending to the list
        top_tracks(artist_uri, artist['name']) # sending this through top_tracks
        #print(related_artists_uris)

artist_lookup()
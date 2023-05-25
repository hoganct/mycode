import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = '349309ae5ef349eb85096837bc86547b'
CLIENT_SECRET = 'c06e23caa93b489db429fc3ac6233ad6'

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Prompt the user for an artist name
artist_name = input("Enter an artist name: ")

# Search for the artist using Spotify API
results = spotify.search(q='artist:' + artist_name, type='artist', limit=1)

# Get the artist URI from the search results
if results['artists']['items']:
    artist = results['artists']['items'][0]
    artist_uri = artist['uri']
    print("Artist URI:", artist_uri)
else:
    print("Artist not found.")

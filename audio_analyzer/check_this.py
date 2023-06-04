import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist = str(input("What artist would you like to query? "))

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=,
                                                           client_secret=))

results = sp.search(q=artist, limit=10)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
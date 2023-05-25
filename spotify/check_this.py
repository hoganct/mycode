import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist = str(input("What artist would you like to query? "))

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='349309ae5ef349eb85096837bc86547b',
                                                           client_secret='c06e23caa93b489db429fc3ac6233ad6'))

results = sp.search(q=artist, limit=10)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
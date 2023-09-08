import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, CategoricalColorMapper
from bokeh.layouts import column
from bokeh.models.widgets import Div

# Storing my Spotify API credentials - delete before commit!
CLIENT_ID = '349309ae5ef349eb85096837bc86547b'
CLIENT_SECRET = '2c5d4880a00a4bba80c915b55ccb54b5'

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Defining CSV and field names
csv_file = '50_tracks.csv'
field_names = ['Artist Name', 'Artist URI', 'Track Name', 'Track URI', 'Album',
               'Key', 'Mode', 'Danceability', 'Energy', 'Loudness', 'Speechiness',
               'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Embed Code']

# Writing to the csv
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
        top_tracks(artist_uri, user_artist) # Passing to top_tracks, with artist_uri and user_artist as arguments
        related_artists(artist_uri) # Passing to related_artists, with artist_uri as argument
    else:
        print("Artist not found.")


def top_tracks(artist_uri, user_artist):
    results = sp.artist_top_tracks(artist_uri) # Saving as results
    tracks = results['tracks'] # Looking for just tracks

    print("\n\nThe top 10 tracks for the artist are...\n")
    with open(csv_file, 'a', newline='', encoding="utf-8") as file: # Opening and appending the csv now
        writer = csv.DictWriter(file, fieldnames=field_names)
        for track in tracks:
            track_uri = track['uri'][14:] # Dropping the first 15 characters (spotify:tracks:) from the output
            track_info = sp.track(track_uri) # Getting information for each track, such as Album Name
            audio_features = sp.audio_features(track_uri) # Getting audio features

            # Perform Spotify oEmbed lookup
            oembed_api_url = (f'https://open.spotify.com/oembed?url=https://open.spotify.com/track/{track_uri}&format=json')
            response = requests.get(oembed_api_url)

            if response.status_code == 200:
                oembed_data = response.json()
                embedded_html = oembed_data['html'] # Taking just the html portion of the response.json()
            else:
                embedded_html = ''

            writer.writerow({ # Writing everything to the csv now
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


def related_artists(artist_uri): # Using this to look up the 4 most closely related artists for the user_artist
    print("\nAnd 4 related artists... ")
    related = sp.artist_related_artists(artist_uri)
    related_artists_uris = []
    for artist in related['artists'][:4]: # Limiting to just 4
        print(artist['name'])
        artist_uri = artist['uri']
        related_artists_uris.append(artist_uri) # Appending to the list
        top_tracks(artist_uri, artist['name']) # Running each of these through top_tracks


artist_lookup()

# Reading CSV made from artist_explorer.py
df = pd.read_csv('50_tracks.csv', encoding='utf-8')

# Select the columns from the 8th field onwards - just the floats and tempo, no strings
data_columns = df.columns[7:-1]  # Exclude the last column "Embed Code"

# Normalizing with Min-Max scaling - this will take tempo and convert it into a 0-1 value
scaler = MinMaxScaler()
df[data_columns] = scaler.fit_transform(df[data_columns])

# Calculate the variances for each field
variances = df[data_columns].var()

# Sort the fields based on their variances in descending order
sorted_variances = variances.sort_values(ascending=False)
print("All of the variances:")
print(sorted_variances)

# Select the top two fields with the highest variances
top_two_fields = sorted_variances.head(2)
field1 = top_two_fields.index[0]  # Get the field name of the first field
field2 = top_two_fields.index[1]  # Get the field name of the second field

print(f"The two fields with the greatest variance are {field1} and {field2}.\n")

# Ask the user if they want to use the fields with the greatest variance or define their own fields
user_choice = input("Would you like select your own categories to analyze? (Y/N): ")

if user_choice.lower() == 'y':
    field1 = input("Enter Field 1: ") # Would be nice to incorporate some input filtering/control here
    field2 = input("Enter Field 2: ")

# Print the names of the selected fields
print("\nThe two selected fields are:")
print(field1)
print(field2)

# Get unique artists
artists = df['Artist Name'].unique()

# Defining a color palette for each artist
color_palette = ['#FF0000', '#FF8000', '#000080', '#008000', '#00FFFF']

# Create a color mapper mapping each artist to a color
num_artists = len(artists)
palette = color_palette[:num_artists]
color_mapper = CategoricalColorMapper(factors=artists, palette=palette) # Building using CCM

# Create the scatterplot with colored points
scatterplot = figure()
scatterplot.circle(x=field1, y=field2, source=df, fill_color={'field': 'Artist Name', 'transform': color_mapper}, size=6, legend_field='Artist Name')

"""right about here is the limit of my abilities - this was heavily influenced by stackoverflow research, co-pilot, and ChatGPT"""

# Customize hover tooltips
hover = HoverTool(tooltips=[("Artist", "@{Artist Name}"), ("Track", "@{Track Name}")])
scatterplot.add_tools(hover)

# Set plot attributes
scatterplot.xaxis.axis_label = field1
scatterplot.yaxis.axis_label = field2

# Get the HTML data from the last field for each record
html_data = df.iloc[:, -1]

# Create a Div element to display the HTML data     
html_content = Div(text='', width=800, height=200)

# Concatenate all the HTML data and update the Div element
html_content.text = '\n\n'.join(html_data)

# Create a layout with the scatterplot and the Div element
layout = column(scatterplot, html_content)

# Save the plot as an HTML file and show it
output_file("scatterplot.html")
show(layout)

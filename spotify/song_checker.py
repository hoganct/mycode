#!/usr/bin/env python3

"""the first iteration of this program will,
broadly, prompt the user for an artist and 
return their ten top songs"""

#importing libraries
import requests
from requests.auth import HTTPBasicAuth
import sys
import json

# storing the credentials
CLIENT_ID = 
CLIENT_SECRET = 
GRANT_TYPE = 'client_credentials'

# prompting user for artist
artist = str(input("Which artist would you like to query? "))

# retrieving OAuth2 token to make requests
def get_auth_token():
    body = {
        "grant_type": GRANT_TYPE
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), data=body)
    print(f"AUTH TOKEN: {response.json()['access_token']}")
    return response.json()['access_token']




# this will search for the artist and provide a list of tracks back
def get_search_page(artist, limit, offset, token):
    url = f"https://api.spotify.com/v1/search?q=artist%3A{artist}&type=track&market=US&limit={limit}&offset={offset}"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'})
    return response.json()
    
#print(response.json())

"""if __name__ == "__main__":
    auth_token = get_auth_token()

    limit = 10  # how many items you want on each "page"
    offset = 0  # what "page" you're on

    # Most likely won't run into this super quick, but be careful of Spotify rate limiting you with this while loop
    # total_pages starts at the max int size until we can pull back the max number of pages returned from the search
    total_pages = 1
    while offset < (total_pages):
        # data provides a list of tracks under data['tracks']['items'] for each track there is a list of artists ex:
        # data['tracks']['items'][0]['artists']. You'll be able to pull the name of each artist there and consider
        # them a collaborator of Above & Beyond ex: data['tracks']['items'][0]['artists'][0]['name']
        data = get_search_page(artist, limit, offset, auth_token)
        print(json.dumps(data, indent=2))  # print json page retrieved from search

        total_pages = data['tracks']['items'][0]['artists']
        offset = offset + 1

print(total_pages)"""
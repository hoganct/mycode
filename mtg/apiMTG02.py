#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    # creating the response, our request object
    response = requests.get(f"{API}sets") # using the fstring to add sets to my request (good idea)

    print( dir(response) )

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    post = requests.post(MAJORTOM)
    # send a put with requests.put()
    put = requests.put(MAJORTOM)
    # send a delete with requests.delete()
    delete = requests.delete(MAJORTOM)
    # send a head with requests.head()
    head = requests.head(MAJORTOM)

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for craft in helmetson['people'][0]:
        craft = spacecraft

    for astronaut in helmetson['people']['name'][0]:
        print(f"{astronaut} on the {spacecraft}")

if __name__ == "__main__":
    main()


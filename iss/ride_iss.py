#!/usr/bin/env python3

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading JSON from API"""
    # calling API
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    #print(helmet)
    
    helmetson = json.loads(helmet.decode("utf-8"))

    """print(type(helmet))

    print(type(helmetson))

    print(helmetson["number"])

    print(helmetson["people"])

    print(helmetson["people"][0])"""
    
    for astro in helmetson["people"]:
        print(astro)

    for astro in helmetson["people"]:
        print(astro["name"])

if __name__ == "__main__":
    main()

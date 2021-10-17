#!/bin/python
import random
import json
import requests


api_key = "YOUR GIPHY API KEY"
# Can be fetched from https://developers.giphy.com/dashboard/


def getgif(query: str) -> str:
    """
    Get 1 URL of GIF on a given `query`

    >>> getgif("space ship") 
      Topic: space+ship
      Total urls received:  50
      https://giphy.com/gifs/startrekfleetcommand-BPVIRni1Z70QO2nJMX
    """
    formatted_query: str = "+".join(query.split(" "))
    print("Topic: ", formatted_query)
    url: str = f"http://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    jsdata = requests.get(url)
    data: dict = json.loads(jsdata.content)
    print("Total urls received: ", len(data["data"]))
    return data["data"][random.randint(0, 49)]["url"]


print(getgif("space ship"))

import requests
import json
pokemon_name=input("Enter the name of pokemon")
def get_poke_data(name=pokemon_name):
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

recieved_data=get_poke_data(pokemon_name)

import matplotlib.pyplot as plt
url_data=requests.get(recieved_data["cards"][1]["imageUrl"])
with open("001.png","wb")as f:
    for item in url_data.iter_content(1024):
        f.write(item)
image_data=plt.imread("./001.png")
plt.imshow(image_data)
plt.show()

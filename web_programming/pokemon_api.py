import requests
import json
import matplotlib.pyplot as plt

if __name__ == "__main__":
    name = "pikachu"
    # The image URL is in the content field of the first meta tag
    url = f"https://api.pokemontcg.io/v1/cards?name={name}"
    print(url)
    response = requests.get(url)
    json = response.json()
    recieved_data=json(name)
    url_data=requests.get(recieved_data["cards"][1]["imageUrl"])
    with open("001.png","wb") as f:
        for item in url_data.iter_content(1024):
            f.write(item)
    image_data=plt.imread("./001.png")
    plt.imshow(image_data)
    plt.show()

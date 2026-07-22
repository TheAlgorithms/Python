import requests
import sys


def options():

    print("-" * 5, "Welcome To Daily News", "-" * 5)
    print("Enter 1 For Headlines")
    print("Enter 2 For Topic's")
    print("Enter 3 For Geting News From Your API :)")
    print("Enter 4 For Exit")

    while True:
        try:
            choose = int(input("Choose :"))
            match choose:
                case 1:
                    return Fatch_News()
                case 2:
                    return search()
                case 3:
                    return Fatch_Key()
                case 4:
                    return Exit()

        except ValueError:
            print("Enter Numbers Only")


def Fatch_Key():

    user_key = input("Enter Your API Key :")
    return Fatch_News(user_key)


def search():
    pass


def Fatch_News(user_key=""):  # Enter Your API Key Heare

    url = f"https://newsapi.org/v2/everything?q=keyword&apiKey={user_key}"
    request = requests.get(url)
    data = request.json()

    news = []

    for article in data["articles"]:
        news.append(
            {
                "Title": article["title"],
                "Author": article["author"],
                "Description": article["description"],
            }
        )

    return news


def Exit():

    print("Thanks For Using PDF Tool Kit :)")
    sys.exit()


# Run These Command To Get Info About Type Of Data We Are Dealing With
def Data_Info():
    """Tell Abut Type Of Data We Are Grtting From URL"""

    url = "https://newsapi.org/v2/everything?q=keyword&apiKey=6495169f47154cfd83e9ac94ed500b0a"
    request = requests.get(url)

    data = request.json()

    print(type(data))
    print(data.keys())
    print(data["articles"][0].keys())


if __name__ == "__main__":
    options()

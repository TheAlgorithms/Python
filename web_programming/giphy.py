#!/usr/bin/env python3
import requests


giphy_api_key = "YOUR API KEY"
# Can be fetched from https://developers.giphy.com/dashboard/


def get_gifs(query: str, api_key : str = giphy_api_key) -> list:
    """
    Get a list of URLs of GIF on a given `query`

    >>> getgif("space ship")
    ['https://giphy.com/gifs/studiosoriginals-3ov9jPghXAsbvLmcjm', 'https://giphy.com/gifs/primevideo-the-expanse-theexpanse-2daHMQ9QPwmoSsRYWZ', 'https://giphy.com/gifs/newyorker-space-rocket-bkgsATGfFyrKUf1IsO', 'https://giphy.com/gifs/CBSAllAccess-star-trek-startrek-discovery-pI9dBz15pbGJg03LnE', 'https://giphy.com/gifs/nowthis-aliens-ufo-unidentified-flying-object-TZnOtiTDAnsQUwLs3j', 'https://giphy.com/gifs/DrSquatchSoapCo-mars-bar-marsbar-bars-H1k0w5P3beQHf8OIrr', 'https://giphy.com/gifs/heyduggee-hey-duggee-thespacebadge-XaMTNZkRahZ7ysPMci', 'https://giphy.com/gifs/doctorwho-doctor-who-dr-series-12-PkS3n3TERbjIntnx9E', 'https://giphy.com/gifs/startrekfleetcommand-H03zikfKQPxzuS4ZcE', 'https://giphy.com/gifs/startrekfleetcommand-htJzM2rN0DgbS8g8nC', 'https://giphy.com/gifs/animation-space-weird-RIUZHIBmReqsnztdW2', 'https://giphy.com/gifs/doctorwho-doctor-who-dr-series-12-Vi0EFzgMLWhMOo76SE', 'https://giphy.com/gifs/startrekfleetcommand-BPVIRni1Z70QO2nJMX', 'https://giphy.com/gifs/lego-star-wars-space-SiEz6hxdcJuOf2n3TE', 'https://giphy.com/gifs/nickelodeon-space-astronauts-life-in-krr7nv4iK6Hw2vK5S6', 'https://giphy.com/gifs/rocket-space-ship-X0oEvTEdLj2YU', 'https://giphy.com/gifs/southparkgifs-l2Sqed5gI8GMP09So', 'https://giphy.com/gifs/S3bZdGN7y2MQyNgPF1', 'https://giphy.com/gifs/heyduggee-hey-duggee-thespacebadge-MB0tFoeiKyrdhWAXPM', 'https://giphy.com/gifs/star-wars-teddy-bear-tie-fighter-EpGU43iHxzKrZe3yVv', 'https://giphy.com/gifs/thesims-the-sims-thesimsxstarwars-thesims4starwarsjourneytobatuu-THCL5K4oXsF90sps16', 'https://giphy.com/gifs/time-regret-machine-73h4dfm9DaTRrhFko9', 'https://giphy.com/gifs/space-universe-rocket-l41m6oJBtKRm1NseA', 'https://giphy.com/gifs/thesims-ts-sims-the-Xy21pj6ClKwkz2KsQC', 'https://giphy.com/gifs/CBeebiesHQ-cbeebies-button-clangers-ZEr5tiKWdvpfYa2L9V', 'https://giphy.com/gifs/doctorwho-doctor-who-dalek-daleks-a5EPJWqRznZw6SVXzG', 'https://giphy.com/gifs/peanuts-snoopy-woodstock-in-space-X1gjuOGjIZioNcqKCG', 'https://giphy.com/gifs/funny-weird-aliens-26xBQ7d3MeECbUpCU', 'https://giphy.com/gifs/CBSAllAccess-star-trek-discovery-BHJ8BRu1CgTjoDfvoo', 'https://giphy.com/gifs/doctorwho-doctor-who-dr-the-doctors-wife-L1Phzvvp8Zjfvgr2uy', 'https://giphy.com/gifs/startrekfleetcommand-NRfbanUlUPvdqLzd8O', 'https://giphy.com/gifs/CBeebiesHQ-space-wow-fCUBPlsv3FTkDqtgYG', 'https://giphy.com/gifs/startrekfleetcommand-4v1pOaMg4Z1pOUFK5K', 'https://giphy.com/gifs/animation-happy-K4HqMo1UoOjew', 'https://giphy.com/gifs/ralph-stairs-space-ship-flight-of-the-navigator-jsqUVil8tURoyQ9t1C', 'https://giphy.com/gifs/shocked-surprised-cow-jrht6TXUa0SYlVZFnQ', 'https://giphy.com/gifs/PERQDOTCOM-perq-bot-perqbot-fJ5veFeMaJd3UXGfc3', 'https://giphy.com/gifs/SignatureEntertainmentUK-wesley-snipes-the-recall-final-322VVjQkldB9IvPmbX', 'https://giphy.com/gifs/doctorwho-doctor-who-dr-the-fires-of-pompeii-jsl7zjaaK6IlSdbWeb', 'https://giphy.com/gifs/usnationalarchives-launch-apollo-11-blast-off-l3vR6QzrzOvAD8I7K', 'https://giphy.com/gifs/SignatureEntertainmentUK-wesley-snipes-the-recall-final-22OMufnulfcTGUErzG', 'https://giphy.com/gifs/doctor-who-pretty-time-kxAX99ncvbPk4', 'https://giphy.com/gifs/rocket-launch-spaceship-TRdADd4gJOQteAeY0z', 'https://giphy.com/gifs/doctorwho-doctor-who-dr-the-doctors-wife-YOGLP2Z7eaMRDsPwmD', 'https://giphy.com/gifs/rocket-austin-powers-UtymVt10zlXPCo6FL3', 'https://giphy.com/gifs/AdVentureCapitalistHH-capitalism-adcap-adventure-capitalist-4EJXnSY3oPsQ4xvpfa', 'https://giphy.com/gifs/ralph-scifi-space-ship-xT1Ra1Nu4MaJqHIBgY', 'https://giphy.com/gifs/world-spacex-grasshopper-huvlSnGxC0rT2', 'https://giphy.com/gifs/SignatureEntertainmentUK-wesley-snipes-the-recall-final-7TiefcAB5P4nlV1Ok5', 'https://giphy.com/gifs/SignatureEntertainmentUK-wesley-snipes-the-recall-final-8vLnUghW4aamUxtTy2']
    """
    formatted_query = "+".join(query.split())
    url = f"http://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    gifs = requests.get(url).json()["data"]
    return [gif["url"] for gif in gifs]


if __name__ == "__main__":
    print("\n".join(get_gifs("space ship")))

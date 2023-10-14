import requests
from bs4 import BeautifulSoup


# Function to retrieve the daily horoscope for a zodiac sign and day.
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )

    # Fetch and parse the HTML content of the webpage.
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    # Extract and return the daily horoscope text from the parsed content.
    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "enter your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
    )

    # Prompt the user to select a zodiac sign and day for the horoscope.
    zodiac_sign = int(input("number> ").strip())
    print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
    day = input("enter the day> ")

    # Fetch and display the horoscope text.
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)

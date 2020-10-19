import requests
from bs4 import BeautifulSoup


def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "Zodiac signs:\n",
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
    zodiac_sign = int(input("Select a sign [1-12] > ").strip())
    if zodiac_sign not in range(0, 13):
        print("Invalid choice of Zodian sign!")
    else:
        days_list = {"1": "Yesterday", "2": "Today", "3": "Tomorrow"}
        print("\nDays available:")
        for day in days_list.items():
            print("{}. {}".format(day[0], day[1]))
        inp_day = input("Choose a day [1-3] > ")
        if inp_day not in days_list:
            print("Invalid choice of day!")
        else:
            day = days_list[inp_day].lower()
            horoscope_text = horoscope(zodiac_sign, day)
            print(horoscope_text)

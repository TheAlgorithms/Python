from datetime import date, datetime

import requests
import tabulate

API_URL = (
    "https://www.forbes.com/forbesapi/person/rtb/0/-estWorthPrev/true.json"
    "?fields=personName,gender,source,countryOfCitizenship,"
    "birthDate,finalWorth&limit=10"
)


def real_time_billionaires() -> str:
    """Get top 10 realtime billionaires using forbes API
    Returns:
    Top 10 realtime billionaires date in tabulated string.
    """
    response_json = requests.get(API_URL).json()
    today = date.today()
    final_response = []
    for person in response_json["personList"]["personsLists"]:
        birthdate = datetime.fromtimestamp(person["birthDate"] / 1000).date()
        final_response.append(
            {
                "Name": person["personName"],
                "Source": person["source"],
                "Country": person["countryOfCitizenship"],
                "Gender": person["gender"],
                "Worth": f"{person['finalWorth'] / 1000:.1f} Billion",
                "Age": today.year
                - birthdate.year
                - ((today.month, today.day) < (birthdate.month, birthdate.day)),
            }
        )
    header = tuple(final_response[0].keys())
    rows = [x.values() for x in final_response]
    return tabulate.tabulate(rows, header)


if __name__ == "__main__":
    print(real_time_billionaires())

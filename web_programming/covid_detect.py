"""
[Vikas Ukani]
(Edge Detection Object)
https://github.com/vikas-ukani/
"""


def fetch_covid():
  

  # Importing Packages
  import COVID19Py
  import pandas as pnds

  # Make an instance of Covid

  covid19 = COVID19Py.COVID19()
  # Get all Data Filter by Death Sort

  location = covid19.getLocationByCountryCode("IN")
  # location = covid19.getLocations(rank_by='deaths')

  covidInfo = []
  print(location[0])
  for list in location:
      covidInfo.append({
          "Country": list['country'],
          "Total Population": list['country_population'],
          "Total Death": list['latest']['deaths'],
          "Total Recovered": list['latest']['recovered'],
          "Total Confirmed": list['latest']['confirmed'], })

  pnds.set_option('display.max_rows', None)
  df = pnds.DataFrame(covidInfo).set_index(
      "Country")
  df.to_csv(
      r'covid_death_info.csv', index=True)


if __name__ == "__main__":
    fetch_covid()

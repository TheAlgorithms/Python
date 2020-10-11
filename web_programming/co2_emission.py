"""
Get CO2 emission data from CarbonIntensity API
"""
import requests
import datetime


BASE_URL = 'https://api.carbonintensity.org.uk/intensity'
DATE_FORMAT = '%Y-%m-%d'


# Emission in the last half hour
def fetch_last_half_hour():
  data = requests.get(BASE_URL).json()
  actual_intensity = data['data'][0]['intensity']['actual']
  return actual_intensity


# Emissions in a specific date range
def fetch_from_to(start, end):
  data = requests.get(f'{BASE_URL}/{start}/{end}').json()
  for entry in data['data']:
    print('from ' + entry['from'] + ' to ' + entry['to'] + ': ' + str(entry['intensity']['actual']) + '\n')


if __name__ == '__main__':
  start = datetime.date(2020, 10, 1)
  end = datetime.date(2020, 10, 3)

  fetch_from_to(start, end)

import urllib.request
import json
def currency_converter(currency_from, currency_to, currency_input):
    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair' \
                '%20in%20("'+currency_from+currency_to+'")'
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib.request.urlopen(yql_query_url)
        try:
            json_string = str(yql_response.read())
            json_string = json_string[2:
            json_string = json_string[:-1]
            print(json_string)
            yql_json = json.loads(json_string)
            last_rate = yql_json['query']['results']['rate']['Rate']
            currency_output = currency_input * float(last_rate)
            return currency_output
        except (ValueError, KeyError, TypeError):
            print(yql_query_url)
            return "JSON format error"
    except IOError as e:
        print(str(e))
currency_input = 1
// currency codes : http://en.wikipedia.org/wiki/ISO_4217
currency_from = "USD"
currency_to = "TRY"
rate = currency_converter(currency_from, currency_to, currency_input)
print(rate)

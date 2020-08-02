'''
This programs gives the latest statistics related to the situaion of Covid 19 all around the world.
The data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
'''

def get_stats():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.worldometers.info/coronavirus/"

    page = requests.get(url)
    page = page.text
    soup = BeautifulSoup(page, 'html.parser')

    print("\033[1m" + "COVID-19 Status of the World" + "\033[0m\n")

    x1 = soup.findAll('h1')
    x2 = soup.findAll("div", {"class": "maincounter-number"})

    for i, j in zip(x1, x2):
        print(i.text, j.text)

    x3 = soup.findAll("span", {"class": "panel-title"})
    x4 = soup.findAll("div", {"class": "number-table-main"})

    for i, j in zip(x3, x4):
        _i = i.text.strip()
        _j = j.text.strip()
        print(_i, _j, sep = ":\n", end = "\n\n")

        
def main():
    get_stats()
    
main()

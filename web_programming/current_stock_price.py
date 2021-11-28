import urllib.request
searchStr = input("Enter Search Query \n")
r = urllib.request.urlopen("https://cve.mitre.org/cgi-bin/cvekey.cgi?
keyword="+searchStr)
source_code = r.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(source_code, 'html.parser')

# FIRST OF ALL SEE THAT THE ID "TableWithRules" is associated to the divtag 

table = soup.find('div', {"id" : 'TableWithRules'})
rows=table.find_all("tr")   # here you have to use find_all for finding all rows of table
for tr in rows:
    cols = tr.find_all('td') #here also you have to use find_all for finding all columns of current row
    if cols==[]: # This is a sanity check if columns are empty it will jump to next row
        continue
    p = cols[0].text.strip()
    d = cols[1].text.strip()
    print(p)
    print(d)

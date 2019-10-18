from bs4 import BeautifulSoup
import requests
#from urllib.request import urlopen
import webbrowser
import sys
from fake_useragent import UserAgent  #This is needed for intialazing the User agent of the system otherwise it act like bot
ua = {"UserAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"}
print("Googling.....")
res=requests.get('https://www.google.com/search?q='+ ' '.join(sys.argv[1:]),headers=ua)
#res.raise_for_status()
file=open('project1a.html','wb') #only for knowing the class
for i in res.iter_content(10000):
    file.write(i)
soup= BeautifulSoup(res.text,'lxml')
linkele=soup.select('.eZt8xd')

num=min(5,len(linkele))
print(num)
for i in range(num):
    
    webbrowser.open('http://google.com' + linkele[i].get('href'))

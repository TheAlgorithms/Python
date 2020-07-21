'''
Scraping jobs given job title and location from indeed website
'''

import requests
from bs4 import BeautifulSoup

 
url = "https://www.indeed.co.in/jobs?q=mobile+app+development&l=mumbai"


def fetch_jobs():
    #request the url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')

    # This attribute finds out all the specifics listed in a job
    results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})

    for x in results:
        #Job Title
        job = x.find('a', attrs={'data-tn-element': "jobTitle"})
        #company name
        company = x.find('span', {"class" : "company"})
        print(f"Job is {job.text.strip()} and Company is {company.text.strip()}")
        
        
        
    
if __name__ == "__main__":
  fetch_jobs()
    
    

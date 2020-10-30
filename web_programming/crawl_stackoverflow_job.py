import requests #Navigating with Python
from bs4 import BeautifulSoup #extract Stackoverflow pages

#Get the Stackoverflow URL
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

#Get the last page using requests and soup syntax
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True) #Find and get last pages
    return int(last_page)

def extract_jobs(last_page): 
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            jobId = result["data-jobid"]
            link = {"link": f"https://stackoverflow.com/jobs/{jobId}"}
            jobs.append(link)
    return jobs

#Collect the stackoverflow information and return main.py
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    print(jobs)

if __name__ == "__main__":
    print("Python job finding now...")
    get_jobs()
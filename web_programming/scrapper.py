# Scrapper
# Python selenium scraper to extract out profiles of famous personalities

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4

# f = open("tmp_data.txt", "w")

# create webdriver object
driver = webdriver.Chrome()
  
bse = ""
# name = ['Xi Jinping', 'Vladimir Putin', 'Donald Trump', 'Angela Merkel', 'Jeff Bezos', 'Pope Francis', 'Bill Gates', 'Mohammed bin Salman Al Saud', 'Narendra Modi', 'Larry Page', 'Jerome H. Powell', 'Emmanuel Macron', 'Mark Zuckerberg', 'Theresa May', 'Li Keqiang', 'Warren Buffett', 'Ali Hoseini-Khamenei', 'Mario Draghi', 'Jamie Dimon', 'Carlos Slim Helu', 'Jack Ma', 'Christine Lagarde', 'Doug McMillon', 'Tim Cook', 'Elon Musk', 'Benjamin Netanyahu', 'Ma Huateng', 'Larry Fink', 'Akio Toyoda', 'John L. Flannery', 'Antonio Guterres', 'Mukesh Ambani', 'Jean-Claude Juncker', 'Darren Woods', 'Sergey Brin', 'Kim Jong-un', 'Charles Koch', 'Shinzo Abe', 'Rupert Murdoch', 'Satya Nadella', 'Jim Yong Kim', 'Stephen Schwarzman', 'Khalifa bin Zayed Al-Nahyan', 'Haruhiko Kuroda', 'Abdel Fattah el-Sisi', 'Li Ka-shing', 'Lloyd Blankfein', 'Recep Tayyip Erdogan', 'Bob Iger', 'Michel Temer', 'Michael Bloomberg', 'Wang Jianlin', 'Mary Barra', 'Moon Jae-in', 'Masayoshi Son', 'Bernard Arnault', 'Justin Trudeau', 'Robin Li', 'Michael Dell', 'Hui Ka Yan', 'Lee Hsien Loong', 'Bashar al-Assad', 'John Roberts', 'Enrique Pena Nieto', 'Ken Griffin', 'Aliko Dangote', 'Mike Pence', 'Qamar Javed Bajwa', 'Rodrigo Duterte', 'Abigail Johnson', 'Reed Hastings', 'Robert Mueller', 'Abu Bakr al-Baghdadi', 'Jokowi Widodo', 'Gianni Infantino']
name = ["india","china","usa","japan","australia"]
final_data = ""

for j in range(0,len(name)):
    data = ""
    url = "https://www.google.com.tr/search?q="+bse+" "+name[j]
    # if(j%20==19):
        # time.sleep(300)
    driver.get(url)
    # all_spans = driver.find_elements_by_xpath("//span[@class='PZPZlf hb8SAc']")
    # i=0
    # for span in all_spans:
    #     data = data + "; "+(span.text)
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')

    search = soup.find_all('div', class_="PZPZlf hb8SAc")
    for h in search:
        x = (h.getText())
        final_data = final_data +"\n"+name[j]+"\n"+ x 
        break
print(final_data)
# f.write(final_data)
# f.close()
driver.close()

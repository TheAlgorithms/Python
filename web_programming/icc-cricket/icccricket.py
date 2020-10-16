# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:18:46 2020

@author: KAMESH
"""

"""
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test 
    
"""


import pandas as pd
from selenium import webdriver

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

driver = webdriver.Firefox(executable_path="geckodriver.exe")

# Opening the submission url
driver.get(url)

all_tables   =  driver.find_element_by_tag_name('tbody')

#df = pd.DataFrame(all_tables)

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]

for row in all_tables.find_elements_by_tag_name('tr'):
    
    cells = row.find_elements_by_tag_name('td')
    
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        

from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

df = pd.DataFrame(col_data) 
print(df)

driver.quit()
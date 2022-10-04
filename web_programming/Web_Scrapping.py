import re
import bs4
import requests
import csv
res=requests.get('https://techcrunch.com/')

soup = bs4.BeautifulSoup(res.text,'lxml')


meta_info={}
language=str(soup.html.get('lang'))
if(language=='None'):
    meta_info['language']='Not mentioned'
else:
    meta_info['language']=language
charset=str(soup.meta.get('charset'))
if(charset=='None'):
    meta_info['charset']='Not mentioned'
else:
    meta_info['charset']=charset

try:
    title=soup.find("meta",property="og:title")["content"]
    if(title):
        meta_info['title']=title
except:
    try:
        title=soup.find("meta",attrs={"name":"title"})["content"]
        if(title):
            meta_info['title']=title
    except:
        meta_info['title']='Not mentioned'


try:
    type_=soup.find("meta",property="og:type")["content"]
    if(type_):
        meta_info['type']=type_
except:
    try:
        type_=soup.find("meta",attrs={"name":"type"})["content"]
        if(type_):
            meta_info['type']=type_
    except:
        meta_info['type']='Not mentioned'



try:
    description=soup.find("meta",property="og:description")["content"]
    if(description):
        meta_info['description']=description
except:
    try:
        description=soup.find("meta",attrs={"name":"description"})["content"]
        if(description):
            meta_info['description']=description
    except:
        meta_info['description']='Not mentioned'


try:
    site_name=soup.find("meta",property="og:site_name")["content"]
    if(site_name):
        meta_info['site_name']=site_name
except:
    try:
        site_name=soup.find("meta",attrs={"name":"site_name"})["content"]
        if(site_name):
            meta_info['site_name']=site_name
    except:
        meta_info['site_name']='Not mentioned'


try:
    image=soup.find("meta",property="og:image")["content"]
    if(image):
        meta_info['image']=image
except:
    try:
        image=soup.find("meta",attrs={"name":"image"})["content"]
        if(image):
            meta_info['image']=image
    except:
        meta_info['image']='Not mentioned'



try:
    keywords=soup.find("meta",property="og:keywords")["content"]
    if(keywords):
        meta_info['keywords']=keywords
except:
    try:
        keywords=soup.find("meta",attrs={"name":"keywords"})["content"]
        if(keywords):
            meta_info['keywords']=keywords
    except:
        meta_info['keywords']='Not mentioned'

if(meta_info['title']=='Not mentioned'):
    title=soup.find("title").text
    meta_info['title']=title
print(meta_info)
meta_list=[]
for key,value in meta_info.items():
    l=[]
    l.insert(0,key)
    l.append(value)
    meta_list.append(l)



all_tags=[]
allhrefs=set()
for a in soup.find_all("a",href=True):
    if(a["href"].find("https://")==-1):
        allhrefs.add("https://machinelearningmastery.com/blog/"+a["href"])
    else:
        allhrefs.add(a["href"])
print(allhrefs)
hrefs=list(allhrefs)
hrefs.insert(0,'links')
all_tags.append(hrefs)
all_images=set()

for img in soup.find_all("img",src=True):
    all_images.add(img["src"])
print(all_images)
images=list(all_images)
images.insert(0,'images')
all_tags.append(images)

all_h2=set()
for h2 in soup.find_all("h2"):
    text=h2.text
    text=text.strip('\n')
    text=text.strip('\t')
    all_h2.add(text)
print(all_h2)
h2=list(all_h2)
h2.insert(0,'h2')
all_tags.append(h2)

print(all_tags)

with open("webpage_info.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(meta_list)
    writer.writerows(all_tags)

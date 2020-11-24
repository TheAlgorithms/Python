import requests
from PyInquirer import style_from_dict, Token, prompt
import json
from pySmartDL import SmartDL
import os
from bs4 import BeautifulSoup
import sys

# create style for beautiful print in terminal
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


# create class for terminal color
class bcolors:
    GREEN = '\033[32m'
    HEADER = '\033[95m'
    MAGENTA = '\033[35m'
    OKBLUE = '\033[94m'
    BLUE = '\033[34m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# https://www.instagram.com/p/CDDDA0nAhj3/

# create func that get video and IGTV url
def get_video(link):
    url = f"https://downloadgram.net/wp-json/wppress/video-downloader/video?url={link}"
    req = requests.get(url)
    res = req.content
    json_data = json.loads(res)
    # print(json_data[0]['urls'][0])
    information = [
        json_data[0]['urls'][0]['quality'],
        json_data[0]['urls'][0]['ext'],
        json_data[0]['urls'][0]['size'],
        json_data[0]['urls'][0]['src']
    ]
    print(f"""
                    {bcolors.GREEN}This Is Information About Video{bcolors.ENDC}
         
         {bcolors.MAGENTA}Quality : {information[0]}{bcolors.ENDC}
         {bcolors.OKBLUE}Format  : {information[1]}{bcolors.ENDC}
         {bcolors.OKGREEN}Size    : {information[2]}{bcolors.ENDC} 
         {bcolors.FAIL}SRC     : {information[3]}{bcolors.ENDC}
    """)
    print(f"{bcolors.HEADER}Download Starting{bcolors.BLUE}")
    download(information[3])
    print(bcolors.ENDC)


# create func that download url
def download(link):
    dest = os.path.abspath(os.getcwd())
    downloader = SmartDL(link, dest=dest)
    downloader.start()
    path = downloader.get_dest()


# crate func that get picture url
def get_picture(link):
    res = requests.get(link)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    photo_url = soup.find("meta", property="og:image")
    print(f"""
                        {bcolors.GREEN}This Is Information About Picture{bcolors.ENDC}

             {bcolors.MAGENTA}SRC     : {photo_url["content"]}{bcolors.ENDC}
        """)
    print(f"{bcolors.HEADER}Download Starting{bcolors.BLUE}")
    download(photo_url["content"])
    print(bcolors.ENDC)


if __name__ == '__main__':
    works = [
        'Download Video',
        'Download Picture',
        'Download IGTV',
        'Exit'
    ]
    choice = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Which feature do you want?',
            'choices': works
        }
    ]
    while True:
        answer = prompt(choice, style=style)
        if answer['choice'] == "Download Video":
            link = [
                {
                    'type': 'input',
                    'name': 'link',
                    'message': 'Enter Video Url :'
                }
            ]
            answer = prompt(link, style=style)
            get_video(answer['link'])
        elif answer['choice'] == "Download Picture":
            link = [
                {
                    'type': 'input',
                    'name': 'link',
                    'message': 'Enter Picture Url :'
                }
            ]
            answer = prompt(link, style=style)
            get_picture(answer['link'])
        elif answer['choice'] == "Download IGTV":
            link = [
                {
                    'type': 'input',
                    'name': 'link',
                    'message': 'Enter IGTV Url :'
                }
            ]
            answer = prompt(link, style=style)
            get_video(answer['link'])
        elif answer['choice'] == 'Exit':
            sys.exit(0)

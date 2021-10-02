import pywhatkit
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import time
from selenium.webdriver.chrome.options import Options

num = 1


def assistant_speaks(output):
    global num
    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    # assistant_text("Assistant : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    assistant_text(f"Assistant : {output}")
    playsound.playsound(file, True)
    assistant_text(f"Assistant : {output}")
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        assistant_text("Speak...")
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
        assistant_text("Stop.")  # limit 5 secs

    try:
        text = rObject.recognize_google(audio, language='en-US')
        assistant_text(f"You : {text}")
        return text
    except:

        assistant_speaks("Could not understand your audio, PLease try again !")
        return get_audio()


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Your personal Assistant. 
			I am here to make your life easier. You can command me to perform 
			various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "what can you do" in input:
            speak = "My actions depends on what you ask for. I will try my best to provide you with best results. Thank You"
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Group-9 members which comprise of Ishwam Lakshay Ishika and Mani."
            assistant_speaks(speak)
            return

        elif "geeksforgeeks" in input:  # just
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning. Here is result for geeksforgeeks"""
            assistant_speaks(speak)
            pywhatkit.search('geeksforgeeks')
            return

        elif "what" in input or "who" in input:
            try:
                app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                assistant_speaks(answer)
                return
            except BaseException as e:
                assistant_text(e)

        elif "calculate" in input.lower():
            # write your wolframalpha app_id here #working
            assistant_text("calculate called")
            try:
                app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                client = wolframalpha.Client(app_id)
                indx = input.lower().split().index('calculate')
                query = input.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                assistant_speaks("The answer is " + answer)
                return
            except BaseException as e:
                assistant_text(e)

        elif "open" in input:
            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:
            try:
                app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                assistant_speaks(answer)
                return
            except BaseException as e:
                assistant_text(e)
    except:
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


def search_web(input):
    if 'youtube' in input:
        assistant_speaks("Opening in youtube")
        # indx = input.lower().split().index('youtube')
        # query = input.split()[indx + 1:]
        query = input.replace('youtube', '')
        query = query.replace('play', '')
        query = query.replace('search', '')
        query = query.replace('on', '')
        pywhatkit.playonyt(query)
        return

    elif 'wikipedia' in input:
        assistant_speaks("Here is your search from Wikipedia")
        query = input.replace('wikipedia', '')
        pywhatkit.info(query, lines=5)
        return

    else:
        assistant_speaks("here is your search result")
        query = input.replace("search", '')
        query = query.replace("google", '')
        pywhatkit.search(query)
        time.sleep(15)
        return


# function used to open application
# present inside the system.
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Opening Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Word.lnk')
        return
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Excel.lnk')
        return
    elif "powerpoint" in input:
        assistant_speaks("Opening This PC")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\PowerPoint.lnk')
    elif "whatsapp" in input:
        assistant_speaks("Opening Your Whatsapp")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\WhatsApp.lnk')
    elif "edge" in input:
        assistant_speaks("Opening Microsoft edge")
        os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe')
    elif "epic games" in input:
        assistant_speaks("Opening Epic Games")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Epic Games Launcher.lnk')
    elif "android studio" in input:
        assistant_speaks("Opening Android Studio")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\\Android Studio.lnk')
    elif "sublime text" in input:
        assistant_speaks("Opening Your Sublime Text Editor")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Sublime Text 3.lnk')
    else:
        assistant_speaks("Application not available,Therefore showing results on google")
        query = input.replace("open", '')
        pywhatkit.search(query)
        return


# Driver Code
def startListen():
    if (num == 1):
        assistant_speaks("Hi, I am Your Assistant. What's your name?")
        name = 'human'
        name = get_audio()
        assistant_speaks("Hi, " + name)
    assistant_speaks("What can i do for you?")
    text = get_audio().lower()
    if "thank" in str(text):
        assistant_speaks("It is my pleasure to help you. What can I do for you now")
        text = get_audio().lower()
    if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
        assistant_speaks("Ok bye " + name)
        time.sleep(2)
        window.destroy()

    # calling process text to process the query
    process_text(text)


from tkinter import *
import tkinter as tk

# from Voice_Assistant_Mini_Project import *
window = Tk()


def assistant_text(stri):
    l1.configure(text=stri)
    window.update()


window.geometry('450x200')
# window.minsize(400,400)
# window.maxsize(400,400)
window.title('ASSISTANT')
f1 = Frame(window, height=300, width=250, borderwidth=5, relief=SUNKEN, bg='black')
f1.pack(side=TOP)
# can_wid=Canvas(f1,height=300,width=270,bg='black')
# can_wid.grid(row=1,column=0)
l1 = Label(f1, height=3, text='hey there i am your assistant press listen to perform action', font='16', fg='white',
           bg='black')
l1.pack(side=TOP)
f2 = Frame(window, height=400, width=200, borderwidth=5, relief=SUNKEN, bg='black')
f2.pack(side=BOTTOM, fill=X)
b1 = Button(f2, height=3, text="Listen", bg='grey', command=startListen)
b1.pack(side=BOTTOM, fill=X)
window.mainloop()

__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 0.1'
"""
JARVIS:
- Control windows programs with your voice
"""
# import modules
from datetime import datetime  # datetime module supplies classes for manipulating dates and times
import subprocess  # subprocess module allows you to spawn new processes
import speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..
# pip install pyttsx3                   # need to run only once to install the library
# importing the pyttsx3 library 
import pyttsx3

# initialisation 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('[JARVIS]:' + "Say something")
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)
# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio, language = 'en-IN', show_all = True )
print(Query)
# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":
        print(datetime.now())
    elif Q == "notepad":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "browser":
        subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()
    return
# Call get_app(Query) Func.
get_app(Query)

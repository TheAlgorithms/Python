import pyttsx3
import speech_recognition as sr
import datetime
from gtts import gTTS
from pygame import mixer
import random
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning shampy")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("sAT SRI AKAAL SAAREA NU. ")
    speak("balle balle shaava shaava")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

          print("Say something!")
          r.pause_threshold = 1
          audio = r.listen(source)


    try:
        print("recognising")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)

        print("say that again please")
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
        query =  takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


























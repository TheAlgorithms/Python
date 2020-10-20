
pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
ip = input().strip()
engine.say(ip)
engine.runAndWait()

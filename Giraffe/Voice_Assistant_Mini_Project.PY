import pywhatkit
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import time
from selenium.webdriver.chrome.options import Options

#for selenium initz
"""
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
"""
num = 1
#PATH ="C:\Program Files (x86)\chromedriver.exe"

#driver = webdriver.Chrome(options=chrome_options,executable_path=PATH)
#driver = webdriver.Chrome(PATH)

def assistant_speaks(output):
	global num
	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1

	toSpeak = gTTS(text=output, lang='en', slow=False)
	# saving the audio file given by google text to speech
	file = str(num) + ".mp3"
	toSpeak.save(file)

	# playsound package is used to play the same file.
	print("Assistant : ", output)
	playsound.playsound(file, True)
	os.remove(file)


def get_audio():
	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")
		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit=5)
	print("Stop.")  # limit 5 secs

	try:
		text = rObject.recognize_google(audio, language='en-US')
		print("You : ", text)
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
				print(e)

		elif "calculate" in input.lower():
			# write your wolframalpha app_id here #working
			print("calculate called")
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
				print(e)

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
				print(e)
	except:
		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
		ans = get_audio()
		if 'yes' in str(ans) or 'yeah' in str(ans):
			search_web(input)


def search_web(input):
	#driver = webdriver.Firefox()
	#driver = webdriver.Chrome(PATH)
	#driver.implicitly_wait(1)
	#driver.maximize_window()
	print("search_web called")

	if 'youtube' in input:
		assistant_speaks("Opening in youtube")
		#indx = input.lower().split().index('youtube')
		#query = input.split()[indx + 1:]
		query = input.replace('youtube','')
		query = query.replace('play','')
		query = query.replace('search','')
		query = query.replace('on','')
		pywhatkit.playonyt(query)
		#driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
		#driver.get("https://www.youtube.com/")
		#enter = driver.find_element_by_xpath("""/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input""")
		"""
		enter.send_keys(query)
		enter.submit()
		time.sleep(10)
		"""
		return

	elif 'wikipedia' in input:
		assistant_speaks("Here is your search from Wikipedia")
		#indx = input.lower().split().index('wikipedia')
		#query = input.split()[indx + 1:]
		query = input.replace('wikipedia','')
		pywhatkit.info(query,lines=5)
		#driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:
			#indx = input.lower().split().index('google')
			#query = input.split()[indx + 1:]
		assistant_speaks("here is your search result")
		query = input.replace("search",'')
		query = query.replace("google",'')
		pywhatkit.search(query)
		time.sleep(15)
			#driver.get("https://www.google.com/search?q =" + '+'.join(query))
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
		query = input.replace("open",'')
		pywhatkit.search(query)
		return
# Driver Code
if __name__ == "__main__":
	assistant_speaks("Hi, I am Your Assistant. What's your name?")
	name = 'human'
	name = get_audio()
	assistant_speaks("Hi, " + name)
	while (1):
		assistant_speaks("What can i do for you?")
		text = get_audio().lower()

		if text == 0:
			continue

		if "thank" in str(text):
			assistant_speaks("It is my pleasure to help you. What can I do for you now")
			text = get_audio().lower()
		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
			assistant_speaks("Ok bye " + name)
			break

		# calling process text to process the query
		process_text(text)
		time.sleep(10)
		"""
		assistant_speaks("Should I Continue\n")
		text = get_audio().lower()
		if "exit" in str(text) or "bye" in str(text) or "no" in str(text):
			assistant_speaks("OK bye "+ name)
			break
		"""
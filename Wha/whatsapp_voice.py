from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
import pyttsx3 
import sys
import time 
 ## this below lines are for initializing the recognizer and voices
e = pyttsx3.init()
voices = e.getProperty('voices')
e.setProperty('voice',voices[0].id)
r = sr.Recognizer()

## this below lines configuration for chorome 

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options) 
url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://web.whatsapp.com/") 
# driver = webdriver.Remote(command_executor=url,desired_capabilities={})
# driver.session_id = session_id
wait = WebDriverWait(driver, 60) 

## this function take the input 
def takecommand():
    with sr.Microphone() as source:  ## this make the microphone able to listen voice 
        print("Listening...")
        # e.say("to whome you want to send a message ")
        r.adjust_for_ambient_noise(source) # this line adjust your voice and remove the noise
        r.pause_threshold=0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, key=None, language='en-IN') # this line will recognize your voice and and store it in query
        print("You said: ",query,"\n")
    except Exception as obj:
        e.say("Say that again please")
        e.runAndWait()
        takecommand()
        return "none"
    return query
   
# this function is for  sending a message 
def sendMessage():
    print("in sendmessage")
    e.say("to whom you want to send a message")
    e.runAndWait()
    target=takecommand()    ## this line take the contact name from user
    print(target)
    e.say("you really want to send a message to "+target)
    e.runAndWait()
    flag = takecommand()
    if "yes" in flag:
        target = '"{}"'.format(target)
        # Replace the below string with your own message 
        x_arg = '//span[contains(@title,' + target + ')]' ## this line is for path for contact name
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))  ## this line wait until find the element
        group_title.click()                                                          ## this line click on that contact
        # inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        # input_box = wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath))) 
        inp_xpath='//*[@id="main"]//footer//div[contains(@contenteditable, "true")]'    ## this line is for input box path
        input_box=driver.find_element(By.XPATH,inp_xpath)
        input_box.click()                                                               ## this line take click on the input box so curosr will appear
        e.say("what's your message ")   
        e.runAndWait()
        string = takecommand()                                                          ## this line take the message from user that he want to send
        action = ActionChains(driver)                                                   ## this line set action chain for drive
        action.send_keys(string+Keys.ENTER)                                             ## this line perform the typing effect it'll type the message that 
                                                                                        ## that we want to send and enter key
        action.perform()                                                                ## this line perform the action 
        e.say("message has been sent")
        e.runAndWait()
        print(string)
    if "no" in flag:
        e.say("you want to send message to anyone else or terminate the process ")
        e.runAndWait()
        choice = takecommand()
        if "yes" in choice:
            sendMessage()
        if "terminate" in choice:
            sys.exit()
## main function starting from here
if __name__ == "__main__":
    e.say("hi welcome to voice based whatsapp chat ")
    e.runAndWait()
    sendMessage()               ## call the sendmessage function 
    print("in main \n")
    e.say("want to send more message? say yes or no")
    # e.say("say yes or no")
    e.runAndWait()
    choice = takecommand()      ## this line take the command from user 
    if "yes" in choice:
        e.say("say stop to terminate ")
        e.runAndWait()
        stop = takecommand()
        print("in stop \n")
        while(True):              ## this loop continue untill user says terminate
            sendMessage()
            if("stop" in stop):
                sys.exit()
    if "no" in choice:
        e.say("thanks for your valuable time")
        e.runAndWait()
        sys.exit()

## below code is for if you want to resume the browese or session than you'll go for bellow code
# driver.close()
# driver.session_id = session_id
# def create_driver_session(session_id, executor_url):
#     from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

#     # Save the original function, so we can revert our patch
#     org_command_execute = RemoteWebDriver.execute

#     def new_command_execute(self, command, params=None):
#         if command == "newSession":
#             # Mock the response
#             return {'success': 0, 'value': None, 'sessionId': session_id}
#         else:
#             return org_command_execute(self, command, params)

#     # Patch the function before creating the driver object
#     RemoteWebDriver.execute = new_command_execute

#     new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
#     new_driver.session_id = session_id

#     # Replace the patched function with original function
#     RemoteWebDriver.execute = org_command_execute

#     return new_driver
# driver2 = create_driver_session(session_id,url)

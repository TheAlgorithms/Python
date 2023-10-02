import pyttsx3 as pd

if __name__ == '__main__':
            text_to_speech = pd.init()
            while (True):
                word = input("Enter your command: ")
                if word == 'q':
                    break
                text_to_speech.say(word)
                text_to_speech.runAndWait()

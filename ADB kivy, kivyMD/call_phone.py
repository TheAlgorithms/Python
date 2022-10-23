from ppadb.client import Client as AdbClient
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
client = AdbClient(host="127.0.0.1", port=5037)

class MainScreen(Screen):
    def callback(self,phone):
        print('calling')
        print(client.devices()[0].shell(f'am start -a android.intent.action.CALL -d tel:{phone.text}'))
        print('called')
class MainApp(MDApp):
    
    def build(self):
        return MainScreen()


MainApp().run()
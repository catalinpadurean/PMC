""" Feel good application """

#Creating a login page
#A good practice is to write the features of the GUI in kivi file in kivi language
#Python will be used for logic and kivi for design
#Tip: Shift + Alt + F in json files to format the file for a better reading
import json
import glob
import random

from datetime import datetime
from hoverable import HoverBehavior
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from pathlib import Path
Builder.load_file('design.kv')

#Build some empty classes that will have the same name as the rules(capitals and name) in design.kv file

class LoginScreen(Screen):
    """Screen object inheritance class - FRONTEND"""
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    #Self refers to the instance of the class and this class is inherited from Screen
    #Manager is an atribute of the class "Screen" and sincer LoginScreen is created with inheritance, it will also inherit the manger atribute
    #Current is an atribute of the manager and in this line we take the sign_up_screen an add it to the current screen
    #Long story short: when you press the "Sign Up " button the sing_up() method is called and the current screen is changed from LoginScreen to SignUpScreen
    def forgot_password(self):
            self.manager.current = "forgot_password_screen"
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            if uname in users.keys() and users[uname]['password'] == pword:
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_wrong.text = "Wrong username or password !"
                
class RootWidget(ScreenManager):
    """ScreenManager object inheritance class - FRONTEND"""
    pass

class SignUpScreen(Screen):
    """Screen object inheritance class - FRONTEND"""
    
    def add_user(self, uname, pword):
        with open ("users.json") as file:
            users = json.load(file) #load the file into a dict
            users[uname]= {'username': uname, 'password' : pword, 'created' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            #Load into the dictionary the user and password keeping the following format:
            #Key - username, Value: A dictionary with keys: username, password, created and values: username string passed from GUI, password string passed from GUI and date of creation read from datetime
        
        with open ("users.json", 'w') as file:
            json.dump(users, file)
            #Write into json file the newly added values
        self.manager.current = "sign_up_screen_success"
    
class SignUpScreenSuccess(Screen):
    """Screen object inheritance class - FRONTEND"""
    def login_page(self):
        self.manager.transition.direction = 'right' #set the transition of the screen
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    """Screen object inheritance class - BACKEND""" 
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt") #This will search in the quotes folder and return all text files.
        #TODO:Read about 'glob' module
        available_feelings = [Path(filename).stem for filename in available_feelings ]
        
        if feel in available_feelings: #Check if feel from Frontend does exist in Backend
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file: #Use stringformat to open the "feel" file from quotes folder, if the file exists
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image ):
    """Class that will behave like all 3 of its parents"""
    pass

class ForgotPasswordScreen(Screen):
    def forgot_password(self):
        self.manager.transition.direction = 'left' #set the transition of the screen
        self.manager.current = "forgot_password_screen"
    def recover_password(self, user_name):
        with open ("users.json") as file:
            users = json.load(file) #load the file into a dict
        if user_name in users:
            user_info = users.get(user_name)
            self.ids.recovered_password.text = user_info.get('password')
        else:
            self.ids.recovered_password.text = "User not found"
            


class MainApp(App):
    """App object inheritance class"""
    def build(self):
        return RootWidget() #object not class

#The hierarchy is: App(MainApp)-ScreenManager(RootWidget)-Screen(LoginScreen)
if __name__ == "__main__":
    MainApp().run()
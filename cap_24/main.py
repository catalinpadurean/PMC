""" Feel good application - FRONTEND"""

#Creating a login page
#A good practice is to write the features of the GUI in kivi file in kivi language
#Python will be used for logic and kivi for design
#Tip: Shift + Alt + F in json files to format the file for a better reading
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('design.kv')

#Build some empty classes that will have the same name as the rules(capitals and name) in design.kv file

class LoginScreen(Screen):
    """Screen object inheritance class"""
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    #Self refers to the instance of the class and this class is inherited from Screen
    #Manager is an atribute of the class "Screen" and sincer LoginScreen is created with inheritance, it will also inherit the manger atribute
    #Current is an atribute of the manager and in this line we take the sign_up_screen an add it to the current screen
    #Long story short: when you press the "Sign Up " button the sing_up() method is called and the current screen is changed from LoginScreen to SignUpScreen


class RootWidget(ScreenManager):
    """ScreenManager object inheritance class"""
    pass

class SignUpScreen(Screen):
    """Screen object inheritance class"""
    def add_user(self, uname, pword):
        print(uname, pword)

class MainApp(App):
    """App object inheritance class"""
    def build(self):
        return RootWidget() #object not class


#The hierarchy is: App(MainApp)-ScreenManager(RootWidget)-Screen(LoginScreen)

if __name__ == "__main__":
    MainApp().run()
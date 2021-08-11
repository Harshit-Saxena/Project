from re import MULTILINE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Greeting(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.7, 0.7)   # * Padding on the window...top-bottom and left-right
        self.window.pos_hint = {"center_x": 0.5,"center_y": 0.5}

# TODO: Adding widgets to window

# * Image widget
        self.window.add_widget(Image
        (source="C:\VScode\JavaScript\images\Hello.png")
        )

# * Label widget
        self.greeting = Label(
                              text = "What's your name?",
                              font_size = 22,
                              color = "#00FFCE",
                             )
        self.window.add_widget(self.greeting)

# * User Text inputBox
        self.user = TextInput(
                              multiline=False,
                              padding_y = (20,20),
                              font_size = 22,
                              size_hint = (1,0.5)  # Size of the input box
                              )
        self.window.add_widget(self.user)

# * Button Widget
        self.button = Button(
                              text="Greet",
                              padding_y = (20,20),
                              size_hint = (1,0.5),
                              font_size = 18,
                              italic = True,
                              background_color = "#00FFCE"
                              )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self,instance):
            if self.user.text == "":
                self.greeting.text = "Please provide a name"
            else:
                self.greeting.text = "Hello " + self.user.text + " !"


if __name__ == "__main__":
    Greeting().run()            # * The name of the class is the name that comes here and its the name on top of the app
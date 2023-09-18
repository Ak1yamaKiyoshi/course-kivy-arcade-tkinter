from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        label = Label(text="Hello World")
        return label

app = HelloWorld()
app.run()
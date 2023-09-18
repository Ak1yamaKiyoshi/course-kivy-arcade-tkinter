import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        # Set columns
        self.cols = 1
        # Add widgets 
        self.add_widget(Label(text="Name: "))
        # Add input box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name) 
        self.submit = Button(text="Submit", font_size=55)
        self.add_widget(self.submit)
        # Bind button 
        self.submit.bind(on_press=self.press)
    
    def press(self, instance):
        name = self.name.text 
        # Print to the screen
        self.add_widget(Label(text=f"{name}"))
        self.name.text = ""

class TestInputs(App):
    def build(self):
        return Layout()
    
    
    
app = TestInputs()
app.run()
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self.cols = 1
        # Create second grid layout 
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.top_grid.add_widget(Label(text="Hello"))
        self.top_grid.add_widget(Label(text="World"))
        self.add_widget(self.top_grid)
        self.add_widget(Button(text="idk"))
    
    def press(self, instance):
        pass

class TestInputs(App):
    def build(self):
        return Layout()
    
    
    
app = TestInputs()
app.run()
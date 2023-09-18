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
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
        )
  
        
        self.top_grid.cols = 2
        self.top_grid.add_widget(Label(width=10, text="Hello"))
        self.top_grid.add_widget(Label(text="World"))
        self.add_widget(self.top_grid)
        self.submit = Button(
            text="idk", 
            size_hint_y=None,
            height = 30,
            size_hint_x=None,
            width = 90
        )
        self.add_widget(self.submit)
    
    def press(self, instance):
        pass

class TestInputs(App):
    def build(self):
        return Layout()
    
    
    
app = TestInputs()
app.run()
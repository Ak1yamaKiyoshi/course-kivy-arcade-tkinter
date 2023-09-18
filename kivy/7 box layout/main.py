from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('my.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyLayout()
    
app = MyApp() 
app.run()
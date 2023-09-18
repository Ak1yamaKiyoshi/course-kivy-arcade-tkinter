from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Builder.load_file('whatever.kv')
Builder.load_string("""
<MyGridLayout>

    name:name
    pizza:pizza
    color:color

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2
            Label:
                text: "Name"

            TextInput:
                id: name
                multiline:False

            Label:
                text: "Fav pizze"

            TextInput:
                id: pizza
                multiline:False

            Label:
                text: "fav color"

            TextInput:
                id: color
                multiline:False
        Button: 
            text: "Submit"
            font_size: 32
            on_press: root.press()""")

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    
    def press(self):
        name = self.name.text 
        pizza = self.pizza.text
        color = self.color.text
        print(f"{name} {pizza} {color}")
        self.name.text = ""
        self.pizza.text= ""
        self.color.text= ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()
    
app = AwesomeApp() 
app.run()
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import ObjectProperty

Config.set('graphics', 'resizable', '0') 
Config.set('graphics', 'height', '300')
Config.set('graphics', 'width', '280')

Builder.load_file('calculator.kv')

class CalculatorLayout(Widget):
    expression = ObjectProperty(None)
    
    def add_symbol(self, button):
        if button.text != "Erase" and button.text != "Enter":
            self.expression.text += button.text
        elif button.text == "Erase":
            self.expression.text = self.expression.text[:-1:] 
        elif button.text == "Enter":
            try:
                self.expression.text = str(eval(self.expression.text))
            except: self.expression.text = ""
                
        
class Calculator(App):
    def build(self):
        return CalculatorLayout()
    
Calculator().run()
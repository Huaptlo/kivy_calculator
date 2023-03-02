from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.core.window import Window # jotta fullscreen toimii

class CalcWidget(Widget):
    def __init__(self):
        super().__init__()
    # laskimen toiminnalisuus tänne
    def exit(self):
        exit()

    def numeric_press(self, num):
        if self.ids.calc_input.text=="0":
            self.ids.calc_input.text=str(num)
        else:
            self.ids.calc_input.text+=str(num)
    
    def clear(self):
        self.ids.calc_input.text="0"

class Calculator(App):
    def build(self):
        return CalcWidget()

if __name__=='__main__':
    Calculator().run()

# Name: Calculator
# version: 1.0
# Author: Nori07
# website: https://nori.my.id
# Github : https://github.com/use63


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.config import Config

Config.set('graphics', 'resizable', 'False')
Window.size = (220, 320)
Builder.load_file('main.kv')

class MainLayout(Widget):
    screenText = ''
    screenColor = get_color_from_hex('#000000')

    def tulis(self, num):
        if num in ['+', '-', 'x', '/'] and self.screenText[-1] in ['+', '-', 'x', '/']:
            self.screenTex = self.screenText
        else:
            if num == '+':
                self.screenText += '+'
            elif num == '-':
                self.screenText += '-'
            elif num == 'x':
                self.screenText += 'x'
            elif num == '/':
                self.screenText += '/'
            elif num == 'C':
                self.screenText = self.screenText[:-1]
            elif num == '=' and self.screenText == '':
                self.screenText == ''
            elif num == '=' and self.screenText[-1] in ['+', '-', 'x', '/']:
                self.screenTex = self.screenText
            elif num == '=':
                self.screenText = self.screenText.replace('x', '*')
                result = eval(self.screenText)
                self.screenText = str(result)
            elif self.screenText == '' and str(num) == '0':
                self.screenText = ''
            elif num == 'AC':
                self.screenText = ''
            else:
                self.screenText += str(num)
            self.ids.screen.text = self.screenText


class MainApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MainLayout()


if __name__ == '__main__':
    MainApp().run()
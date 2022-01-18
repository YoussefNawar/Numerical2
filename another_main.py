import os
import json
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

import solutions
from solutions import *

# Set the app size
# Window.size = (500, 700)
# Window.clearcolor = (255/255, 255/255, 255/255, 1)
# Designate Our .kv design file 
Builder.load_file('calc.kv')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(0.5, 0.5))
        self._popup.open()

    def load_list(self, path, filename):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()


class CustomDropDown(BoxLayout):
    state = False
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def printAnswer(self, iterationList, x):
        pass

    def selection(self, text):
        if text == 'Bisection':
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        elif text == 'Regula falsi':
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        elif text == 'Fixed point':
            self.ids.x2.opacity = 0
            self.ids.x2TextArea.opacity = 0
            self.ids.gxInputField.opacity = 1
            self.ids.gx.opacity = 1
        elif text == 'Newton Raphhsen':
            self.ids.x2.opacity = 0
            self.ids.x2TextArea.opacity = 0
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        else:
            self.ids.x2.opacity = 1
            self.ids.x2TextArea.opacity = 1
            self.ids.gxInputField.opacity = 0
            self.ids.gx.opacity = 0
        self.ids.dropdown.select(text)

    def evaluate(self, inputText, selection, x1, x2, gx, maxIteration, precision):
        if maxIteration == '':
            maxIteration = 50
        if precision == '':
            precision = 0.00001
        if selection == 'Bisection':
            answers, x = solutions.bisection(inputText, float(x1), float(x2), float(precision), int(float(maxIteration)))
        elif selection == 'Regula falsi':
            answers, x = solutions.falsi(inputText, float(x1), float(x2), float(precision), int(float(maxIteration)))
        elif selection == 'Fixed point':
            answers, x = solutions.fixed(inputText, gx, float(x1), float(precision), int(float(maxIteration)))
        elif selection == 'Newton Raphhsen':
            answers, x = solutions.Newton(inputText, float(x1), float(precision), int(float(maxIteration)))
        else:
            answers, x = solutions.secant(inputText, float(x1), float(x2), float(precision), int(float(maxIteration)))
        self.ids.answerField.text = str(answers) + str(x)

    def upload(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])):
            f = open(filename[0])
            data = json.load(f)
            print(data)
            fx = data.get('f(x)')
            Selection = data.get("Selection")
            x1 = data.get("x1")
            x2 = data.get("x2")
            gx = data.get("g(x)")
            maxIteration = data.get("MaxIteration")
            precision = data.get("precision")
            self.evaluate(fx, Selection, x1, x2, gx, maxIteration, precision)
        self.dismiss_popup()

    def cancel(self):
        self.dismiss_popup()


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()

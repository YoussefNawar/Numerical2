import os
import json
import re
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
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
        if text == 'Gaussian-elimination':
            self.ids.maxIteration.opacity = 0
            self.ids.maxTextArea.opacity = 0
            self.ids.precision.opacity = 0
            self.ids.precisionTextArea.opacity = 0
        elif text == 'LU decomposition':
            self.ids.maxIteration.opacity = 0
            self.ids.maxTextArea.opacity = 0
            self.ids.precision.opacity = 0
            self.ids.precisionTextArea.opacity = 0
        elif text == 'Gaussian-Jordan':
            self.ids.maxIteration.opacity = 0
            self.ids.maxTextArea.opacity = 0
            self.ids.precision.opacity = 0
            self.ids.precisionTextArea.opacity = 0
        elif text == 'Gauss-Seidel':
            self.ids.maxIteration.opacity = 1
            self.ids.maxTextArea.opacity = 1
            self.ids.precision.opacity = 1
            self.ids.precisionTextArea.opacity = 1
        self.ids.dropdown.select(text)

    def evaluate(self):
        equations = self.ids.equationsTextArea.text
        equationsList = equations.split("\n")
        matrix = []
        for eqn in equationsList:
            equation = re.findall(r'[\d\.\-\+]+', eqn)
            #print(equation)
            equation2 = []
            for i in equation:
                if (i[0] == '='):
                    str = i.split('=')
                    equation2.append(float(str[1]))
                else:
                    equation2.append(float(i))

           # print(equation2)
            matrix.append(equation2)
        # print(equationsList)
        print(matrix)

        selection = self.ids.diffbtn.text
        if selection == 'LU decomposition':
            memo, uu, ll, bb, dd, xx = solutions.LU(matrix)

            self.ids.answerField.text = memo + uu + ll + bb + dd + xx
        elif selection == 'Gaussian-elimination':
            a,x = solutions.gauss_elimination(matrix)
            self.ids.answerField.text = a + x
        else:
            memo, memo_jordan, xx = solutions.jordan(matrix)
            self.ids.answerField.text = memo + memo_jordan + xx

        return

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
            equations = data.get('equations')
            equationsList = equations.split("\n")
            matrix = []
            for eqn in equationsList:
                equation = re.findall(r'[\d\.\-\+]+', eqn)
                equation2 = []
                for i in equation:
                    if (i[0] == '='):
                        str = i.split('=')
                        equation2.append(float(str[1]))
                    else:
                        equation2.append(float(i))

                # print(equation2)
                matrix.append(equation2)
            # print(equationsList)
            print(matrix)
            selection = data.get("Selection")
            if selection == 'LU decomposition':
                memo, uu, ll, bb, dd, xx = solutions.LU(matrix)
                self.ids.answerField.text = memo + uu + ll + bb + dd + xx
            elif selection == 'Gaussian-elimination':
                a, x = solutions.gauss_elimination(matrix)
                self.ids.answerField.text = a + x
            else:
                memo, memo_jordan, xx = solutions.jordan(matrix)
                self.ids.answerField.text = memo + memo_jordan + xx
        self.dismiss_popup()

    def cancel(self):
        self.dismiss_popup()


class CalculatorApp(App):
    def build(self):
        return CustomDropDown()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()

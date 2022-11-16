from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 540)
Config.set('graphics', 'height', 960)
import math
class CalculatorApp(App):
    def unadd(self,instance):
        if instance.text == 'C':
            self.formula = '0'
        elif instance.text == '<-':
            a = self.lbl.text[::-1]
            b = a[1:]
            self.formula = b[::-1]
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def add_num(self, instance):
        if(self.formula == '0'):
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_oper(self, instance):
        if (self.formula == '0'):
            self.formula = ''
        if (str(instance.text).lower() == 'x^2'):
            self.formula += '**2'
        elif (str(instance.text).lower() == 'x^y'):
            self.formula += '**'
        elif (str(instance.text).lower() == '√'):
            self.formula += 'math.sqrt('
        elif (str(instance.text).lower() == 'cos'):
            self.formula += 'math.cos('
        elif (str(instance.text).lower() == 'sin'):
            self.formula += 'math.sin('
        elif (str(instance.text).lower() == 'tg'):
            self.formula += 'math.tan('
        elif (str(instance.text).lower() == 'e'):
            self.formula += '2.718281828459045'
        elif (str(instance.text).lower() == 'pi'):
            self.formula += '3.141592653589'
        elif (str(instance.text).lower() == '%'):
            self.formula += '/100*'
        elif (str(instance.text).lower() == 'y√x'):
            self.formula += '**(1/'
        elif (str(instance.text).lower() == '!'):
            self.formula += 'math.factorial('
        elif (str(instance.text).lower() == 'log10'):
            self.formula += 'math.log10('
        elif (str(instance.text).lower() == 'loge'):
            self.formula += 'math.log('
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = "vertical", padding = 15)
        gl = GridLayout(cols = 5, spacing = 3, size_hint = (1, .7))

        self.lbl = Label(text = "0", font_size = 40, halign = "right", valign = "center", size_hint = (1, .3), text_size = (540-30, 960 *  .3 - 30))
        bl.add_widget( self.lbl)

        gl.add_widget(Button(text='1', on_press = self.add_num))
        gl.add_widget(Button(text='2', on_press = self.add_num))
        gl.add_widget(Button(text='3', on_press = self.add_num))
        gl.add_widget(Button(text='C', on_press = self.unadd))
        gl.add_widget(Button(text='<-', on_press = self.unadd))

        gl.add_widget(Button(text='4', on_press = self.add_num))
        gl.add_widget(Button(text='5', on_press = self.add_num))
        gl.add_widget(Button(text='6', on_press = self.add_num))
        gl.add_widget(Button(text='+',on_press = self.add_oper))
        gl.add_widget(Button(text='-',on_press = self.add_oper))

        gl.add_widget(Button(text='7', on_press = self.add_num))
        gl.add_widget(Button(text='8', on_press = self.add_num))
        gl.add_widget(Button(text='9', on_press = self.add_num))
        gl.add_widget(Button(text='*',on_press = self.add_oper))
        gl.add_widget(Button(text='/',on_press = self.add_oper))

        gl.add_widget(Button(text='=', on_press = self.calc_result))
        gl.add_widget(Button(text='0', on_press = self.add_num))
        gl.add_widget(Button(text='.',on_press = self.add_oper))
        gl.add_widget(Button(text='x^2', on_press=self.add_oper))
        gl.add_widget(Button(text='x^y', on_press=self.add_oper))

        gl.add_widget(Button(text='sin', on_press=self.add_oper))
        gl.add_widget(Button(text='cos', on_press=self.add_oper))
        gl.add_widget(Button(text='tg', on_press=self.add_oper))
        gl.add_widget(Button(text='e', on_press=self.add_oper))
        gl.add_widget(Button(text='√', on_press=self.add_oper))

        gl.add_widget(Button(text='(', on_press=self.add_oper))
        gl.add_widget(Button(text=')', on_press=self.add_oper))
        gl.add_widget(Button(text='pi', on_press=self.add_oper))
        gl.add_widget(Button(text='%', on_press=self.add_oper))
        gl.add_widget(Button(text='y√x', on_press=self.add_oper))

        gl.add_widget(Button(text='!', on_press=self.add_oper))
        gl.add_widget(Button(text='log10', on_press=self.add_oper))
        gl.add_widget(Button(text='loge', on_press=self.add_oper))

        bl.add_widget(gl)
        return bl
if __name__ == "__main__":
    CalculatorApp().run()

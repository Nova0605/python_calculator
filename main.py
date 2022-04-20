from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class RasculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def reset(self, instance):
        self.formula = "0"
        self.update_label()

    def ac(self, instance):
        if (str(instance.text).lower() == "AC"):
            self.formula = "0"
        else:
            self.formula == str(instance.text)
        self.update_label()

    def delete(self, instance):
        if (str(instance.text).lower() == "delete"):
            self.formula = self.formula[:-1] or "0"
        else:
            self.formula == str(instance.text)
        self.update_label()


    def add_number(self, instance):
        if(self.formula == "0"):
            self.formula = ""



        self.formula += str(instance.text)
        self.update_label()

    def operation(self, instance):
        if(str(instance.text).lower() == "x"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()
        self.formula += str(instance.text)
        self.update_label()

    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):
        self.formula = "0"
        gl = GridLayout(cols=4)
        bl = BoxLayout(orientation="vertical")
        self.lbl = Label(text="0", font_size=40, halign="right", text_size=(750 - 50, 500*.4 - 50))
        bl.add_widget(self.lbl)
        gl.add_widget(Button(text="AC", on_press=self.ac))
        gl.add_widget(Button(text="Delete", on_press=self.delete))
        gl.add_widget(Button(text="%", on_press=self.add_number))
        gl.add_widget(Button(text="/", on_press=self.add_number))
        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="*", on_press=self.add_number))
        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="-", on_press=self.add_number))
        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="+", on_press=self.add_number))
        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=".", on_press=self.add_number))
        gl.add_widget(Button(text="=", on_press=self.result))
        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    RasculatorApp().run()

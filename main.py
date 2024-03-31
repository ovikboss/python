import socket
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.textinput import  TextInput
import sqlite3 as sq 
import time




def reg(self):
  try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("26.88.178.51",2000))
    
    name=self.name_input.text
    family=self.family_input.text
    mail=self.mail_input.text
    password=self.pass_input.text
    users=[name,family,mail,password]
    for user in users:
     client.send(user.encode("utf-8"))
     time.sleep(0.01)
  except Exception as _ex:
     self.label.text= f"{_ex}\nЧТо то пошло не так"
     

   # cur.execute("""INSERT INTO USERS (name,family,mail,password)VALUES(?,?,?,?)""",(name,family,mail,password))
  #  con.commit()



Config.set("graphics","resizable",0)
Config.set("graphics","width",400)
Config.set("graphics","height",600)



class Aplication(App):


    def click(self, instance):
        self.label.text = "Cпасибо за регестрацию"
        reg(self)
        self.family_input.text=""
        self.name_input.text=""
        self.mail_input.text= ""
        self.pass_input.text= ""
        

    def build(self):
        self.icon="фото.jpg"
        but_together = BoxLayout()
        grid = GridLayout(cols=1,padding=10)
    
        self.family_input= TextInput(hint_text="Фамилия",multiline=False,height=20)
        self.name_input= TextInput(hint_text="Имя",multiline=False,height=20)
        self.mail_input= TextInput(hint_text="Почта",multiline=False,height=20)
        self.pass_input= TextInput(hint_text="Пароль",multiline=False,height=20)


        Testbut =Button(text="Зарегистроваться",font_size=30,background_color="cyan",on_press=self.click)
        self.label = Label(text="",font_size=30)
      
        but_together.add_widget(Testbut)
        grid.add_widget(self.family_input)
        grid.add_widget(self.name_input)
        grid.add_widget(self.mail_input)
        grid.add_widget(self.pass_input)
        grid.add_widget(but_together)
        grid.add_widget(self.label)
        return grid




if __name__ =="__main__":
    Aplication().run()
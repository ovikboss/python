from tkinter import *
from threading import Thread
import random
import time


with open(r'C:\Users\ovikb\Desktop\проекты\Что то новое\text.txt', 'r', encoding="utf-8") as file:
    text = file.read().splitlines()


class Application:
    button = Button()
    truebutton = Button()
    falsebutton = Button()
    first_team = 0
    second_team = 0
    continuebutton = Button()
    root = ""
    label1 = Label()
    label2 = Label()
    label3 = Label()
    timelabel = Label()


game = Application()


def sleepme():
    for x in range(1, 61):
        time.sleep(1)
        game.timelabel["text"] = x
    game.truebutton.destroy()
    game.falsebutton.destroy()
    game.continuebutton = Button(text="Продолжить игру", command=game.root.destroy)
    game.continuebutton.pack()


def click(num, team):

    if team == 0:
        game.first_team += num
        game.label3["text"] = f"Первая команда {game.first_team}"
        game.label1["text"] = f"{text[random.randrange(len(text))]}"
        
    elif team == 1:
        game.second_team += num
        game.label2["text"] = f"Вторая команда {game.second_team}"
        game.label1["text"] = f"{text[random.randrange(len(text))]}"
        

def startgame(team: int):

    game.truebutton = Button(text="Правильно", command=lambda: click(1, team), background="green")
    game.falsebutton = Button(text="Не угадали", command=lambda: click(-1, team), background="red")
    game.truebutton.pack()
    game.falsebutton.pack()
    game.label1["text"] = f"{text[random.randrange(len(text))]}"
    th = Thread(target=sleepme, args=())
    th.start()
    game.button.destroy()


def game1(team):

    game.root = Tk()
    game.label = Label(text="Alias the best game")
    game.timelabel = Label(text="")
    game.button = Button(text="Начать игру", command=lambda: startgame(team))
    game.root.geometry("400x200")
    game.label1 = Label(text="")
    game.label.pack()
    game.button.pack()
    game.label1.pack()
    game.label3 = Label(text=f"Первая команда {game.first_team}")
    game.label2 = Label(text=f"Вторая команда{game.second_team}")
    game.label3.pack()
    game.label2.pack()
    game.timelabel.pack()
    game.root.mainloop()


while True:
    for team in range(0, 2):
        game1(team)

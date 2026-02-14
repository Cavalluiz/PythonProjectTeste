import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel, mainloop

def final(tl, name, sports, city, playername, drinkname, snacks):

    text = f'''
One day me and my friend {name} decided to play a {sports} game in {city}
We wanted to watch {playername}
We drank {drinkname} and also ate some {snacks}
We really enjoyed! We are looking forward to go again and enjoy
'''
tl.geometry('500x500')
Label(tl, text='Story: ', wraplength=tl.winfo_width()).place(x=160, y=310)
Label(tl, text=text, wraplength=t1.winfo_width()).place(x=0, y=330)

def Story1(win):

NewScreen: Toplevel = Toplevel(win, bg='yellow')
NewScreen.title('A memorable day')
NewScreen.geometry('500x500')

Label(NewScreen, text='Memorable Day').place(x=100, y=0)
Label(NewScreen, text='Name: ').place(x=0, y=35)
Label(NewScreen, text='Enter a game: ').place(x=0, y=70)
Label(NewScreen, text='Enter a city: ').place(x=0, y=110)
Label(NewScreen, text='Enter the name of a player: ').place(x=0, y=150)
Label(NewScreen, text='Enter the name of a drink: ').place(x=0, y=190)
Label(NewScreen, text='Enter the name of a snack: ').place(x=0, y=230)

Name = Entry(NewScreen, width=17)
Name.place(x=250, y=35)
game = Entry(NewScreen, width=17)
game.place(x=250, y=70)
city = Entry(NewScreen, width=17)
city.place(x=250, y=105)
player = Entry(NewScreen, width=17)
player.place(x=250, y=150)
drink = Entry(NewScreen, width=17)
drink.place(x=250, y=190)
snack = Entry(NewScreen, width=17)
snack.place(x=250, y=220)

SubmitButton - Button(NewScreen, text="Submit", background='Blue',
                      font=('Times', 12), command=lambda: final(NewScreen, Name.get(),
                                                                game.get(), city.get(), player.get(), drink.get(),
                                                                snack.get()))
NewScreen, mainloop()

Screen = tk.Tk()
Screen.title('PythonGeeks Mad Libs Generator')
Screen.geometry('400x400')
Screen.config(bg='pink')

Label(Screen, text='PythonGeeks Mad Libs Generator').place(x=100, y=20)
Story1Button = Button(Screen, text='A memorable day', font=('Times New Roman', 13),
                      command=lambda: Story1(Screen), bg='Blue')

Screen.mainloop()

import random
import time
import tkinter.messagebox
from tkinter import*

def draw_ball():
    global x,y,r
    speed = 1000
    canv.delete(ALL)
    r = random.randint(50,150)
    x,y = random.randint(0,1600),random.randint(0,900)
    canv.create_oval(x-r,y-r,x+r,y+r,fill=f"#{random.randint(100000000000,999999999999)}",width=2)
    canv.create_text(100,40,text = f"Очки:{level}",font=("Arial",30))
    canv.create_text(100,80,text=f"Live:{live}",font=("Arial",30))
    canv.create_text(1460,40,text=f"рекорд😉{rekord}",font=("Arial",30))
    canv.after(speed - level,draw_ball)
def clik(event):
    global level,live,rekord
    if(event.x-x)**2 + (event.y-y)**2 <= r**2:
        level +=1
        time.sleep(0.7)
    else:
        live-=1
    if live <= 0:
        if tkinter.messagebox.askyesno("Ты проиграл ", "Хочешь поробоать ещё раз?"):
            live = 3
            rekord = level if level > rekord else rekord
            level = 0
        else:
            svet.destroy()
rekord = 0
live = 3
level = 0
svet = Tk()
svet.geometry("1600x900+0+0")
canv = Canvas(svet,bg = "#006633")
canv.pack(fill= BOTH,expand= 1)
draw_ball()
canv.bind("<Button-1>",clik)

mainloop()

from tkinter import  *
import tkinter.messagebox
def clik(btn):
    if '='  in ex.cget("text"):
        ex.config(text="")
    if btn in "0123456789,":
        vvod.insert(END,btn,)
    elif btn in "+-/*":
        if ex.cget("text") =="":
            ex.config(text=vvod.get()+btn)
            vvod.delete(0,END)
        else:
            ex.config(text = ex.cget("text") + vvod.get())
            if ex.cget("text")[-1] not in "+-*/":
                r =str(eval(ex.cget("text")))
                #print(r)
                ex.config(text = r +btn)
                vvod.delete(0,END)
                #vvod.insert(END,r)
            else:
                ex.config(text = ex.cget("text")[:-1] + btn)
    elif btn in "=":
        try:
            ex.config(text = ex.cget("text")+ vvod.get() + btn )
            vvod.delete(0,END)
            vvod.insert(END,str(eval(ex.cget("text")[:-1])))
        except:
            tkinter.messagebox.showerror("Ошибка")


komar = Tk()
komar.title("Буль")
komar.geometry("+700+300")
ex = Label(komar,text="",font=("Arial",20),justify="right")
ex.grid(row = 0,column=0)
vvod=Entry(komar,font=("Arial",26),justify="right")
ex.grid(row=0,column=0,columnspan=4)
vvod.grid(row=1,column=0,columnspan=4,)
btn=("%","CE","C","delet","1/x","x^2","/2","/","7","8","9","*","4","5","6","-","1","2","3", "+" , "+/-","0",",","=" )
c =0
r = 2
for b in btn:
    cmd = lambda name_btn = b: clik(name_btn)
    Button(komar, text=b,width=12,height=4,command=cmd ).grid(row=r,column=c)
    c +=1
    if c == 4:
        r+=1
        c = 0


mainloop()
from tkinter import *
import webbrowser as wb
soul = Tk()
soul.geometry("310x310")
soul.title("Webaccess")
bg1 = "#D9E000" #F30707    #EF3C3C #5B5952
bg2 = "#B0B19A" #6A6262 #A2A099
soul.configure(background = bg1)

def close():
    exit()
def action():
    wb.open("www.{}.com".format(ent.get()))

lab1 = Label(soul, text = "WEB ACCESSING",justify = LEFT,font = "Helvetica 18 bold italic",bg = bg1)
lab1.place(x = 52,y =20)

lab2 = Label(soul,bg = bg1,text = "ENTER WEBSITE NAME",font = "Times 11 bold")
lab2.place(x = 0,y = 100)

ent = Entry(soul,bg = bg2,width = "20")
ent.place(x = 183,y = 100)

btn = Button(soul,text = "BROWSE",bg = bg2,font = "Times",command = action,height = 2,width = 8)
btn.place(x = 50, y= 160)

btn1 = Button(soul,bg = bg2,text = "QUIT",command = close,height = 2,width = 8,font = "Times")
btn1.place(x = 200, y= 160)

soul.mainloop()

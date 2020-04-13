from tkinter import *
#Initialize the Tkinter.
soul = Tk()
soul.geometry("200x356")
soul.title("Soul_Calci")

#Declaring the empty variable as global.
global val
val = ''

#Fucntion to operate or calculate the values.
def calc(num):
    global val
    val += num
    txt.insert(INSERT,num)
    
#Funtions to  provide the result to  display.
def res(val):
    try:
        d = eval(val)
        txt1.insert(INSERT,d)
    except:
        txt1.insert(INSERT,'Not possible ')

#Functions to Clear the screen.
def clr(m):
    global val
    m = ''
    val = m
    txt.delete(0,END)
    txt1.delete(0,END)

#Buttons Declaration.    
txt = Entry(soul, width = '32',bg = 'white')
txt.grid(row = 0,column = 0)
txt.pack(ipady = 19)

txt1 = Entry(soul, width = '33',bg = '#CCCDB9')
txt1.place(x = 0,y=48)

btn1 = Button(soul,command = lambda:calc('1'),text = '1',width = '5',height = '4')
btn1.place(x=0, y =69)
btn2 = Button(soul,command = lambda:calc('2'),text = '2',width = '5',height = '4')
btn2.place(x = 45,y = 69)
btn3 = Button(soul,command = lambda:calc('3'),text = '3',width = '5',height = '4')
btn3.place(x = 90,y = 69)

btn4 = Button(soul,command = lambda:calc('4'),text = '4',width = '5',height = '4')
btn4.place(x=0, y =140)
btn5 = Button(soul,command = lambda:calc('5'),text = '5',width = '5',height = '4')
btn5.place(x = 45,y = 140)
btn6 = Button(soul,command = lambda:calc('6'),text = '6',width = '5',height = '4')
btn6.place(x = 90,y = 140)


btn7 = Button(soul,command = lambda:calc('7'),text ='7',width = '5',height = '4')
btn7.place(x=0, y =212)
btn8 = Button(soul,command = lambda:calc('8'),text = '8',width = '5',height = '4')
btn8.place(x = 45,y = 212)
btn9 = Button(soul,command = lambda:calc('9'),text = '9',width = '5',height = '4')
btn9.place(x = 90,y = 212)


btn0 = Button(soul,command = lambda:calc('0'),text ='0',width = '5',height = '4')
btn0.place(x=45, y =283)
btnp = Button(soul,command = lambda:calc('.'),text ='.',width = '5',height = '4')
btnp.place(x=0, y =283)
btne = Button(soul,command = lambda:res(val),text ='=',width = '5',height = '4')
btne.place(x=90, y =283)


btnpl = Button(soul,command = lambda:calc('+'),text ='+',width = '8',height = '3')
btnpl.place(x=135, y =71)
btns = Button(soul,command = lambda:calc('-'),text ='-',width = '8',height = '3')
btns.place(x=135, y =128)
btnd = Button(soul,command = lambda:calc('/'),text ='/',width = '8',height = '3')
btnd.place(x=135, y =184)
btnm = Button(soul,command = lambda:calc('*'),text ='*',width = '8',height = '3')
btnm.place(x=135, y =240)
btnc = Button(soul,text ='clr',command = lambda:clr(val),width = '8',height = '3')
btnc.place(x=135, y =298)


#Bring the function again and again.
soul.mainloop()

#Soul Corporation
# For Contact - profsoul23@gmail.com

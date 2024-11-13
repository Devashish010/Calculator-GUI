from tkinter import *
import math
root=Tk()
#root.geometry("400x400")





#def f5():
#    ent.get()
#   ent.set("")

def btn_click(n):
    global data
    data=data + n
    ent.set(data)
def clr():
    global data
    data=""
    ent.set(data)
def eql():
    global data
    val=eval(ent.get())
    data=str(val)
    ent.set(data)
def square():
    global data
    val=eval(ent.get())
    val=val**2
    data=str(val)
    ent.set(data)
def cube():
    global data
    val=eval(ent.get())
    val=val**3
    data=str(val)
    ent.set(data)
def fact():
    global data
    val=eval(ent.get())
    val=math.factorial(val)
    data=str(val)
    ent.set(data)
def erase():
    global data
    val=ent.get()
    c=len(val)
    data=val[0:c-1]
    ent.set(data)
    
        

    


ent=StringVar()
data=""    



Entry(root,textvariable=ent).grid(row=0,columnspan=4)

Button(root,text="7",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('7')).grid(row=1,column=0)
Button(root,text="8",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('8')).grid(row=1,column=1)
Button(root,text="9",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('9')).grid(row=1,column=2)
Button(root,text="+",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('+')).grid(row=1,column=3)
Button(root,text="4",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('4')).grid(row=2,column=0)
Button(root,text="5",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('5')).grid(row=2,column=1)
Button(root,text="6",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('6')).grid(row=2,column=2)
Button(root,text="-",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('-')).grid(row=2,column=3)
Button(root,text="1",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('1')).grid(row=3,column=0)
Button(root,text="2",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('2')).grid(row=3,column=1)
Button(root,text="3",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('3')).grid(row=3,column=2)
Button(root,text="*",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('*')).grid(row=3,column=3)
Button(root,text="c",bg="cyan",fg="black",bd=5,font="now 25 bold",command=clr).grid(row=4,column=0)
Button(root,text="0",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('0')).grid(row=4,column=1)
Button(root,text="=",bg="cyan",fg="black",bd=5,font="now 25 bold",command=eql).grid(row=4,column=2)
Button(root,text="/",bg="cyan",fg="black",bd=5,font="now 25 bold",command=lambda:btn_click('/')).grid(row=4,column=3)
Button(root,text="^2",bg="cyan",fg="black",bd=5,font="now 25 bold",command=square).grid(row=5,column=0)
Button(root,text="^3",bg="cyan",fg="black",bd=5,font="now 25 bold",command=cube).grid(row=5,column=1)
Button(root,text="!",bg="cyan",fg="black",bd=5,font="now 25 bold",command=fact).grid(row=5,column=2)
Button(root,text="<--",bg="cyan",fg="black",bd=5,font="now 25 bold",command=erase).grid(row=5,column=3)



root.mainloop()

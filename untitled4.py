# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 03:57:57 2021

@author: PC
"""
from tkinter import * 
import pandas as pd

History={'answer':[],'phrase':[]}

His = pd.DataFrame(data=History).T

window = Tk()
window.title("Calculator")
q=""
flag=False
#for numbers 
def qq(p):
    global q
    global flag
    q=q+p
    result.config(text=q)
    flag=True
#for =
def oo(p):
    global q
    resvalue=result.cget("text")
    r=eval(resvalue)
    result.config(text=str(r))
    q=str(r)
    if resvalue!=str(r):
        History['answer'].append(r)
        History['phrase'].append(resvalue)
#for delete
def de(p):
    global q
    global flag
    newresult=result.cget("text")
    i=[char for char in newresult]
    del i[-1]
    if set(i[-1]).issubset({"*","/","+","-"}):
        flag=False
    else:
        flag=True
    result.config(text="".join(i))
    q=result.cget("text")

#for * + - / 
def qx(p):
    global q
    global flag
    if flag==True:
        q=q+p
        result.config(text=q)
        flag=False
    elif result.cget("text")=="":
        result.config(text="Eror")
    else:
        newresult=result.cget("text")
        i=[char for char in newresult]
        del i[-1]
        result.config(text="".join(i))
        q=result.cget("text") 
        q=q+p
        result.config(text=q)
        flag=False
            
        
        


window.rowconfigure([0,1,2,3,4],minsize=75, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=75, weight=1)

result=Label(window, text="")
result.grid(row=4, column=0 , columnspan=2)


one = Button(master=window, text="1", command=lambda: qq("1"))
one.grid(row=0, column=0, sticky="nsew")

two = Button(master=window, text="2", command=lambda: qq("2"))
two.grid(row=0, column=1, sticky="nsew")

three = Button(master=window, text="3", command=lambda: qq("3"))
three.grid(row=0, column=2, sticky="nsew")

four = Button(master=window, text="4", command=lambda: qq("4"))
four.grid(row=1, column=0, sticky="nsew")

five = Button(master=window, text="5", command=lambda: qq("5"))
five.grid(row=1, column=1, sticky="nsew")

six = Button(master=window, text="6", command=lambda: qq("6"))
six.grid(row=1, column=2, sticky="nsew")

seven = Button(master=window, text="7", command=lambda: qq("7"))
seven.grid(row=2, column=0, sticky="nsew")

eight = Button(master=window, text="8", command=lambda: qq("8"))
eight.grid(row=2, column=1, sticky="nsew")

nine = Button(master=window, text="9", command=lambda: qq("9"))
nine.grid(row=2, column=2, sticky="nsew")

zero = Button(master=window, text="0", command=lambda: qq("0"))
zero.grid(row=3, column=1, sticky="nsew")

plus = Button(master=window, text="+", command=lambda: qx("+"))
plus.grid(row=0, column=3, sticky="nsew")

minos = Button(master=window, text="-", command=lambda: qx("-"))
minos.grid(row=1, column=3, sticky="nsew")

multi = Button(master=window, text="*", command=lambda: qx("*"))
multi.grid(row=2, column=3, sticky="nsew")

divide = Button(master=window, text="/", command=lambda: qx("/"))
divide.grid(row=3, column=3, sticky="nsew")

equal = Button(master=window, text="=", command=lambda: oo("="))
equal.grid(row=3, column=2, sticky="nsew")

delete = Button(master=window, text="del", command=lambda: de("del"))
delete.grid(row=3, column=0, sticky="nsew")





window.mainloop()
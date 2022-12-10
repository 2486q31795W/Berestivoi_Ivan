from tkinter import *  
from tkinter import messagebox
import tkinter as tk 
import tkinter
import requests
import json


def f():  
    v = txt.get()
    response = requests.get('https://api.github.com/users/vscode')

    f_ = json.loads(response.text)

    y = dict.fromkeys(['company'], f_['company'])
    y2 = dict.fromkeys(['created_at'], f_['created_at'])
    y3 = dict.fromkeys(['email'], f_['email'])
    y4 = dict.fromkeys(['id'], f_['id'])
    y5 = dict.fromkeys(['name'], f_['name'])
    y6 = dict.fromkeys(['url'], f_['url'])
    j = (y,y2,y3,y4,y5,y6)




    

    if v == 'Microsoft':
        with open('C:\\Users\\Galahan\\Desktop\\Практика\\Berestivoi_Ivan\\пр11\\vivod.json', 'w') as file:
            json.dump(j,file)
        
        
    else:
        print('Данное имя не задано')
    


window = Tk()  
window.title("Добро пожаловать")  
window.geometry('500x300')  
lbl = Label(window, text="Привет")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=20, row=0)  
btn = Button(window, text="клик", command=f)  
btn.grid(column=100, row=0)  
window.mainloop()
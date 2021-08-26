from tkinter import *
from tkinter import messagebox
import math

from numpy import square

window=Tk()
window.title("Calculator")
window.geometry("390x395")
window.resizable(0,0)

global expression

def get_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def clear_click():
    global expression
    expression=""
    input_text.set('')

def equals():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=result

def delete():
    global expression
    l=len(expression)
    new_=expression[:l-1]
    expression=new_
    input_text.set(expression)

def cosine():
    global expression
    solved=math.cos(int(expression))
    input_text.set(str(solved))
    expression=str(solved)

def sine():
    global expression
    solved=math.sin(int(expression))
    input_text.set(str(solved))
    expression=str(solved)

def tan():
    global expression
    solved=math.tan(int(expression))
    input_text.set(str(solved))
    expression=str(solved)

def factorial_():
    try:
        global expression
        if int(expression)<0:
            return messagebox.showerror(title='Error',message='Factorial only takes integral values!!' ,options=Message)
            expression=''
        if expression == 0 or expression == 1:
            expression=1
            input_text.set(expression)
        else:
            solved=int(expression) * math.factorial(int(expression)-1)
        input_text.set(solved)
    except ValueError:
        return messagebox.showerror(title='Error',message='Factorial only takes integral values!!' ,icon='warning')


expression=""

input_text=StringVar()
input_frame=Frame(window,width=360,height=70,bd=0,highlightbackground='black')
input_frame.pack(side=TOP)
input_field=Entry(input_frame,font=('arial',22,'bold'),textvariable=input_text,width=50,bg='#eee', bd=0)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

buttons_frame=Frame(window, width=350, height=330, bg='grey')
buttons_frame.pack()

clear = Button(buttons_frame,text='C',fg='black',width=32,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:clear_click()).grid(row=0,column=0, columnspan=3, padx=1,pady=1)
divide = Button(buttons_frame,text='/',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('/')).grid(row=0,column=3, padx=1,pady=1)
deletelastchar = Button(buttons_frame,text='<--',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:delete()).grid(row=0,column=1,columnspan=3,padx=1,pady=1)
cos = Button(buttons_frame,text='cos',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:cosine()).grid(row=0,column=4,padx=1,pady=1)


seven = Button(buttons_frame,text='7',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('7')).grid(row=1,column=0, padx=1,pady=1)
eight = Button(buttons_frame,text='8',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('8')).grid(row=1,column=1, padx=1,pady=1)
nine = Button(buttons_frame,text='9',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('9')).grid(row=1,column=2, padx=1,pady=1)
multiply=Button(buttons_frame,text='*',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('*')).grid(row=1,column=3, padx=1,pady=1)
sine_= Button(buttons_frame,text='sin',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:sine()).grid(row=1,column=4,padx=1,pady=1)


four = Button(buttons_frame,text='4',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('4')).grid(row=2,column=0, padx=1,pady=1)
five = Button(buttons_frame,text='5',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('5')).grid(row=2,column=1, padx=1,pady=1)
six = Button(buttons_frame,text='6',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('6')).grid(row=2,column=2, padx=1,pady=1)
minus = Button(buttons_frame,text='-',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('-')).grid(row=2,column=3, padx=1,pady=1)
tan_ = Button(buttons_frame,text='tan',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:tan()).grid(row=2,column=4,padx=1,pady=1)


one = Button(buttons_frame,text='1',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('1')).grid(row=3,column=0, padx=1,pady=1)
two = Button(buttons_frame,text='2',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('2')).grid(row=3,column=1, padx=1,pady=1)
three = Button(buttons_frame,text='3',fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('3')).grid(row=3,column=2, padx=1,pady=1)
add = Button(buttons_frame,text='+',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('+')).grid(row=3,column=3, padx=1,pady=1)

zero = Button(buttons_frame,text='0',fg='black',width=21,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:get_click('0')).grid(row=4,column=0,columnspan=2, padx=1,pady=1)
point = Button(buttons_frame,text='.',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('.')).grid(row=4,column=3, padx=1,pady=1)
equal_s = Button(buttons_frame,text='=',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:equals()).grid(row=4,column=2, padx=1,pady=1)
raise2pwr = Button(buttons_frame,text='^',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:get_click('**')).grid(row=3,column=4,padx=1,pady=1)
factorial = Button(buttons_frame,text='!',fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:factorial_()).grid(row=4,column=4,padx=1,pady=1)



window.mainloop()













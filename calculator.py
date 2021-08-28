from tkinter import *

root = Tk()
root.title("Calculator")

information = ""
text_input = StringVar(value="0")

#function
def btn(num):
    global information
    information += str(num)
    text_input.set(information)

def sum():
    global information
    calcu = float(eval(information))
    text_input.set(calcu)
    information = ''

def clears():
    global information
    information = ''
    text_input.set('')
    display.insert(0,'0')
    
#process

#display
display = Entry(font=('arial',30,'bold'),fg="black",textvariable=text_input,justify="right")
display.grid(columnspan=4) #4column

#button
btn1 = Button(fg="black",font=('arial',30,'bold'),text='1',padx=30,pady=15,command=lambda:btn(1)).grid(row=1,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),text='2',padx=30,pady=15,command=lambda:btn(2)).grid(row=1,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),text='3',padx=30,pady=15,command=lambda:btn(3)).grid(row=1,column=2)
btnc = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='C',padx=30,pady=15,command=lambda:clears()).grid(row=1,column=3)

btn4 = Button(fg="black",font=('arial',30,'bold'),text='4',padx=30,pady=15,command=lambda:btn(4)).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),text='5',padx=30,pady=15,command=lambda:btn(5)).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),text='6',padx=30,pady=15,command=lambda:btn(6)).grid(row=2,column=2)
btnplus = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='+',padx=30,pady=15,command=lambda:btn('+')).grid(row=2,column=3)

btn7 = Button(fg="black",font=('arial',30,'bold'),text='7',padx=30,pady=15,command=lambda:btn(7)).grid(row=3,column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),text='8',padx=30,pady=15,command=lambda:btn(8)).grid(row=3,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text='9',padx=30,pady=15,command=lambda:btn(9)).grid(row=3,column=2)
btnrub = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='-',padx=30,pady=15,command=lambda:btn('-')).grid(row=3,column=3)

btn0 = Button(fg="black",font=('arial',30,'bold'),text='0',padx=30,pady=15,command=lambda:btn(0)).grid(row=4,column=0)
btndot = Button(fg="black",font=('arial',30,'bold'),text='.',padx=30,pady=15,command=lambda:btn('.')).grid(row=4,column=1)
btndivide = Button(fg="black",font=('arial',30,'bold'),text='÷',padx=30,pady=15,command=lambda:btn('/')).grid(row=4,column=2)
btnmul = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='X',padx=30,pady=15,command=lambda:btn('*')).grid(row=4,column=3)

btnsum = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='=',padx=80,pady=15,command=lambda:sum()).grid(row=5,column=0,columnspan=2)
btnbracket = Button(fg="black",bg="gray",font=('arial',30,'bold'),text='(',padx=30,pady=15,command=lambda:btn('(')).grid(row=5,column=2)
btnbracket2 = Button(fg="black",bg="gray",font=('arial',30,'bold'),text=')',padx=30,pady=15,command=lambda:btn(')')).grid(row=5,column=3)
root.mainloop()
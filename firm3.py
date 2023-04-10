from tkinter import *
import pyfirmata
import time
root=Tk()
port='COM15'
board=pyfirmata.Arduino(port)
time.sleep(2.0)
root.configure(bg='blue')
root.geometry('250x250')
root.title('IGATUS CONTROL')
def off():
     board.digital[9].write(0)
     lb=Label(root,text='FAN IS OFF',font='Verdana 50 italic',bg='red',fg='white').place(x=20,y=150)
def level1():
      board.digital[9].write(0.2)
#     #lb=Label(root,text='LIGHT IS OFF',font='Verdana 10 italic').place(x=100,y=220)
def level2():
    board.digital[9].write(0.4)
#     #lb=Label(root,text='LIGHT IS OFF',font='Verdana 10 italic').place(x=100,y=220)
def level3():
    board.digital[9].write(0.6)
#     # lb=Label(root,text='LIGHT IS OFF',font='Verdana 10 italic').place(x=100,y=220)
def level4():
    board.digital[9].write(0.9)
#     # lb=Label(root,text='LIGHT IS OFF',font='Verdana 10 italic').place(x=100,y=220)
def on():
     board.digital[9].write(1)
     lb=Label(root,text='FAN IS ON',font='Verdana 50 italic',bg='green',fg='white').place(x=20,y=150)
label=Label(root,text='GATUS FAN SWITCH',font='Helvetica 20 bold')
label.place(x=20,y=20)
button=Button(root,text='ON',font='Helvetica 20 bold',command=on).place(x=20,y=70)
# button=Button(root,text='LEVEL1',font='Helvetica 20 bold',command=level1).place(x=70,y=70)
# button=Button(root,text='LEVEL2',font='Helvetica 20 bold',command=level2).place(x=200,y=70)
# button=Button(root,text='LEVEL3',font='Helvetica 20 bold',command=level3).place(x=330,y=70)
# button=Button(root,text='LEVEL4',font='Helvetica 20 bold',command=level4).place(x=460,y=70)
button=Button(root,text='OFF',font='Helvetica 20 bold',command=off).place(x=100,y=70)
if __name__=='__main__':
    root.mainloop()
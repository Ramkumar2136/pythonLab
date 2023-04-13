from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from tkinter.filedialog import askopenfilename

def start():
    global image1,path
    global panel
    path=filedialog.askopenfilename()
    image1=cv2.imread(path)
    image1=cv2.resize(image1,(200,100))
    image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
    image=Image.fromarray(image1)
    image=ImageTk.PhotoImage(image)
    if panel is None:
        panel=Label(image=image)
        panel.image=image
        panel.pack(side='left',padx=30,pady=60)
    else:
        panel.configure(image=image)
        panel.image=image

def gray_image():
    global panelB
    gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    gray=Image.fromarray(gray)
    gray=ImageTk.PhotoImage(gray)
    if panelB is None:
        panelB = Label(image=gray)
        panelB.image=gray
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=gray)
        panelB.image=gray

def edge_image():
    global panelB
    gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,50,100)
    edge=Image.fromarray(edge)
    edge=ImageTk.PhotoImage(edge)
    if panel is None:
        panelB=Label(image=edge)
        panelB.image=edge
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=edge)
        panelB.image=edge

def negative_image():
    global panelB
    image=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
    negative=cv2.bitwise_not(image)
    negative=Image.fromarray(negative)
    negative=ImageTk.PhotoImage(negative)
    if panelB is None:
        panelB=Label(image=negative)
        panelB.image=negative
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=negative)
        panelB.image=negative

root=Tk()
root.geometry('600x400')
fm=Frame(root,width=300,height=200)
fm.pack(side=BOTTOM,expand=NO,fill=NONE)
panelB=None
panel=None
btn=Button(root,text="select an image",command=start,activebackground='red',fg='blue')
btn.pack(side='top')
btn2=Button(fm,text='Grey',command=gray_image,activebackground='red',height=2,width=10,fg='gray')
btn2.pack(side=LEFT,padx='10',pady='20')
btn3=Button(fm,text="EDGE",command=edge_image,activebackground='red',height=2,width=10,fg='green')
btn3.pack(side=LEFT,padx='10',pady='20')
btn4=Button(fm,text='NEGATIVE',command=negative_image,activebackground='red',height=2,width=10,fg='purple')
btn4.pack(side=LEFT,padx='10',pady='20')
root.mainloop()
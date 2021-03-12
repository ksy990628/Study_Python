#계산기

import tkinter
import math     #math 모듈 import

window = tkinter.Tk()   #창 띄우기

frame = tkinter.Frame(window, borderwidth=2, relief=(tkinter.GROOVE))
frame.pack()

ep = tkinter.StringVar()
entry = tkinter.Entry(frame, textvariable=ep)
entry.pack(side="left")

label = tkinter.Label(window,text=" ")
label.pack()


def onClick():
    label.config(text = str(eval(ep.get())))

button = tkinter.Button(frame,text="계산", command=onClick)
button.pack(side="right")

window.mainloop()

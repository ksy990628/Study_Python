import tkinter
window = tkinter.Tk()   #윈도우 창 띄우기

label = tkinter.Label(window,text="Hello, Python",bg="black",fg="yellow",font=('Times',48,'bold'))
label.pack()

window.mainloop()


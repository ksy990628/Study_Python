#keyboard 입력 받은 후 출력해주는 프로그램

import tkinter
window = tkinter.Tk()   #윈도우 창 만들기


#keyboard 입력이 들어왔을 때 처리할 이벤트
def keyPressed(event):
    var.set("Key: %s" %event.char)  #입력된 key 출력

#label1 설정
label1 = tkinter.Label(window,text = "Press any key")
label1.pack()


#label2에서 쓰일 가변변수 설정
var = tkinter.StringVar()
var.set(' ')

#label2 설정
label2 = tkinter.Label(window, textvariable = var)
label2.pack()

#이벤트 바인딩(이벤트와 이벤트 핸들러 연결)
window.bind("<Key>",keyPressed)

window.mainloop()




#방법2
'''
#keyboard 입력 받은 후 출력해주는 프로그램

import tkinter
window = tkinter.Tk()   #윈도우 창 만들기

#label1 설정
label1 = tkinter.Label(window,text = "Press any key")
label1.pack()

#label2 설정
label2 = tkinter.Label(window,text = ' ')
label2.pack()

#keyboard 입력이 들어왔을 때 처리할 이벤트
def keyPressed(event):
    label2.config(text= 'key: %s'%event.char)
    
#이벤트 바인딩(이벤트와 이벤트 핸들러 연결)
window.bind("<Key>",keyPressed)

window.mainloop()
'''

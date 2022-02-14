import tkinter
from tkinter import font 

win = tkinter.Tk() #창 생성
win.title("First GUI") #창 타이틀
win.geometry("500x500") # 창 크기 
win.option_add("*Font", "맑은고딕 25") #전체 폰트 
win.configure(bg="tomato") #배경 색깔 
win.resizable(True, True) #사이즈 변경 

win.mainloop()     #창 실행 


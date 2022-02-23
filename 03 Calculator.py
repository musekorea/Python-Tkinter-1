import tkinter

# Window 
win = tkinter.Tk() #창 생성
win.title("First GUI") #창 타이틀
win.geometry("268x275+1360+100") # 창 크기 
win.option_add("*Font", "맑은고딕 15") #전체 폰트 
win.configure(bg="cornflowerblue") #배경 색깔 
win.resizable(True, True) #사이즈 변경 

# Entry
input = tkinter.Entry(win,justify="right", width=21)
input.insert(0,"0")
input.config(relief="sunken",borderwidth=15, background="pink", foreground="blue",insertbackground="red")
input.grid(row=0, column=0, columnspan=4)

# Button 1열
btn_c = tkinter.Button(win, text="C",  height=2, width=5)
btn_c.config(overrelief="groove", bg="red")
btn_c.grid(row=1, column=0, padx=1, pady=1)
btn_d = tkinter.Button(win, text="/",  height=2, width=5)
btn_d.grid(row=1, column=1, padx=1, pady=1)
btn_m = tkinter.Button(win, text="*",  height=2, width=5)
btn_m.grid(row=1, column=2, padx=1, pady=1)
btn_s = tkinter.Button(win, text="-",  height=2, width=5)
btn_s.grid(row=1, column=3, padx=1, pady=1)

# Button 2열 
btn_7 = tkinter.Button(win, text="7", height=2, width=5)
btn_7.grid(row=2, column=0)
btn_8 = tkinter.Button(win, text="8", height=2, width=5)
btn_8.grid(row=2, column=1)
btn_9 = tkinter.Button(win, text="9", height=2, width=5)
btn_9.grid(row=2, column=2)
btn_x = tkinter.Button(win, text="+", height=2, width=5)
btn_x.grid(row=2, column=3)

# Button 3열 
btn_4 = tkinter.Button(win, text="4", height=2, width=5)
btn_4.grid(row=3, column=0)
btn_5 = tkinter.Button(win, text="5",  height=2, width=5)
btn_5.grid(row=3, column=1)
btn_6 = tkinter.Button(win, text="6",  height=2, width=5)
btn_6.grid(row=3, column=2)
btn_e = tkinter.Button(win, text="=",  height=2, width=5)
btn_e.config(bg="blue", fg="white")
btn_e.grid(row=3, column=3 )

# Button 3열 
btn_1 = tkinter.Button(win, text="1", height=2, width=5)
btn_1.grid(row=4, column=0)
btn_2 = tkinter.Button(win, text="2", height=2, width=5)
btn_2.grid(row=4, column=1)
btn_3 = tkinter.Button(win, text="3", height=2, width=5)
btn_3.grid(row=4, column=2)
btn_0 = tkinter.Button(win, text="0", height=2, width=5)
btn_0.grid(row=4, column=3)





#창 실행 
win.mainloop()    


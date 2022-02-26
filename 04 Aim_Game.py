from cgi import test
from functools import partial
import tkinter
import random

win = tkinter.Tk()
win.title("Aim Game")
win.geometry("550x150+1130+200")
win.option_add("*Font", "20")
win.resizable(False,False)

# 배경이미지
bg_img = tkinter.PhotoImage(file="./galaxy.png")
bg_img = bg_img.subsample(4,7)
bg_label = tkinter.Label(win, image=bg_img)
bg_label.config(bd=0)
bg_label.place(x=0,y=0)

# 시작화면 
target_number=10 

label = tkinter.Label(win)
label.config(text="표적 개수")
label.grid(row=0, column=0, padx=20, pady=25)

input = tkinter.Entry(win)
input.insert(0,"10")
input.grid(row=0,  column=1)

btn = tkinter.Button(win)
btn.config(text="시작", width=20, bg="red", fg="white", relief="groove",overrelief="sunken")
btn.grid(row=1, column=1, columnspan=2)

def handle_clear(e):
  input.delete(0,tkinter.END)
input.bind("<Button-1>", handle_clear)



# 게임 실행 로직

counter = 1

def handle_btn_click():
  btn.destroy()
  global counter 
  global target_number
  counter+=1
  print(counter)
  if target_number<counter:
    print("끝")
    return
  else:
    make_btn()
    print("새로운 버튼 생성")
  

def make_btn():
  global btn
  btn = tkinter.Button(win)
  btn.config(text=counter, bg="red", fg="white", padx=5, pady=5)
  btn.place(x=random.randrange(10,500),y=random.randrange(10,500))
  btn.config(command= handle_btn_click)

def handle_start_click():
  global target_number
  try:
    target_number =  int( input.get())
    for widget in win.grid_slaves():
      widget.destroy()
    #게임 화면으로 전환
    win.geometry("550x550")
    win.config(background="cornflowerBlue")
    bg_label.destroy()
    #게임실행 로직 함수
    make_btn()

  except ValueError:
    input.delete(0, tkinter.END)
    input.insert(0,"숫자를 입력해주세요")
  

btn.config(command=handle_start_click)



tkinter.mainloop()
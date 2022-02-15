import tkinter
import requests
from  bs4 import BeautifulSoup

# Window 
win = tkinter.Tk() #창 생성
win.title("First GUI") #창 타이틀
win.geometry("500x500") # 창 크기 
win.option_add("*Font", "맑은고딕 15") #전체 폰트 
win.configure(bg="tomato") #배경 색깔 
win.resizable(True, True) #사이즈 변경 

# Label1
label1 = tkinter.Label(win, width=30, height=2)
label1.config(text="회차를 입력하세요 예) 2022014")
label1.pack()

# Entry 
input = tkinter.Entry(win, width=30)
input.pack()
lotto_list = []

def btn_click():
  input_value = input.get()
  req = requests.get(f"https://www.cjcp.com.cn/kaijiang/ssq/index.php?qh={input_value}")
  soup = BeautifulSoup(req.text, "html.parser")
  lotto_red = soup.find_all("span", {"class","qiu_red"})
  lotto_blue = soup.find("span", {"class","qiu_blue"}).get_text()
  global lotto_list
  for lotto in lotto_red:
    lotto_num = lotto.get_text()
    lotto_list.append(lotto_num)
  lotto_list.append(lotto_blue)
  input.delete(0,tkinter.END)
  numbers(input_value,lotto_list)


# Button
btn = tkinter.Button(win, text="로또 당첨 번호 확인")
btn.pack()
btn.config(command=btn_click)

# Label2
def numbers(input_value,lotto_list):
  lotto_str = ""
  for index, lotto in enumerate(lotto_list) :
    print(index, lotto)
    if index==6:
      break
    lotto_str = lotto_str + " " + lotto
  result = f"{input_value}회차\n 로또번호 : {lotto_str}\n 보너스번호 : {lotto_list[-1]}"
  label = tkinter.Label(win, text=result, width=50, height=3)
  label.config()
  label.pack()


#창 실행 
win.mainloop()    


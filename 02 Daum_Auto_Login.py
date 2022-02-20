import tkinter
from selenium import webdriver

win = tkinter.Tk()
win.title("Daum Auto Log-in")
win.geometry("400x300")
win.option_add("*Font", "'-apple-system 20")

#LOGO
logo = tkinter.Label(win)
logo.pack()
logo_img = tkinter.PhotoImage(file="./daum.png")
logo_img = logo_img.subsample(20)
logo.config(image=logo_img)

#ID LABEL
label1 = tkinter.Label(win)
label1.pack()
label1.config(text="ID")

#ID ENTRY
def handle_clear(e):
  browser_login_input.clear()
  browser_pwd_input.clear()
  if id_input.get()== "temp@temp.com":
    id_input.delete(0,tkinter.END)

id_input = tkinter.Entry(win)
id_input.pack()
id_input.insert(0,"temp@temp.com")
id_input.bind("<Button-1>",handle_clear)

#PASSWORD LABEL
label2 = tkinter.Label(win)
label2.pack()
label2.config(text="Password")

#PASSWORD ENTRY
pw_input = tkinter.Entry(win)
pw_input.pack()
pw_input.config(show="*")
pw_input.bind("<Button-1>",handle_clear)

#LOGIN
def handle_login_btn_click():
  message.config(text="")
  id = id_input.get()
  pw = pw_input.get()
  if id=="" or pw=="":
    message.config(text="[메시지] 빈칸을 입력해주세요")
  try:
    browser_login_input.send_keys(id)
    browser.implicitly_wait(5)
    browser_pwd_input.send_keys(pw)
    browser.implicitly_wait(5)
    browser_login_button.click()
    browser.implicitly_wait(5)
    message.config(text="[메시지] 로그인에 성공했습니다")
    
  except:
    print("Error 발생")

btn = tkinter.Button(win)
btn.pack()
btn.config(text="Login")
btn.config(command=handle_login_btn_click)

#LOGIN MESSAGE
message = tkinter.Label(win)
message.pack()

#SELINIUM
browser = webdriver.Chrome("./chromedriver.exe")
url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net"
browser.get(url)
browser_login_input = browser.find_element_by_xpath('//*[@id="id_email_2"]')
browser_pwd_input = browser.find_element_by_xpath('//*[@id="id_password_3"]')
browser_login_button = browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]')



win.mainloop()
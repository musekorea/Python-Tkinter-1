from email.mime import image
import tkinter

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
id_input = tkinter.Entry(win)
id_input.pack()


#PASSWORD LABEL
label2 = tkinter.Label(win)
label2.pack()
label2.config(text="Password")

#PASSWORD ENTRY
pw_input = tkinter.Entry(win)
pw_input.pack()

#LOGIN
btn = tkinter.Button(win)
btn.pack()
btn.config(text="Login")



win.mainloop()
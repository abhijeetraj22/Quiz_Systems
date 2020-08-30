from tkinter import messagebox
import testfunct
from testfunct import *


def user_reg():
    mainwin.destroy()
    os.system('python user_regis.py')


def forget_password():
    mainwin.destroy()
    os.system('python pass_recov.py')


def entered3(event):
    forget_pass_btn.config(bg="grey",fg="white")


def left3(event):
    forget_pass_btn.config(bg="light grey",fg="black")


def entered1(event):
    loginbtn.config(bg="blue",fg="white")


def left1(event):
    loginbtn.config(bg="light blue",fg="black")


def entered2(event):
    regbtn.config(bg="red", fg="white")


def left2(event):
    regbtn.config(bg="pink", fg="black")


def login_detail():
    global mainwin
    login_type = entry5.get()
    email_enter = emailtxt.get()
    passwd_enter = passtxt.get()
    tempa=checkEmail(email_enter)
    if(len(login_type) == 0):
        messagebox.showwarning("Warning", "Select Login Type")
    elif (len(passwd_enter) == 0):
        messagebox.showwarning("Warning", "password Empty")
    else:
        temp = login_check(login_type, email_enter)
        if (temp is not None):
            #tk.messagebox.showinfo('Info',temp[0])
            if (temp[0] == passwd_enter):
                f = open("QuizDetail/quizsystem.txt", "w+")
                d = email_enter
                f.write(d)
                f.seek(0, 0)
                f.close()
                ft = open("QuizDetail/quiztype.txt", "w+")
                dt = login_type
                ft.write(dt)
                ft.seek(0, 0)
                ft.close()
                if (login_type == "Admin"):
                    mainwin.destroy()
                    os.system('python admin_panel.py')
                elif (login_type == "User"):
                    mainwin.destroy()
                    os.system('python user_Panel.py')
                elif (login_type == "Root"):
                    f = open("QuizDetail/quizsystem.txt", "w+")
                    d = temp[1]
                    f.write(d)
                    f.seek(0, 0)
                    f.close()
                    mainwin.destroy()
                    os.system('python root_panel.py')
            else:
                messagebox.showwarning("Warning", "Password Incorrect")
        else:
            tk.messagebox.showinfo('Info', 'Login Fail or Email Not Found')


mainwin = Tk()
i, j, k, l = 450, 590, 400, 30
mainwin.geometry(f"{i}x{j}+{k}+{l}")
mainwin.resizable(0, 0)
mainwin['bg']="white"
mainwin.title("Quiz System")
mainwin.tk.call('wm','iconphoto',mainwin, ImageTk.PhotoImage(file='venv/Image/quiz_icon.png'))
labelframe1= LabelFrame(mainwin, text="Authentication",font= ("Tahoma",20),fg="#ff40d0",bd=2,bg="white").pack(fill="both", expand="yes",padx=40,pady=25)

imageX = Image.open("venv/Image/quiz.png")
width, height = imageX.size
sXimg = 70
imageX = imageX.resize((round(100 / height * width)+sXimg, round(80)+sXimg))
imgX = ImageTk.PhotoImage(imageX)
imglvl=Label(mainwin, image=imgX,bd=0).place(x=80, y=60)

imageY = Image.open("venv/Image/systemImg.png")
width, height = imageY.size
x,y=60,60
imageY = imageY.resize((round(x / height * width), round(y)))
imgY = ImageTk.PhotoImage(imageY)
imglvl2=Label(mainwin, image=imgY,bd=0,bg="white").place(x=210, y=200)


mailId = Image.open("venv/Image/email_img.png")
width, height = mailId.size
x,y=30,30
mailId = mailId.resize((round(x / height * width), round(y)))
mailIdimg = ImageTk.PhotoImage(mailId)
mailIdimglvl=Label(mainwin, image=mailIdimg,bg="white").place(x=320, y=335)

passKeys = Image.open("venv/Image/passKey.png")
width, height = passKeys.size
x,y=25,25
passKeys = passKeys.resize((round(x / height * width), round(y)))
passKeysimg = ImageTk.PhotoImage(passKeys)
passKeyslvl=Label(mainwin, image=passKeysimg,bg="white").place(x=320, y=399)

accTypelvl = Label(mainwin, text="Account Type",font=("Tahoma",12,"bold"),bg="white")
accTypelvl.place(x=180, y=255)
fontEx= ("Tahoma",12,"bold")
justifyEx="center"
entry5=ttk.Combobox(mainwin,values=["Root","Admin","User"],width=21,font= fontEx,justify=justifyEx )
mainwin.option_add('*TCombobox*Listbox.font',fontEx)
mainwin.option_add('*TCombobox*Listbox.justify',justifyEx)
entry5.place(x=110, y=280)

emailIdlvl = Label(mainwin, text="Email ID",font=("Tahoma",12,"bold"),bg="white")
emailIdlvl.place(x=190, y=315)

emailtxt= StringVar()
emailentry = ttk.Entry(mainwin, textvariable=emailtxt,width=22,font=("Tahoma",12))
emailentry.place(x=110, y=340)

passlvl = Label(mainwin, text="Password",font=("Tahoma",12,"bold"),bg="white")
passlvl.place(x=190, y=375)

passtxt= StringVar()
paswdentry = ttk.Entry(mainwin, textvariable=passtxt,width=22,font=("Tahoma",12),show="*")
paswdentry.place(x=110, y=400)

loginbtn = Button(mainwin, text="Login",command= login_detail, font=("Tahoma",12),width=25,bd=0)
loginbtn.configure(bg="light blue")
loginbtn.place(x=110, y=440)

forget_pass_btn = Button(mainwin, text="Forget Password",command= forget_password ,font=("Tahoma",12),width=25,bd=0)
forget_pass_btn.configure(bg="light grey")
forget_pass_btn.place(x=110, y=520)

regbtn = Button(mainwin, text="User Registration",command= user_reg ,font=("Tahoma",12),width=25,bd=0)
regbtn.configure(bg="pink")
regbtn.place(x=110, y=480)

loginbtn.bind("<Enter>",entered1)
loginbtn.bind("<Leave>",left1)

forget_pass_btn.bind("<Enter>",entered3)
forget_pass_btn.bind("<Leave>",left3)

regbtn.bind("<Enter>",entered2)
regbtn.bind("<Leave>",left2)

mainwin.mainloop()
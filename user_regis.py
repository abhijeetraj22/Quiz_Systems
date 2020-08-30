from testfunct import *


def entered1(event):
    clear_btn.config(bg="green",fg="white")


def left1(event):
    clear_btn.config(bg="light green",fg="black")


def entered2(event):
    submit_btn.config(bg="red",fg="white")


def left2(event):
    submit_btn.config(bg="pink",fg="black")


def entered3(event):
    back_btn.config(bg="blue",fg="white")


def left3(event):
    back_btn.config(bg="light blue",fg="black")


def clearUser():
    urNametxt.set("")
    urEmailtxt.set("")
    urMobtxt.set("")
    urcountrytxt.set("")
    urstatetxt.set("")
    urcitytxt.set("")
    ques_enter_txt.set("")
    ans_enter_txt.set("")
    urPasswdtxt.set("")
    urRepasswdtxt.set("")


def backMain():
    userRegWin.destroy()
    os.system('python main.py')


def addUser():
    global wb
    urName=urNametxt.get()
    urGen=v.get()
    urEmail=urEmailtxt.get()
    urMob=urMobtxt.get()
    urcountry=urcountrytxt.get()
    urstate=urstatetxt.get()
    urcity=urcitytxt.get()
    ur_sec_ques = ques_enter_txt.get()
    ur_sec_ans = ans_enter_txt.get()
    urPasswd=urPasswdtxt.get()
    urRepasswd=urRepasswdtxt.get()

    if (len(urcountry) == 0):
        messagebox.showinfo("Error", "Please Enter a Country Name")
    elif (len(urstate) == 0):
        messagebox.showinfo("Error", "Please Enter a State Name")
    elif (len(urcity) == 0):
        messagebox.showinfo("Error", "Please Enter a City Name")
    elif len(ur_sec_ques) == 0:
        messagebox.showinfo("Error","Please Choose a question")
    elif len(ur_sec_ans) == 0:
        messagebox.showinfo("Error", "Please Enter a answer")
    else:
        ur_name = checkName(urName)
        if (ur_name != 0): #or ur_email == 0 or ur_mobile == 0 or ur_password == 0):
            ur_email = checkEmail(urEmail)
            if (ur_email != 0):
                ur_mobile = checkMob(urMob)
                if (ur_mobile != 0):
                    ur_password = checkPassword(urPasswd, urRepasswd)
                    if (ur_password != 0):
                        #print(ur_name, urGen, ur_email, ur_mobile, urcity, urstate, urcountry,ur_sec_ques, ur_sec_ans, ur_password)
                        temp = insert_into_user_data(ur_name, urGen, ur_email, ur_mobile, urcity, urstate, urcountry,ur_sec_ques, ur_sec_ans, urPasswd)
                        if (temp):
                            messagebox.showinfo("Database", "Record Added to Database")
                            clearUser()


userRegWin = Tk()
i, j, k, l = 540, 680, 400, 10
userRegWin.geometry(f"{i}x{j}+{k}+{l}")
userRegWin.resizable(0, 0)
userRegWin.tk.call('wm','iconphoto',userRegWin, ImageTk.PhotoImage(file='venv/Image/quiz_icon.png'))
userRegWin['bg']="white"
userRegWin.title("Registration")
imageX = Image.open("venv/Image/quiz.png")
width, height = imageX.size
x,y=80,80
imageX = imageX.resize((round(x / height * width), round(y)))
imgX = ImageTk.PhotoImage(imageX)
imageY = Image.open("venv/Image/systemImg.png")
width, height = imageY.size
x,y=35,35
imageY = imageY.resize((round(x / height * width), round(y)))
imgY = ImageTk.PhotoImage(imageY)

imglvl=Label(userRegWin,bd=0,bg="white").pack(padx=10,pady=20)
imglvl=Label(userRegWin, image=imgX,bd=0).place(x=5,y=1)
imglvl2=Label(userRegWin, image=imgY,bd=0,bg="white").place(x=120, y=40)

labelframe2= LabelFrame(userRegWin, text="New User",font= ("Tahoma",20),fg="#ff40d0",bd=2,bg="white").pack(fill="both", expand="yes",padx=40,pady=35)
fontlvlExp = ("Tahoma",11,"bold")
fontExp = ("Tahoma",12)
v = StringVar()
v.set("M")
values = {"Male": "M",
          "Female": "F"
          }

urNametxt = StringVar()
urEmailtxt=StringVar()
urMobtxt=StringVar()
ques_enter_txt = StringVar()
ans_enter_txt = StringVar()
urPasswdtxt=StringVar()
urRepasswdtxt=StringVar()

urcountrytxt=StringVar()
urstatetxt=StringVar()
urcitytxt=StringVar()
urNamelvl = Label(userRegWin, text="Full Name",font = fontlvlExp,bg="white")
urNamelvl.place(x=80, y=150)
entry1 = ttk.Entry(userRegWin, textvariable=urNametxt,font = fontExp,width=22)
entry1.place(x=240, y=150)
urGenlvl = Label(userRegWin, text="Gender",font = fontlvlExp,bg="white")
urGenlvl.place(x=80, y=190)
rx,ry=240,190
for (text, value) in values.items():
    Radiobutton(userRegWin, text=text, variable=v,
                value=value,font = fontlvlExp,bg="white").place(x=rx, y=ry)
    rx+=70

urEmaillvl = Label(userRegWin, text="Email",font = fontlvlExp,bg="white")
urEmaillvl.place(x=80, y=230)
entry3= ttk.Entry(userRegWin, textvariable=urEmailtxt,font = fontExp,width=22)
entry3.place(x=240, y=230)
urMoblvl=Label(userRegWin, text="Mobile",font = fontlvlExp,bg="white")
urMoblvl.place(x=80, y=270)
entry4= ttk.Entry(userRegWin, textvariable=urMobtxt,font = fontExp,width=22)
entry4.place(x=240, y=270)

urCountrylvl = Label(userRegWin, text="Country",font = fontlvlExp,bg="white")
urCountrylvl.place(x=80, y=310)
entry5= ttk.Entry(userRegWin, textvariable=urcountrytxt,font = fontExp,width=22)
entry5.place(x=240, y=310)
urStatelvl = Label(userRegWin, text="State",font = fontlvlExp,bg="white")
urStatelvl.place(x=80, y=350)
entry6= ttk.Entry(userRegWin, textvariable=urstatetxt,font = fontExp,width=22)
entry6.place(x=240, y=350)
urCitylvl = Label(userRegWin, text="City",font = fontlvlExp,bg="white")
urCitylvl.place(x=80, y=390)
entry7= ttk.Entry(userRegWin, textvariable=urcitytxt,font = fontExp,width=22)
entry7.place(x=240, y=390)

secu_ques = ["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"]

ques_lvl = Label(userRegWin, text="Security Question",bg="white",font=fontlvlExp)
ques_lvl.place(x=80, y=430)
ans_lvl = Label(userRegWin, text="Security Answer",bg="white",font=fontlvlExp)
ans_lvl.place(x=80, y=470)

ques_enter = ttk.Combobox(userRegWin, textvariable = ques_enter_txt,font=fontExp,values= secu_ques, width=20)
ques_enter.place(x=240, y=430)
ans_enter = ttk.Entry(userRegWin, show="*", textvariable=ans_enter_txt, font=fontExp, width=22)
ans_enter.place(x=240, y=470)

urPasswdlvl = Label(userRegWin, text="Password",font = fontlvlExp,bg="white")
urPasswdlvl.place(x=80, y=510)
entry8= ttk.Entry(userRegWin, show="*", textvariable=urPasswdtxt,font = fontExp,width=22)
entry8.place(x=240, y=510)
urRepasswdlvl = Label(userRegWin, text="Re-Password",font = fontlvlExp,bg="white")
urRepasswdlvl.place(x=80, y=550)
entry9= ttk.Entry(userRegWin, show="*", textvariable=urRepasswdtxt,font = fontExp,width=22)
entry9.place(x=240, y=550)


#######################################Button Icon Image######################################################
photo1 = PhotoImage(file="venv/Image/back_img.png")
backimg = photo1.subsample(1,1)
photo2 = PhotoImage(file="venv/Image/User_img.png")
submitimg = photo2.subsample(1,1)
photo3 = PhotoImage(file="venv/Image/clear_img.png")
clearimg = photo3.subsample(1,1)

back_btn = Button(userRegWin, text="Back", image=backimg, compound = LEFT, font = fontExp, width=90, command=backMain, bd=0)
back_btn.configure(bg="light blue")
back_btn.place(x=110, y=600)
back_btn.bind("<Enter>",entered3)
back_btn.bind("<Leave>",left3)

submit_btn = Button(userRegWin, text="Submit", image= submitimg, compound = LEFT,font = fontExp, width=90, command=addUser, bd=0)
submit_btn.configure(bg="pink")
submit_btn.place(x=210, y=600)
submit_btn.bind("<Enter>",entered2)
submit_btn.bind("<Leave>",left2)

clear_btn = Button(userRegWin, text="Clear", image= clearimg, compound = LEFT, font = fontExp, width=90, command=clearUser, bd=0)
clear_btn.configure(bg="light green")
clear_btn.place(x=310, y=600)
clear_btn.bind("<Enter>",entered1)
clear_btn.bind("<Leave>",left1)

userRegWin.mainloop()

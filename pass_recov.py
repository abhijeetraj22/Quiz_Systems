from testfunct import *


def back_main():
    pass_rec_win.destroy()
    os.system('python main.py')


def entered1(event):
    verify_btn.config(bg="red",fg="white")


def left1(event):
    verify_btn.config(bg="pink",fg="black")

sub_btn = ""


def entered2(event):
    sub_btn.config(bg="blue", fg="white")


def left2(event):
    sub_btn.config(bg="light blue", fg="black")


def entered3(event):
    back_btn.config(bg="blue", fg="white")


def left3(event):
    back_btn.config(bg="light blue", fg="black")


def ins():
    flag=0
    if (len(pass_enter_txt.get())) < 8:
        flag = -1
        messagebox.showinfo("Error", "password must be Minimum 8")
    elif (len(pass_enter_txt.get())) > 7 or len(re_pass_enter_txt.get()) > 7:
        print("hello")
        while True:
            if not re.search("[a-z]", pass_enter_txt.get()):
                flag = -1
                break
            elif not re.search("[A-Z]", pass_enter_txt.get()):
                flag = -1
                break
            elif not re.search("[0-9]", pass_enter_txt.get()):
                flag = -1
                break
            elif not re.search("[_@$]", pass_enter_txt.get()):
                flag = -1
                break
            elif re.search("\s", pass_enter_txt.get()):
                flag = -1
                break
            else:
                flag = 0
                break
        if flag == -1:
            messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
        elif pass_enter_txt.get() != re_pass_enter_txt.get():
            flag = -1
            messagebox.showinfo("Error","New and retype password are not some")

    if(flag == 0):
        try:
            conn = sqlite3.connect('Quiz_System.db')
            myCursor = conn.cursor()
            if(acc_enter_txt.get() == "Admin"):
                qry = f"Update admin_detail set admin_password ='{pass_enter_txt.get()}' where admin_email = '{email_enter_txt.get()}'"
            elif (acc_enter_txt.get() == "User"):
                qry = f"Update user_detail set user_password ='{pass_enter_txt.get()}' where user_email = '{email_enter_txt.get()}'"
            myCursor.execute(qry)
            conn.commit()
            myCursor.close()
            conn.close()
            messagebox.showinfo("Confirm","Password Updated Successfuly")
            pass_rec_win.destroy()
            os.system('python main.py')
        except Error:
            messagebox.showerror("Error","Something Goes Wrong")
def set_password():
    global sub_btn
    acc_lvl.destroy()
    acc_enter.destroy()
    email_lvl.destroy()
    email_enter.destroy()
    ans_lvl.destroy()
    ans_enter.destroy()
    ques_lvl.destroy()
    ques_enter.destroy()
    verify_btn.destroy()
    back_btn.destroy()
    Label(pass_rec_win, text="New Password", bg="white", font=fontlvlExp).place(x=75, y=210)
    ttk.Entry(pass_rec_win, show="*", textvariable=pass_enter_txt, font=fontExp, width=22).place(x=230, y=210)
    Label(pass_rec_win, text="Retype Password", bg="white", font=fontlvlExp).place(x=75, y=270)
    ttk.Entry(pass_rec_win, show="*", textvariable=re_pass_enter_txt, font=fontExp, width=22).place(x=230, y=270)
    sub_btn = Button(pass_rec_win, text="Submit", width=10, bd=0, bg="light blue", font=fontExp, command=ins)
    sub_btn.place(x=230, y=324)
    sub_btn.bind("<Enter>", entered2)
    sub_btn.bind("<Leave>", left2)


def check():
    qry = None
    if len(acc_enter_txt.get()) == 0:
        messagebox.showinfo("Error","Please Select Account Type")
    elif checkEmail(email_enter_txt.get()) == 0:
        pass
    elif len(ques_enter_txt.get()) == 0:
        messagebox.showinfo("Error","Please Choose a question")
    elif len(ans_enter_txt.get()) == 0:
        messagebox.showinfo("Error", "Please Enter a answer")
    else:
        try:
            conn = sqlite3.connect('Quiz_System.db')
            myCursor = conn.cursor()
            #print(acc_enter_txt.get(),acc_enter.get())
            if(acc_enter_txt.get() == "Admin"):
                qry= f"Select admin_sec_ques,admin_sec_ans from admin_detail where admin_email = '{email_enter_txt.get()}'"
            elif (acc_enter_txt.get() == "User"):
                qry= f"Select user_sec_ques,user_sec_ans from user_detail where user_email = '{email_enter_txt.get()}'"
            myCursor.execute(qry)
            pc = myCursor.fetchone()
            if not pc:
                messagebox.showinfo("Error", "Something Wrong in the Details")
            elif str(pc[0]) == ques_enter_txt.get() and str(pc[1]) == ans_enter_txt.get():
                set_password()
            else:
                messagebox.showinfo("info", "Question or Answer Wrong")
        except Error:
            messagebox.showerror("Error","Something Goes Wrong")

pass_rec_win = Tk()
        #self.iconbitmap(r'libico.ico')
i, j, k, l = 520, 520, 400, 30
pass_rec_win.geometry(f"{i}x{j}+{k}+{l}")
pass_rec_win['bg']="white"
pass_rec_win.resizable(0, 0)
pass_rec_win.title("Forget Password")
        #creating variables
acc_enter_txt = StringVar()
email_enter_txt = StringVar()
ques_enter_txt = StringVar()
ans_enter_txt = StringVar()
pass_enter_txt = StringVar()
re_pass_enter_txt = StringVar()
        #label and input box

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

imglvl=Label(pass_rec_win,bd=0,bg="white").pack(padx=10,pady=20)
imglvl=Label(pass_rec_win, image=imgX,bd=0).place(x=5,y=1)
imglvl2=Label(pass_rec_win, image=imgY,bd=0,bg="white").place(x=120, y=40)

pass_rec_labelframe= LabelFrame(pass_rec_win, text="Password Recovery",font= ("Tahoma",20),fg="green",bd=2,bg="white").pack(fill="both", expand="yes",padx=40,pady=35)
fontlvlExp = ("Tahoma",11,"bold")
fontExp = ("Tahoma",12)

secu_ques = ["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"]

acc_lvl = Label(pass_rec_win, text="Account Type",bg="white", font=fontlvlExp)
acc_lvl.place(x=75, y=160)
email_lvl = Label(pass_rec_win, text="Email",bg="white", font=fontlvlExp)
email_lvl.place(x=75, y=210)
ques_lvl = Label(pass_rec_win, text="Security Question",bg="white",font=fontlvlExp)
ques_lvl.place(x=75, y=260)
ans_lvl = Label(pass_rec_win, text="Security Answer",bg="white",font=fontlvlExp)
ans_lvl.place(x=75, y= 310)
justifyEx="center"
fontEx= ("Tahoma",11,"bold")
acc_enter = ttk.Combobox(pass_rec_win, textvariable = acc_enter_txt,font=fontEx,values=["Admin", "User"], width=18,justify=justifyEx)
acc_enter.place(x=230, y=160)
acc_enter.option_add('*TCombobox*Listbox.font',fontEx)
acc_enter.option_add('*TCombobox*Listbox.justify',justifyEx)
email_enter = ttk.Entry(pass_rec_win, textvariable=email_enter_txt,font=fontExp, width=22)
email_enter.place(x=230, y=210)
ques_enter = ttk.Combobox(pass_rec_win, textvariable = ques_enter_txt,font=fontExp,values= secu_ques, width=20)
ques_enter.place(x=230, y=260)
ans_enter = ttk.Entry(pass_rec_win, show = "*", textvariable=ans_enter_txt, font=fontExp, width=22)
ans_enter.place(x=230, y=310)
back_btn = Button(pass_rec_win, text="Back", compound = LEFT, font = fontExp, width=10, command=back_main, bd=0)
back_btn.configure(bg="light blue")
back_btn.place(x=135, y=380)
back_btn.bind("<Enter>",entered3)
back_btn.bind("<Leave>",left3)
verify_btn = Button(pass_rec_win, text='Verify', font=fontExp,bd=0,bg="pink", width=10,command = check)
verify_btn.place(x=295, y=380)
verify_btn.bind("<Enter>",entered1)
verify_btn.bind("<Leave>",left1)
pass_rec_win.mainloop()
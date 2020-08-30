from testfunct import *


f = open("QuizDetail/quizsystem.txt", "r")
email_field = f.read()
#print(email_field)
f.close()
f = open("QuizDetail/quiztype.txt", "r")
login_type = f.read()
#print(login_type)
f.close()


def entered3(event):
    back_btn.config(bg="blue",fg="white")


def left3(event):
    back_btn.config(bg="light blue",fg="black")


def entered1(event):
    verify_btn.config(bg="red",fg="white")


def left1(event):
    verify_btn.config(bg="pink",fg="black")

sub_btn = ""


def entered2(event):
    sub_btn.config(bg="blue", fg="white")


def left2(event):
    sub_btn.config(bg="light blue", fg="black")


def back_main():
    if(login_type == "Admin"):
        pass_rec_win.destroy()
        os.system('python admin_panel.py')
    elif(login_type == "User"):
        pass_rec_win.destroy()
        os.system('python user_Panel.py')

        #verifying input
def insert_recovery(login_type_field,email_field):
    try:
        conn = sqlite3.connect('Quiz_System.db')
        # conn = pymysql.connect(host="localhost",
        #                                   user="root",
        #                                   passwd="1234",
        #                                   port=3306,
        #                                   database="db1")

        myCursor = conn.cursor()
        if login_type_field == "Admin":
            qry = f"Update admin_detail set admin_sec_ques = '{ques_enter_txt.get()}', admin_sec_ans = '{ans_enter_txt.get()}' where admin_email='{email_field}'"

        elif login_type_field == "User":
            qry = f"Update user_detail set user_sec_ques = '{ques_enter_txt.get()}', user_sec_ans = '{ans_enter_txt.get()}' where user_email='{email_field}'"

        myCursor.execute(qry)
        conn.commit()
        myCursor.close()
        conn.close()
        messagebox.showinfo("Confirm","Recovery Update Successfuly")

    except Error:
        messagebox.showerror("Error","Something Goes Wrong")


def check():
    if len(cur_pass_enter_txt.get()) == 0:
        messagebox.showinfo("Error","Please Enter Current Password")
    elif len(ques_enter_txt.get()) == 0:
        messagebox.showinfo("Error","Please Choose a question")
    elif len(ans_enter_txt.get()) == 0:
        messagebox.showinfo("Error", "Please Enter a answer")
    else:
        try:
            conn = sqlite3.connect('Quiz_System.db')
            # conn = pymysql.connect(host="localhost",
            #                       user="root",
            #                       passwd="1234",
            #                       port=3306,
            #                       database="db1")
            mycursor = conn.cursor()
            if (login_type == "Admin"):
                mycursor.execute(f"Select admin_password from admin_detail where admin_email = '{email_field}'")
            elif (login_type == "User"):
                mycursor.execute(f"Select user_password from user_detail where user_email = '{email_field}'")
            pc = mycursor.fetchone()
            #print(pc[0])
            # if not pc:
            #     messagebox.showinfo("Error", "Password Wrong ")
            if str(pc[0]) == cur_pass_enter_txt.get():
                if(login_type == "Admin"):
                    insert_recovery(login_type,email_field)
                    back_main()
                elif (login_type == "User"):
                    insert_recovery(login_type, email_field)
                    back_main()
            else:
                messagebox.showinfo("Error", "Password Wrong ")
        except Error:
            messagebox.showerror("Error","Something Goes Wrong22")

pass_rec_win = Tk()
#self.iconbitmap(r'quiz.ico')
i, j, k, l = 520, 420, 400, 130
pass_rec_win.geometry(f"{i}x{j}+{k}+{l}")
pass_rec_win.tk.call('wm','iconphoto',pass_rec_win, ImageTk.PhotoImage(file='venv/Image/quiz_icon.png'))
pass_rec_win['bg']="white"
pass_rec_win.resizable(0, 0)
pass_rec_win.title("Recovery")

 #creating variables

cur_pass_enter_txt = StringVar()
ques_enter_txt = StringVar()
ans_enter_txt = StringVar()
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

pass_rec_labelframe= LabelFrame(pass_rec_win, text="Recovery Setting",font= ("Tahoma",20),fg="red",bd=2,bg="white").pack(fill="both", expand="yes",padx=40,pady=35)
fontlvlExp = ("Tahoma",11,"bold")
fontExp = ("Tahoma",12)

secu_ques = ["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"]

ques_lvl = Label(pass_rec_win, text="Security Question",bg="white",font=fontlvlExp)
ques_lvl.place(x=75, y=160)
ans_lvl = Label(pass_rec_win, text="Security Answer",bg="white",font=fontlvlExp)
ans_lvl.place(x=75, y=210)
cur_pass_lvl = Label(pass_rec_win, text="Current Password",bg="white", font=fontlvlExp)
cur_pass_lvl .place(x=75, y=260)


ques_enter = ttk.Combobox(pass_rec_win, textvariable = ques_enter_txt,font=fontExp,values= secu_ques, width=20)
ques_enter.place(x=230, y=160)
ans_enter = ttk.Entry(pass_rec_win, show="*", textvariable=ans_enter_txt, font=fontExp, width=22)
ans_enter.place(x=230, y=210)
cur_pass_enter = ttk.Entry(pass_rec_win,show="*", textvariable=cur_pass_enter_txt,font=fontExp, width=22)
cur_pass_enter.place(x=230, y=260)
verify_btn = Button(pass_rec_win, text='Enter', font=fontExp,bd=0,bg="pink", width=10,command = check)
verify_btn.place(x=295, y=310)
verify_btn.bind("<Enter>",entered1)
verify_btn.bind("<Leave>",left1)
back_btn = Button(pass_rec_win, text="Back", compound = LEFT, font = fontExp, width=10, command=back_main, bd=0)
back_btn.configure(bg="light blue")
back_btn.place(x=135, y=310)
back_btn.bind("<Enter>",entered3)
back_btn.bind("<Leave>",left3)

pass_rec_win.mainloop()
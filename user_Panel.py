from tkinter import messagebox
import testfunct
from testfunct import *


qzname = None
logoutbtn = None
userWin = None
listTreeuser = None
newpasstxt = None
oldpasstxt = None
entrynewpass = None
entryoldpass = None

fontlvlExp = ("Tahoma", 10, "bold")
fontExp = ("Tahoma", 11)


f = open("QuizDetail/quizsystem.txt", "r")
user_email = f.read()
ft = open("QuizDetail/quiztype.txt", "r")
acc_type = ft.read()
#print(acc_type)
#print(user_email)
Data = fetch_name(acc_type,user_email)
user_name = Data[0]
user_id = Data[1]
ft.close()
f.close()


def backHome_user():
    global userWin
    userWin.destroy()
    os.system('python main.py')


def entered3(event):
    logoutbtn.config(bg="blue", fg="white")


def left3(event):
    logoutbtn.config(bg="light blue", fg="black")


def clear_password():
    oldpasstxt.set("")
    newpasstxt.set("")

def recov_set_win():
    userWin.destroy()
    os.system('python set_recov.py')


def num_press(name):
    f = open("QuizDetail/quizname.txt", "w+")
    d = name
    f.write(d)
    f.seek(0, 0)
    f.close()
    userWin.destroy()
    os.system('python Quizgame.py')


def user_result():
    u_name = user_name
    temp = ur_result(u_name)
    if (len(temp) > 0):
        listTreeuser.delete(*listTreeuser.get_children())
        for row in temp:
            listTreeuser.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))


def user_on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Home":
        load_quiz_name()
        user_result()
        #print("Home tab selected")

    # if tab_text == "Quiz Score":
    #     print("Quiz Score tab selected")


def change_password():
    oldpass = entryoldpass.get()
    newpass = entrynewpass.get()
    #print(user_email,oldpass,newpass)
    temp = change_password_func(acc_type, user_email,oldpass,newpass)
    if(temp):
        tk.messagebox.showinfo('Info', 'Change Password Successfully')
        clear_password()
    else:
        tk.messagebox.showinfo('Info', 'Old Password Wrong')


def userwin():
    global userWin, logoutbtn
    global newpasstxt, oldpasstxt, entrynewpass, entryoldpass, listTreeuser

    userWin = Tk()
    i, j, k, l = 520, 560, 400, 30
    userWin.geometry(f"{i}x{j}+{k}+{l}")
    userWin.resizable(0, 0)
    userWin.tk.call('wm','iconphoto',userWin, ImageTk.PhotoImage(file='venv/Image/quiz_icon.png'))
    userWin['bg']="white"
    userWin.title("Quiz System")

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

    imageMy = Image.open("venv/Image/my_img.jpg")
    width, height = imageMy.size
    x,y=120,120
    imageMy = imageMy.resize((round(x / height * width), round(y)))
    imgMy = ImageTk.PhotoImage(imageMy)
    imglogout = PhotoImage(file="venv/Image/logout2.png")
    logoutimg = imglogout.subsample(1, 1)

    spacelvl_u = Label(userWin,bd=0,bg="white")
    spacelvl_u.pack(padx=10,pady=45)
    imglvl_u=Label(userWin, image=imgX,bd=0)
    imglvl_u.place(x=5,y=1)
    imglvl2_u=Label(userWin, image=imgY,bd=0,bg="white")
    imglvl2_u.place(x=120, y=40)
    userNamelvl = Label(userWin, text=user_name, font=("Tahoma", 12), bg="white")
    userNamelvl.place(x=1, y=80)
    logoutbtn = Button(userWin, text="Logout", image=logoutimg, compound=RIGHT,command=backHome_user, bd=0, bg="light blue",
                       font=("Tahoma", 11), width=70)
    logoutbtn.place(x=440, y=75)
    logoutbtn.bind("<Enter>", entered3)
    logoutbtn.bind("<Leave>", left3)

    tab_parent = ttk.Notebook(userWin)
    s=ttk.Style()
    s.configure('TNotebook.Tab', font=fontlvlExp)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)

    tab_parent.bind("<<NotebookTabChanged>>", user_on_tab_selected)

    tab_parent.add(tab1, text="Home")
    tab_parent.add(tab2, text="Quiz Score")
    tab_parent.add(tab3, text="Change Pin")
    tab_parent.add(tab4, text="About")

    # === WIDGETS FOR TAB ONE
    newpasstxt = StringVar()
    oldpasstxt = StringVar()

    imglvl=Label(tab1,bd=0).grid(row=0, column=0,pady=30)
    sp=load_quiz_name()
    qzname=[]
    if (sp):
        for e in testfunct.rows:
            qzname.append(e[1])
        i = 0
        #print(i,len(qzname),qzname,testfunct.num_of_rows)
        bttn = []
        for j in range(1, len(qzname)+1):
            bttn.append(Button(tab1, text=qzname[i],font=fontlvlExp,width=45,bd=0))
            bttn[i].grid(row=j, column=0,padx=75, pady=5)
            bttn[i].configure(bg="blue",fg="white")
            bttn[i]["command"] = lambda x=qzname[i]: num_press(x)
            i += 1


    # === WIDGETS FOR TAB TWO # ===============================================================#

    listTreeuser = ttk.Treeview(tab2, height=19, columns=('Quiz Name', 'attempt', 'score', 'total score'))
    vsb = ttk.Scrollbar(tab2, orient="vertical", command=listTreeuser.yview)
    hsb = ttk.Scrollbar(tab2, orient="horizontal", command=listTreeuser.xview)
    listTreeuser.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    listTreeuser.heading("#0", text='QID', anchor='center')
    listTreeuser.column("#0", width=80, minwidth=50, anchor='center')
    listTreeuser.heading("#1", text='Quiz Name')
    listTreeuser.column("#1", width=200, minwidth=150, anchor='center')
    listTreeuser.heading("attempt", text='Attempt')
    listTreeuser.column("attempt", width=70, minwidth=50, anchor='center')
    listTreeuser.heading("score", text='Score')
    listTreeuser.column("score", width=50, minwidth=60, anchor='center')
    listTreeuser.heading("total score", text='Total Score')
    listTreeuser.column("total score", width=95, minwidth=50, anchor='center')

    listTreeuser.place(x=1, y=10)
    vsb.place(x=498, y=10, height=418)
    hsb.place(x=1, y=410, width=498)
    ttk.Style().configure("Treeview", font=('Times new Roman', 12))

    # === WIDGETS FOR TAB THREE
    oldpasslvl = tk.Label(tab3, text="Enter Old Password", font=fontlvlExp)
    oldpasslvl.place(x=60, y=90)
    entryoldpass = ttk.Entry(tab3, textvariable=oldpasstxt, width=30, font=fontExp, show="*")
    entryoldpass.place(x=200, y=90)

    newpasslvl = tk.Label(tab3, text="Enter New Password", font=fontlvlExp)
    newpasslvl.place(x=60, y=170)
    entrynewpass = ttk.Entry(tab3, textvariable=newpasstxt, width=30, font=fontExp, show="*")
    entrynewpass.place(x=200, y=170)

    changebtn = Button(tab3, text="Change", bd=0, fg="white", command=change_password, font=fontlvlExp, width=10)
    changebtn.configure(bg="red")
    changebtn.place(x=150, y=250)

    clearbtn = Button(tab3, text="Clear", bd=0, fg="white", command=clear_password, font=fontlvlExp, width=10)
    clearbtn.configure(bg="green")
    clearbtn.place(x=300, y=250)

    recov_set_btn = Button(tab3, text="Recovery Setting", bd=0, command=recov_set_win, font=fontlvlExp, width=29)
    recov_set_btn.configure(bg="light blue")
    recov_set_btn.place(x=150, y=310)


    # === WIDGETS FOR TAB FOUR
    imglvl=Label(tab4,bd=0).pack(padx=10,pady=60)
    quizlvl=tk.Label(tab4, text="Quiz System V 0.01",font=("Tahoma",15,"bold"))
    quizlvl.place(x=160, y=10)
    imglvl3=Label(tab4, image=imgMy,bd=0,bg="white").place(x=200, y=50)

    labelframe3= LabelFrame(tab4, text="Abhijeet Raj Modanwal",font= ("Tahoma",20),fg="blue",bd=2).pack(fill="both", expand="yes",padx=40,pady=35)
    urNamelvl = Label(tab4, text="Roll Id :",font = ("Tahoma",15))
    urNamelvl.place(x=130, y=230)
    urNamelvl = Label(tab4, text="14170025",font = ("Tahoma",15))
    urNamelvl.place(x=280, y=230)
    urNamelvl = Label(tab4, text="Exam Roll No :",font = ("Tahoma",15))
    urNamelvl.place(x=130, y=270)
    urNamelvl = Label(tab4, text="1701114001",font = ("Tahoma",15))
    urNamelvl.place(x=280, y=270)
    urNamelvl = Label(tab4, text="Reg. No. :",font = ("Tahoma",15))
    urNamelvl.place(x=130, y=310)
    urNamelvl = Label(tab4, text="14170025",font = ("Tahoma",15))
    urNamelvl.place(x=280, y=310)
    urNamelvl = Label(tab4, text="Course :",font = ("Tahoma",15))
    urNamelvl.place(x=130, y=350)
    urNamelvl = Label(tab4, text="M.C.A(6th Sem)",font = ("Tahoma",15))
    urNamelvl.place(x=280, y=350)
    tab_parent.pack(expand=1, fill='both')
    userWin.mainloop()

userwin()
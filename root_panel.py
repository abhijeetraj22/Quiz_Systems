from tkinter import messagebox
import testfunct
from testfunct import *
import os


root_win = None
logoutbtn = None
v = None
admNametxt = None
admEmailtxt = None
admMobtxt = None
admPasswdtxt = None
adRepasswdtxt = None

gen = None
mgadmNametxt = None
mgadmEmailtxt = None
mgadmMobtxt = None
mgadmPasswdtxt = None
mgadRepasswdtxt = None
entry11 = None
entry12 = None
entry13 = None
entry14 = None


f = open(r"C:\ESD\quizsystem.txt", "r")
root_name = f.read()
#print(root_name)
f.close()

listTreeadmin = None
entry_admin_id  = None
def admin_user_result():
    adm_id = entry_admin_id.get()
    temp = adm_quiz_detail(adm_id)
    if (len(temp) > 0):
        listTreeadmin.delete(*listTreeadmin.get_children())
        for row in temp:
            listTreeadmin.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
    else:
        tk.messagebox.showinfo('Info', 'No any Data Found')


def entered3(event):
    logoutbtn.config(bg="blue", fg="white")


def left3(event):
    logoutbtn.config(bg="light blue", fg="black")


def backHome():
    global root_win
    root_win.destroy()
    os.system('python main.py')


def upd_confirm():
    msgbox = tk.messagebox.askquestion('Warning', 'Are You Sure you want to Change the Data....', icon='warning')
    if msgbox == 'yes':
        search_id = entry11.get()
        temp = upd_admin_detail(entry12.get(), gen.get(), entry13.get(), entry14.get(), search_id)
        if (temp):
            tk.messagebox.showinfo('Info', 'Update Successfully')
            entry11.set("")
            mgadmNametxt.set("")
            gen.set("M")
            mgadmEmailtxt.set("")
            mgadmMobtxt.set("")
    else:
        tk.messagebox.showinfo('Info', 'Update Refuse')


def del_confirm():
    msgbox = tk.messagebox.askquestion('Warning', 'Are You Sure you want to Delete the Data....', icon='warning')
    if msgbox == 'yes':
        search_admin_id = entry11.get()
        temp = del_admin(search_admin_id)
        if (temp):
            tk.messagebox.showinfo('Info', 'Delete Successfully')
            entry11.set("")
            mgadmNametxt.set("")
            gen.set("M")
            mgadmEmailtxt.set("")
            mgadmMobtxt.set("")
            update_func()
    else:
        tk.messagebox.showinfo('Info', 'Delete Refuse')


def addSubAdmin():
    global wb
    admName = admNametxt.get()
    admGen = v.get()
    admEmail = admEmailtxt.get()
    admMob = admMobtxt.get()
    admPasswd = admPasswdtxt.get()
    admRepasswd = adRepasswdtxt.get()
    tempa = checkName(admName)

    if (tempa != 0 ):
        tempb = checkEmail(admEmail)
        if (tempb != 0):
            tempc = checkMob(admMob)
            if (tempc != 0):
                tempd = checkPassword(admPasswd, admRepasswd)
                if (tempd != 0):
                    temp = insert_into_admindata(admName, admGen, admEmail, admMob, admPasswd)

                    if (temp):
                        messagebox.showinfo("Database", "Admin Added Successfully")
                        admNametxt.set("")
                        admEmailtxt.set("")
                        v.set("M")
                        admMobtxt.set("")
                        admPasswdtxt.set("")
                        adRepasswdtxt.set("")
                        update_func()


def admin_detail(event):
    search_id = entry11.get()
    tempdata = admin_detail_fetch(search_id)
    for e in tempdata:
        data1 = e[1]
        data2 = e[2]
        data3 = e[3]
        data4 = e[4]
    #print(data1, data2, data3, data4)
    mgadmNametxt.set(data1)
    gen.set(data2)
    mgadmEmailtxt.set(data3)
    mgadmMobtxt.set(data4)


def update_func():
    load_admin_detail()
    adm_name = []
    for e in testfunct.rows:
        adm_name.append(e[0])
    entry11['values'] = adm_name
    entry_admin_id['values'] = adm_name


def root_on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Add Admin":
        update_func()
        #print("Add Admin tab selected")

    #if tab_text == "Manage Admin":
        #print("Manage Admin tab selected")


def rootWin():
    global v, admNametxt, admEmailtxt, admMobtxt, admPasswdtxt, adRepasswdtxt

    global gen, mgadmNametxt, mgadmEmailtxt, mgadmMobtxt, mgadmPasswdtxt, mgadRepasswdtxt
    global entry11, root_win, entry12, entry13, entry14, tab_parent, logoutbtn,entry_admin_id , listTreeadmin

    root_win = Tk()
    i, j, k, l = 520, 560, 400, 30
    root_win.geometry(f"{i}x{j}+{k}+{l}")
    root_win.resizable(0, 0)
    root_win['bg'] = "white"
    root_win.title("Root Panel")
    fontlvlExp = ("Tahoma", 10, "bold")
    fontExp = ("Tahoma", 11)

    v = StringVar()
    admNametxt = StringVar()
    admEmailtxt = StringVar()
    admMobtxt = StringVar()
    admPasswdtxt = StringVar()
    adRepasswdtxt = StringVar()

    gen = StringVar()
    mgadmNametxt = StringVar()
    mgadmEmailtxt = StringVar()
    mgadmMobtxt = StringVar()
    mgadmPasswdtxt = StringVar()
    mgadRepasswdtxt = StringVar()
    entry11 = None

    imageX = Image.open("venv/Image/quiz.png")
    width, height = imageX.size
    x, y = 80, 80
    imageX = imageX.resize((round(x / height * width), round(y)))
    imgX = ImageTk.PhotoImage(imageX)
    imageY = Image.open("venv/Image/systemImg.png")
    width, height = imageY.size
    x, y = 35, 35
    imageY = imageY.resize((round(x / height * width), round(y)))
    imgY = ImageTk.PhotoImage(imageY)

    imageMy = Image.open("venv/Image/my_img.jpg")
    width, height = imageMy.size
    x, y = 120, 120
    imageMy = imageMy.resize((round(x / height * width), round(y)))
    imgMy = ImageTk.PhotoImage(imageMy)
    imglogout = PhotoImage(file="venv/Image/logout2.png")
    logoutimg = imglogout.subsample(1, 1)

    imglvl = Label(root_win, bd=0, bg="white").pack(padx=10, pady=45)
    imglvl = Label(root_win, image=imgX, bd=0).place(x=5, y=1)
    imglvl2 = Label(root_win, image=imgY, bd=0, bg="white").place(x=120, y=40)
    urNamelvl = Label(root_win, text=root_name, font=("Tahoma", 12), bg="white")
    urNamelvl.place(x=1, y=80)
    logoutbtn = Button(root_win, text="Logout",image= logoutimg, compound= RIGHT , command=backHome, bd=0,bg="light blue",font=("Tahoma", 11),width=70)
    logoutbtn.place(x=445, y=75)
    logoutbtn.bind("<Enter>", entered3)
    logoutbtn.bind("<Leave>", left3)

    tab_parent = ttk.Notebook(root_win)
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=fontlvlExp)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)

    tab_parent.bind("<<NotebookTabChanged>>", root_on_tab_selected)

    tab_parent.add(tab1, text="Add Admin")
    tab_parent.add(tab2, text="Manage Admin")
    tab_parent.add(tab3, text="Added Quiz")
    tab_parent.add(tab4, text="About")

    # === WIDGETS FOR TAB ONE
    v.set("M")
    values = {"Male": "M",
              "Female": "F"
              }

    admNamelvl = Label(tab1, text="Full Name  :", font=fontlvlExp)
    admNamelvl.place(x=80, y=70)
    entry1 = Entry(tab1, textvariable=admNametxt, width=25, font=fontlvlExp)
    entry1.place(x=210, y=70)
    admGenlvl = Label(tab1, text="Gender :", font=fontlvlExp)
    admGenlvl.place(x=80, y=120)
    rx, ry = 210, 120
    for (text, value) in values.items():
        Radiobutton(tab1, text=text, variable=v,
                    value=value, font=fontlvlExp).place(x=rx, y=ry)
        rx += 80

    admEmaillvl = Label(tab1, text="Email :", font=fontlvlExp)
    admEmaillvl.place(x=80, y=170)
    entry3 = Entry(tab1, textvariable=admEmailtxt, width=25, font=fontlvlExp)
    entry3.place(x=210, y=170)
    admMoblvl = Label(tab1, text="Mobile :", font=fontlvlExp)
    admMoblvl.place(x=80, y=220)
    entry4 = Entry(tab1, textvariable=admMobtxt, width=25, font=fontlvlExp)
    entry4.place(x=210, y=220)
    admPasswdlvl = Label(tab1, text="Password :", font=fontlvlExp)
    admPasswdlvl.place(x=80, y=270)
    entry5 = Entry(tab1, textvariable=admPasswdtxt, width=25, font=fontlvlExp, show="*")
    entry5.place(x=210, y=270)
    adRepasswdlvl = Label(tab1, text="Re-Password :", font=fontlvlExp)
    adRepasswdlvl.place(x=80, y=320)
    entry6 = Entry(tab1, textvariable=adRepasswdtxt, width=25, font=fontlvlExp, show="*")
    entry6.place(x=210, y=320)

    enter = Button(tab1, text="Add Admin", command=addSubAdmin, bd=0, font=fontlvlExp)
    enter.configure(bg="light blue")
    enter.place(x=210, y=375)
###############################################TAB2#################################################
    gen.set("M")
    values = {"Male": "M",
              "Female": "F"
              }

    admIdlvl = Label(tab2, text="Admin ID. :", font=fontlvlExp)
    admIdlvl.place(x=80, y=60)
    entry11 = ttk.Combobox(tab2, width=23, font=fontExp)
    entry11.place(x=210, y=60)
    entry11.bind("<<ComboboxSelected>>", admin_detail)

    admNamelvl = Label(tab2, text="Full Name  :", font=fontlvlExp)
    admNamelvl.place(x=80, y=105)
    entry12 = Entry(tab2, textvariable=mgadmNametxt, width=25, font=fontlvlExp)
    entry12.place(x=210, y=105)
    admGenlvl = Label(tab2, text="Gender :", font=fontlvlExp)
    admGenlvl.place(x=80, y=150)
    rx, ry = 210, 150
    for (text, value) in values.items():
        Radiobutton(tab2, text=text, variable=gen,
                    value=value, font=fontlvlExp).place(x=rx, y=ry)
        rx += 80

    admEmaillvl = Label(tab2, text="Email :", font=fontlvlExp)
    admEmaillvl.place(x=80, y=195)
    entry13 = Entry(tab2, textvariable=mgadmEmailtxt, width=25, font=fontlvlExp)
    entry13.place(x=210, y=195)
    adm_moblvl = Label(tab2, text="Mobile :", font=fontlvlExp)
    adm_moblvl.place(x=80, y=240)
    entry14 = Entry(tab2, textvariable=mgadmMobtxt, width=25, font=fontlvlExp)
    entry14.place(x=210, y=240)

    enterupdate = Button(tab2, text="Update", command=upd_confirm, bd=0, font=fontExp, width=15)
    enterupdate.configure(bg="light green")
    enterupdate.place(x=100, y=300)
    enterdelete = Button(tab2, text="Delete", command=del_confirm, bd=0,fg="white", font=fontExp, width=15)
    enterdelete.configure(bg="red")
    enterdelete.place(x=280, y=300)

    ##################################################################
    # === WIDGETS FOR TAB FOUR ===================================#

    quizNamelvl = tk.Label(tab3, text="Admin ID:", font=fontlvlExp)
    quizNamelvl.place(x=60, y=15)
    entry_admin_id = ttk.Combobox(tab3, width=30, font=fontExp)
    entry_admin_id.place(x=40, y=40)
    searchbtn = Button(tab3, text="Search", command=admin_user_result, bd=0, font=fontExp, width=15)
    searchbtn.configure(bg="light green")
    searchbtn.place(x=350, y=38)

    listTreeadmin = ttk.Treeview(tab3, height=15, columns=('Time(min)', 'Per_Qs(Score)', 'Qs Attempt', 'Admin Name'))
    vsb = ttk.Scrollbar(tab3, orient="vertical", command=listTreeadmin.yview)
    hsb = ttk.Scrollbar(tab3, orient="horizontal", command=listTreeadmin.xview)
    listTreeadmin.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    listTreeadmin.heading("#0", text='Quiz Name', anchor='center')
    listTreeadmin.column("#0", width=140, minwidth=100, anchor='center')
    listTreeadmin.heading("#1", text='Time(min)')
    listTreeadmin.column("#1", width=80, minwidth=50, anchor='center')
    listTreeadmin.heading("Per_Qs(Score)", text='Per_Qs(Score)')
    listTreeadmin.column("Per_Qs(Score)", width=80, minwidth=50, anchor='center')
    listTreeadmin.heading("Qs Attempt", text='Qs Attempt')
    listTreeadmin.column("Qs Attempt", width=70, minwidth=50, anchor='center')
    listTreeadmin.heading("Admin Name", text='Admin Name')
    listTreeadmin.column("Admin Name", width=135, minwidth=50, anchor='center')

    # listTree.bind('<Button-1>',handle) if you don't want to expand column activat this and the above handle function
    listTreeadmin.place(x=1, y=90)
    # listTree.grid(row=1, column=0)
    vsb.place(x=498, y=90, height=327)
    # vsb.grid(row=2, column=0)
    hsb.place(x=1, y=410, width=500)
    # hsb.grid(row=1, column=0)
    ttk.Style().configure("Treeview", font=('Times new Roman', 12))

    ##################################################################
    # === WIDGETS FOR TAB FOUR ===================================#
    imglvl = Label(tab4, bd=0).pack(padx=10, pady=60)
    quizlvl = tk.Label(tab4, text="Quiz System V 0.01", font=("Tahoma", 15, "bold"))
    quizlvl.place(x=160, y=10)
    imglvl3 = Label(tab4, image=imgMy, bd=0, bg="white").place(x=200, y=50)

    labelframe3 = LabelFrame(tab4, text="Abhijeet Raj Modanwal", font=("Tahoma", 20), fg="blue", bd=2).pack(fill="both",
                                                                                                            expand="yes",
                                                                                                            padx=40,
                                                                                                            pady=35)
    urNamelvl = Label(tab4, text="Roll Id :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=230)
    urNamelvl = Label(tab4, text="14170025", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=230)
    urNamelvl = Label(tab4, text="Exam Roll No :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=270)
    urNamelvl = Label(tab4, text="1701114001", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=270)
    urNamelvl = Label(tab4, text="Reg. No. :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=310)
    urNamelvl = Label(tab4, text="14170025", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=310)
    urNamelvl = Label(tab4, text="Course :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=350)
    urNamelvl = Label(tab4, text="M.C.A(6th Sem)", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=350)
    tab_parent.pack(expand=1, fill='both')
    root_win.mainloop()

rootWin()
from tkinter import messagebox
import testfunct
from testfunct import *


admin_win = None
qz_name_entry2 = None
qdescrptxt2 = None
qz_timelmt_entry2 = None
qz_scoreeachques_entry2 = None
qz_attemptques_entry2 = None
qz_totalques_entry2 = None

qz_name_entry = None
qdescrptxt = None
qz_timelmt_entry = None
qz_scoreeachques_entry = None
qz_attemptques_entry = None
qz_totalques_entry = None
quploadedlvl = None
qznametxt = None
entry_qz_name = None
logoutbtn = None

file_name = "Not select!!"
sheet = None
entrynewpass = None
entryoldpass = None
newpasstxt = None
oldpasstxt = None
fg_qname = []

f = open(r"QuizDetail/quizsystem.txt", "r")
admin_email = f.read()
ft = open(r"QuizDetail/quiztype.txt", "r")
acc_type = ft.read()
#print(acc_type)
#print(admin_email)
Data = fetch_name(acc_type,admin_email)
admin_name = Data[0]
admin_id = Data[1]
ft.close()
f.close()


def clear_password():
    oldpasstxt.set("")
    newpasstxt.set("")


def recov_set_win():
    admin_win.destroy()
    os.system('python set_recov.py')


def change_password():
    oldpass = entryoldpass.get()
    newpass = entrynewpass.get()
    #print(admin_email,oldpass,newpass)
    temp = change_password_func(acc_type,admin_email,oldpass,newpass)
    if(temp):
        tk.messagebox.showinfo('Info', 'Change Password Successfully')
        clear_password()
    else:
        tk.messagebox.showinfo('Info', 'Old Password Wrong')


def admin_user_result():
    quiz_name = entry_qz_name.get()
    temp = adm_user_result(quiz_name)
    if (len(temp) > 0):
        listTreeadmin.delete(*listTreeadmin.get_children())
        for row in temp:
            listTreeadmin.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
    else:
        tk.messagebox.showinfo('Info', 'No any Data Found')


def adm_upd_confirm():
    MsgBox = tk.messagebox.askquestion('Warning', 'Are you Sure want to Change the Data....', icon='warning')
    if MsgBox == 'yes':
        # upd_quiz()
        search_quiz_name = qz_name_entry2.get()
        qtimelimit = qz_timelmt_entry2.get()
        qpermark = qz_scoreeachques_entry2.get()
        q_attempt_ques = qz_attemptques_entry2.get()
        q_total_ques = qz_totalques_entry2.get()
        temp = upd_quiz(qtimelimit, qpermark, q_attempt_ques, q_total_ques, search_quiz_name)
        if (temp > 0):
            tk.messagebox.showinfo('Info', 'Update Successfully')
            qz_name_entry2.set("")
            qz_timelmt_entry2.set("")
            qz_scoreeachques_entry2.set("")
            qz_attemptques_entry2.set("")
            qz_totalques_entry2.set("")
    else:
        tk.messagebox.showinfo('Info', 'Update Refuse')


def adm_del_confirm():
    msgbox = tk.messagebox.askquestion('Warning', 'Are you Sure want to Delete the Data....', icon='warning')
    if msgbox == 'yes':
        search_quiz_name = qz_name_entry2.get()
        temp = del_quiz(search_quiz_name)
        if (temp > 0):
            tk.messagebox.showinfo('Info', 'Delete Successfully')
            qz_name_entry2.set("")
            qz_timelmt_entry2.set("")
            qz_scoreeachques_entry2.set("")
            qz_attemptques_entry2.set("")
            qz_totalques_entry2.set("")
            update_func_quiz()
    else:
        tk.messagebox.showinfo('Info', 'Delete Refuse')


def backHome_adm():
    global admin_win
    admin_win.destroy()
    os.system('python main.py')


def uploadFileHandler():
    global file_name, sheet
    try:
        faddress = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx;*.xls;*.xlsm"),
                                                         ("All files", "*.*")))
        wb = xlrd.open_workbook(faddress)
        file_name = wb.sheet_names()
        wb = xlrd.open_workbook(faddress)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
    except FileNotFoundError:
        messagebox.showerror("Open Source File", "Failed to read file\n'%s'" % faddress)
        file_name = "Not select!!"
    quploadedlvl['text'] = file_name


def create_quiz():
    global file_name
    qname = qz_name_entry.get()
    qtimelimit = qz_timelmt_entry.get()
    qpermark = qz_scoreeachques_entry.get()
    q_attempt_ques = qz_attemptques_entry.get()
    q_total_ques = qz_totalques_entry.get()
    tempa = checkQName(qname)

    if (tempa != 0):
        if (file_name == "Not select!!"):
            messagebox.showwarning("Warning", "Please select File !!!!")

        else:
            temp = insert_into_data_quiz(qname, qtimelimit, qpermark, q_attempt_ques, q_total_ques, sheet, admin_id)
            if (temp):
                messagebox.showinfo("Database", "Quiz Added Successfully")
                qznametxt.set("")
                file_name = ""
                quploadedlvl['text'] = file_name
                update_func_quiz()


def database_error(msgs, err):
    messagebox.showinfo(msgs, err)
    return False


def qzname_detail(event):
    search_qname = qz_name_entry2.get()
    qzd_tempData = qzname_detail_fetch(search_qname)

    if (len(qzd_tempData) > 0):
        for e in qzd_tempData:
            data1 = e[2]
            data2 = e[3]
            data3 = e[4]
            data4 = e[5]

        #print(data1, data2, data3, data4)
        qz_timelmt_entry2.set(data1)
        qz_scoreeachques_entry2.set(data2)
        qz_attemptques_entry2.set(data3)
        qz_totalques_entry2.set(data4)


def update_func_quiz():
    fg_qname = []
    load_quiz_name()
    for e in testfunct.rows:
        fg_qname.append(e[1])
    qz_name_entry2['values'] = fg_qname
    entry_qz_name['values'] = fg_qname


def on_tab_selected_quiz(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Add Quiz":
        update_func_quiz()
        #print("Add Quiz tab selected")

    # if tab_text == "Manage Quiz":
    #     print("Manage Quiz tab selected")
    #
    # if tab_text == "Quiz Result":
    #     print("Quiz Result tab selected")



def entered3(event):
    logoutbtn.config(bg="blue", fg="white")


def left3(event):
    logoutbtn.config(bg="light blue", fg="black")


def admin_Win():
    # mainDestroy()
    global qz_name_entry2, qdescrptxt2, qz_timelmt_entry2, qz_scoreeachques_entry2, qz_attemptques_entry2, qz_totalques_entry2
    global qz_name_entry, qdescrptxt, qz_timelmt_entry, qz_scoreeachques_entry, qz_attemptques_entry, qz_totalques_entry, entry_qz_name
    global quploadedlvl, qznametxt, logoutbtn, admin_win, listTreeadmin, entryoldpass,entrynewpass, oldpasstxt, newpasstxt

    admin_win = Tk()
    i, j, k, l = 520, 565, 400, 30
    admin_win.geometry(f"{i}x{j}+{k}+{l}")
    admin_win.tk.call('wm','iconphoto',admin_win, ImageTk.PhotoImage(file='venv/Image/quiz_icon.png'))
    admin_win.resizable(0, 0)
    admin_win['bg'] = "white"
    admin_win.title("Admin Panel")
    fontbtnExp = ("Tahoma", 11, "bold")
    fontlvlExp = ("Tahoma", 10, "bold")
    fontExp = ("Tahoma", 11)

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

    imglvl = Label(admin_win, bd=0, bg="white").pack(padx=10, pady=45)
    imglvl = Label(admin_win, image=imgX, bd=0).place(x=5, y=1)
    imglvl2 = Label(admin_win, image=imgY, bd=0, bg="white").place(x=120, y=40)
    urNamelvl = Label(admin_win, text=admin_name, font=("Tahoma", 12), bg="white")
    urNamelvl.place(x=1, y=80)
    logoutbtn = Button(admin_win, text="Logout", image=logoutimg, compound=RIGHT, command=backHome_adm, bd=0,
                       bg="light blue",
                       font=("Tahoma", 11), width=70)
    logoutbtn.place(x=445, y=75)
    # command=backHome
    logoutbtn.bind("<Enter>", entered3)
    logoutbtn.bind("<Leave>", left3)

    tab_parent = ttk.Notebook(admin_win)
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=fontlvlExp)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)
    tab5 = ttk.Frame(tab_parent)

    tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected_quiz)

    tab_parent.add(tab1, text="Add Quiz")
    tab_parent.add(tab2, text="Manage Quiz")
    tab_parent.add(tab3, text="Quiz Result")
    tab_parent.add(tab4, text="Change Pin")
    tab_parent.add(tab5, text="About")

    qznametxt = StringVar()
    oldpasstxt = StringVar()
    newpasstxt = StringVar()
    qztimelimittxt = list(range(1, 361))
    qzpermarktxt = list(range(1, 100))

    qtimelimittxt = list(range(1, 361))
    qpermarktxt = list(range(1, 100))

    # === WIDGETS FOR TAB ONE

    qnamelvl = Label(tab1, text="Quiz Name:", font=fontlvlExp)
    qnamelvl.place(x=40, y=80)
    qz_name_entry = ttk.Entry(tab1, textvariable=qznametxt, width=30, font=fontExp)
    qz_name_entry.place(x=180, y=80)

    qtimelimitlvl = Label(tab1, text="Time Limit:", font=fontlvlExp)
    qtimelimitlvl.place(x=40, y=130)
    qz_timelmt_entry = ttk.Combobox(tab1, values=qztimelimittxt, width=3, font=fontExp)
    qz_timelmt_entry.place(x=180, y=130)
    qz_timelmt_entry.current(2)
    minlvl = Label(tab1, text="minutes", font=fontlvlExp)
    minlvl.place(x=250, y=130)
    qtotalqulvl = Label(tab1, text="Total Ques.:", font=fontlvlExp)
    qtotalqulvl.place(x=40, y=180)
    qz_totalques_entry = ttk.Combobox(tab1, values=qzpermarktxt, width=3, font=fontExp)
    qz_totalques_entry.place(x=180, y=180)
    qz_totalques_entry.current(9)

    qpermarklvl = Label(tab1, text="Ques. each Score:", font=fontlvlExp)
    qpermarklvl.place(x=40, y=230)
    qz_scoreeachques_entry = ttk.Combobox(tab1, values=qzpermarktxt, width=3, font=fontExp)
    qz_scoreeachques_entry.place(x=180, y=230)
    qz_scoreeachques_entry.current(5)
    qattemptqulvl = Label(tab1, text="Attempt Ques.:", font=fontlvlExp)
    qattemptqulvl.place(x=40, y=280)
    qz_attemptques_entry = ttk.Combobox(tab1, values=qzpermarktxt, width=3, font=fontExp)
    qz_attemptques_entry.place(x=180, y=280)
    qz_attemptques_entry.current(6)

    upload_filebtn = Button(tab1, text="Upload Qs.", command=uploadFileHandler, bd=0, font=fontbtnExp, width=12)
    upload_filebtn.configure(bg="light blue")
    upload_filebtn.place(x=320, y=180)
    quploadedlvl = Label(tab1, text="", font=fontlvlExp)
    quploadedlvl.place(x=320, y=230)
    qadmin_winatlvl = Label(tab1, text="(.xlsx,.xls,.xlsm)file", font=fontlvlExp)
    qadmin_winatlvl.place(x=310, y=210)

    createBtn = Button(tab1, text="Create", command=create_quiz, bd=0, font=fontbtnExp, width=15)
    createBtn.configure(bg="pink")
    createBtn.place(x=200, y=345)

    # === WIDGETS FOR TAB TWO

    qnamelvl = Label(tab2, text="Quiz Name :", font=fontlvlExp)
    qnamelvl.place(x=40, y=80)
    qz_name_entry2 = ttk.Combobox(tab2, width=30, font=fontExp)
    qz_name_entry2.place(x=180, y=80)
    qz_name_entry2.bind("<<ComboboxSelected>>", qzname_detail)

    qtimelimitlvl = Label(tab2, text="Time Limit  :", font=fontlvlExp)
    qtimelimitlvl.place(x=40, y=130)
    qz_timelmt_entry2 = ttk.Combobox(tab2, values=qtimelimittxt, width=3, font=fontExp)
    qz_timelmt_entry2.place(x=180, y=130)

    minlvl = Label(tab2, text="minutes", font=fontlvlExp)
    minlvl.place(x=250, y=130)

    qpermarklvl = Label(tab2, text="Ques. each Score:", font=fontlvlExp)
    qpermarklvl.place(x=40, y=180)
    qz_scoreeachques_entry2 = ttk.Combobox(tab2, values=qpermarktxt, width=3, font=fontExp)
    qz_scoreeachques_entry2.place(x=180, y=180)

    qtotalqulvl = Label(tab2, text="Total Ques.:", font=fontlvlExp)
    qtotalqulvl.place(x=40, y=230)
    qz_totalques_entry2 = ttk.Combobox(tab2, values=qpermarktxt, width=3, font=fontExp)
    qz_totalques_entry2.place(x=180, y=230)
    # entry6.current(4)
    qattemptqulvl = Label(tab2, text="Attempt Ques.:", font=fontlvlExp)
    qattemptqulvl.place(x=40, y=280)
    qz_attemptques_entry2 = ttk.Combobox(tab2, values=qpermarktxt, width=3, font=fontExp)
    qz_attemptques_entry2.place(x=180, y=280)
    # qz_attemptques_entry2.current(6)

    updateBtn = Button(tab2, text="Update", command=adm_upd_confirm, bd=0, font=fontbtnExp, width=15)
    updateBtn.configure(bg="light green")
    updateBtn.place(x=100, y=345)

    deleteBtn = Button(tab2, text="Delete", command=adm_del_confirm, bd=0, fg="white", font=fontbtnExp, width=15)
    deleteBtn.configure(bg="red")
    deleteBtn.place(x=300, y=345)

    ###############################################
    # === WIDGETS FOR TAB THREE =================#
    quizNamelvl = tk.Label(tab3, text="Quiz Name:", font=fontlvlExp)
    quizNamelvl.place(x=60, y=15)
    entry_qz_name = ttk.Combobox(tab3, width=30, font=fontExp)
    entry_qz_name.place(x=40, y=40)
    searchBtn = Button(tab3, text="Search", command=admin_user_result, bd=0, font=fontbtnExp, width=15)
    searchBtn.configure(bg="light green")
    searchBtn.place(x=350, y=38)

    listTreeadmin = ttk.Treeview(tab3, height=15, columns=('User Name', 'Attempt', 'Score', 'Total Score'))
    vsb = ttk.Scrollbar(tab3, orient="vertical", command=listTreeadmin.yview)
    hsb = ttk.Scrollbar(tab3, orient="horizontal", command=listTreeadmin.xview)
    listTreeadmin.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    listTreeadmin.heading("#0", text='UID', anchor='center')
    listTreeadmin.column("#0", width=80, minwidth=50, anchor='center')
    listTreeadmin.heading("#1", text='User Name')
    listTreeadmin.column("#1", width=200, minwidth=150, anchor='center')
    listTreeadmin.heading("Attempt", text='Attempt')
    listTreeadmin.column("Attempt", width=70, minwidth=50, anchor='center')
    listTreeadmin.heading("Score", text='Score')
    listTreeadmin.column("Score", width=50, minwidth=60, anchor='center')
    listTreeadmin.heading("Total Score", text='Total Score')
    listTreeadmin.column("Total Score", width=95, minwidth=50, anchor='center')

    # listTree.bind('<Button-1>',handle) if you don't want to expand column activat this and the above handle function
    listTreeadmin.place(x=1, y=90)
    # listTree.grid(row=1, column=0)
    vsb.place(x=498, y=90, height=327)
    # vsb.grid(row=2, column=0)
    hsb.place(x=1, y=417, width=490)
    # hsb.grid(row=1, column=0)
    ttk.Style().configure("Treeview", font=('Times new Roman', 12))

    # === WIDGETS FOR TAB FOUR####################################
    oldpasslvl = tk.Label(tab4, text="Enter Old Password", font=fontlvlExp)
    oldpasslvl.place(x=60, y=90)
    entryoldpass = ttk.Entry(tab4, textvariable=oldpasstxt, width=30, font=fontExp, show="*")
    entryoldpass.place(x=200, y=90)

    newpasslvl = tk.Label(tab4, text="Enter New Password", font=fontlvlExp)
    newpasslvl.place(x=60, y=170)
    entrynewpass = ttk.Entry(tab4, textvariable=newpasstxt, width=30, font=fontExp, show="*")
    entrynewpass.place(x=200, y=170)

    changebtn = Button(tab4, text="Change", bd=0, fg="white", command=change_password, font=fontlvlExp, width=10)
    changebtn.configure(bg="red")
    changebtn.place(x=150, y=250)

    clearbtn = Button(tab4, text="Clear", bd=0, fg="white", command=clear_password, font=fontlvlExp, width=10)
    clearbtn.configure(bg="green")
    clearbtn.place(x=300, y=250)

    recov_set_btn = Button(tab4, text="Recovery Setting", bd=0, command=recov_set_win, font=fontlvlExp, width=29)
    recov_set_btn.configure(bg="light blue")
    recov_set_btn.place(x=150, y=310)

    # === WIDGETS FOR TAB FIVE##############################
    imglvl = Label(tab5, bd=0).pack(padx=10, pady=60)
    quizlvl = tk.Label(tab5, text="Quiz System V 0.01", font=("Tahoma", 15, "bold"))
    quizlvl.place(x=160, y=10)
    imglvl3 = Label(tab5, image=imgMy, bd=0, bg="white").place(x=200, y=50)

    labelframe3 = LabelFrame(tab5, text="Abhijeet Raj Modanwal", font=("Tahoma", 20), fg="blue", bd=2).pack(fill="both",
                                                                                                            expand="yes",
                                                                                                            padx=40,
                                                                                                            pady=35)
    urNamelvl = Label(tab5, text="Roll Id :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=230)
    urNamelvl = Label(tab5, text="14170025", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=230)
    urNamelvl = Label(tab5, text="Exam Roll No :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=270)
    urNamelvl = Label(tab5, text="1701114001", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=270)
    urNamelvl = Label(tab5, text="Reg. No. :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=310)
    urNamelvl = Label(tab5, text="14170025", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=310)
    urNamelvl = Label(tab5, text="Course :", font=("Tahoma", 15))
    urNamelvl.place(x=130, y=350)
    urNamelvl = Label(tab5, text="M.C.A(6th Sem)", font=("Tahoma", 15))
    urNamelvl.place(x=280, y=350)
    tab_parent.pack(expand=1, fill='both')
    admin_win.mainloop()


admin_Win()
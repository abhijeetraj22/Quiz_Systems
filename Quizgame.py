import testfunct
from testfunct import *


time_limit = None
score_each_ques = None
attempt_ques = None
total_ques = None

ques = 1
y = 0
indexd = []
radiovar = None
lblQuestion = None
r1 = None
r2 = None
r3 = None
r4 = None

timerlb = None
count = None
t = None

labelimage = None
labeltext = None
btnStart = None
lblInstruction = None
lblRules = None
gameWin = None

q_name = None

user_answer = []
indexes = []
questions = []
answers_choice = []
answers = []


f = open("QuizDetail/quizsystem.txt", "r")
user_email = f.read()
#print(user_email)
f.close()

f = open("QuizDetail/quizname.txt", "r")
quiz_name = f.read()
#print(quiz_name)
f.close()


def start():
    global count
    count = 0
    start_timer()


def start_timer():
    global count
    timer()


def stop_timer():
    global count
    count = 1
    calc()


def backIspressed():
    global gameWin
    gameWin.destroy()
    os.system('python user_Panel.py')


def timer():
    global count,t
    if (count == 0):
        d = str(t.get())
        h, m, s = map(int, d.split(":"))

        hour = int(h)
        min = int(m)
        sec = int(s)
        #print(d)
        if(d == "00:00:00"):
            stop_timer()
        #print(hour, min, sec)

        if sec > 0:
            sec = sec - 1
        elif sec == 0 and min > 0:
            sec = 59
            min = min - 1
        elif min == 0 and hour > 0:
            sec = 59
            min = 59
            hour = hour - 1
        elif sec == 0 and min == 0 and hour == 0:
            count = 1

        if (hour < 10):
            hour = str(0) + str(hour)
        else:
            hour = str(hour)
        if (min < 10):
            min = str(0) + str(min)
        else:
            min = str(min)
        if (sec < 10):
            sec = str(0) + str(sec)
        else:
            sec = str(sec)
        d = hour + ":" + min + ":" + sec
        t.set(d)
        # print(self.d)
    if (count == 0):
        gameWin.after(930, start_timer)


def user_qzname_detail(qz_name):
    global time_limit, score_each_ques, attempt_ques, total_ques
    tempdata = qzname_detail_fetch(qz_name)
    if (len(tempdata) > 0):
        for e in tempdata:
            time_limit = e[2]
            score_each_ques = e[3]
            attempt_ques = e[4]
            total_ques = e[5]
    #print(time_limit, score_each_ques, attempt_ques, total_ques)


def showresult(score):
    global user_btnBack, attempt_ques, score_each_ques
    timerlb.destroy()
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    user_labelimage = Label(
        gameWin,
        background="#ffffff",
        border=0,
    )
    user_labelimage.pack(pady=(50, 30))
    user_labelresulttext = Label(
        gameWin,
        font=("Consolas", 20),
        background="#ffffff",
    )
    user_labelresulttext.pack()
    user_btnBack = Button(
        gameWin,
        text="Back",
        relief=FLAT,
        border=0,
        font=("Consolas",15),
        bg = "green",
        fg = "white",
        width = 10,
        command=backIspressed,
    )
    user_btnBack.pack()
    #print(score)

    if score >= (80*int(attempt_ques) * int(score_each_ques))/100:
        img = PhotoImage(file="venv/Image/great.png")
        user_labelimage.configure(image=img)
        user_labelimage.image = img
        user_labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= (40*int(attempt_ques) * int(score_each_ques))/100) and (score < (80*int(attempt_ques) * int(score_each_ques))/100):
        img = PhotoImage(file="venv/Image/ok.png")
        user_labelimage.configure(image=img)
        user_labelimage.image = img
        user_labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="venv/Image/bad.png")
        user_labelimage.configure(image=img)
        user_labelimage.image = img
        user_labelresulttext.configure(text="You Should Work Hard !!")
    result_insert(score,int(attempt_ques) * int(score_each_ques))


def result_insert(score_field,total_field):
    global q_name
    insert_into_user_result(q_name, user_email,score_field,total_field)


def calc():
    global indexes,user_answer,answers,indexd
    x = 0
    score = 0
    for i in indexd:
        #print(user_answer[x] ,"==", answers[i])
        if user_answer[x] == answers[i]:
            score = score + score_each_ques
        x += 1
    #print(score)
    showresult(score)


def selected():
    global radiovar, user_answer,indexd,count
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    #print(x)
    user_answer.append(x+1)
    radiovar.set(-1)
    indexd.append(indexes[ques-1])
    #print(indexd)

    if ques < attempt_ques:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        stop_timer()


def startquiz():
    global lblQuestion, r1, r2, r3, r4,t,timerlb
    t = StringVar()
    global count
    count = 0
    hour = int(time_limit / 60)
    min = time_limit % 60
    if (hour < 10):
        hour = str(0) + str(hour)
    else:
        hour = str(hour)
    if (min < 10):
        min = str(0) + str(min)
    else:
        min = str(min)

    d = hour + ":" + min + ":" + "00"
    t.set(d)
    timerlb = Label(gameWin, textvariable=t, bg="white")
    timerlb.config(font=("Courier 20 bold"))
    timerlb.place(x=280, y=10)
    #timer()

    lblQuestion = Label(
        gameWin,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        gameWin,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        gameWin,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        gameWin,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        gameWin,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)
    start()


def generate_ques():
    global indexes
    #print(type(attempt_ques))
    while (len(indexes) < int(attempt_ques)):
        x = random.randint(0, int(total_ques)-1)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    generate_ques()
    startquiz()


def num_press_quiz(name):
    global labelimage, labeltext, btnStart, lblInstruction, lblRules,q_name,gameWin
    user_qzname_detail(name)
    qz_q_rows=load_quiz(name)
    if (len(qz_q_rows) > 0):
        for qze in qz_q_rows:
            questions.append(qze[1])
            answers.append(qze[6])
            for i in range(4):
                tempar = []
                tempar.append(qze[2])
                tempar.append(qze[3])
                tempar.append(qze[4])
                tempar.append(qze[5])
            answers_choice.append(tempar)
    #print(questions)
    #print(answers)
    #print(answers_choice)

    q_name = name
    #print(q_name)

    gameWin = Tk()
    gameWin.title("Quiz")
    i, j, k, l = 700, 600, 400, 30
    gameWin.geometry(f"{i}x{j}+{k}+{l}")
    gameWin.config(background="#ffffff")
    gameWin.resizable(0, 0)

    img1 = PhotoImage(file="venv/Image/transparentGradHat.png")
    labelimage = Label(
        gameWin,
        image=img1,
        background="#ffffff",
    )
    labelimage.pack(pady=(40, 0))

    labeltext = Label(
        gameWin,
        text=q_name,
        font=("Comic sans MS", 24, "bold"),
        background="#ffffff",
    )
    labeltext.pack(pady=(0, 50))

    img2 = PhotoImage(file="venv/Image/Frame.png")
    btnStart = Button(
        gameWin,
        image=img2,
        relief=FLAT,
        border=0,
        command=startIspressed,
    )
    btnStart.pack()

    lblInstruction = Label(
        gameWin,
        text="Read The Rules And\nClick Start Once You Are ready",
        background="#ffffff",
        font=("Consolas", 14),
        justify="center",
    )
    lblInstruction.pack(pady=(10, 100))

    lblRules = Label(
        gameWin,
        text=f"This quiz contains {attempt_ques} questions ({score_each_ques} Mark per Question)\nYou will get {time_limit} minutes to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
        width=100,
        font=("Times", 14),
        background="#000000",
        foreground="#FACA2F",
    )
    lblRules.pack()
    gameWin.mainloop()


num_press_quiz(quiz_name)
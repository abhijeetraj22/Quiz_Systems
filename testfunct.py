import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import xlrd
import pymysql
import sqlite3
from sqlite3 import Error
import os
import re
import shutil
import db_config
from tkinter.scrolledtext import ScrolledText
import random

rows=""
num_of_rows=""


def load_quiz(q_name):
    global qz_rows
    global qz_num_of_rows
    fg_qname=[]
    #print("okkkkkkkk",q_name)
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        #
        cursor = con.cursor()
        qry2 = f"SELECT * from quiz_question where quiz_id=(select quiz_id from quiz_detail where quiz_name='{q_name}')"
        cursor.execute(qry2)
        qz_rows = cursor.fetchall()
        qz_num_of_rows = cursor.rowcount
        cursor.close()
        con.close()
        has_loaded_successfully = qz_rows
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


#################################################################################user Win

def change_password_func(acc_type, email,oldpass,newpass):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        if(acc_type == "Admin"):
            qry_pass = f"SELECT admin_password from admin_detail WHERE admin_email ='{email}'"
        elif(acc_type == "User"):
            qry_pass = f"SELECT user_password from user_detail WHERE user_email ='{email}'"
        cursor.execute(qry_pass)
        passdata = cursor.fetchone()
        #print(passdata[0])
        if(passdata[0] == oldpass):
            if (acc_type == "Admin"):
                qry = f"UPDATE admin_detail SET admin_password ='{newpass}' where admin_email ='{email}'"
            elif (acc_type == "User"):
                qry = f"UPDATE user_detail SET user_password ='{newpass}' where user_email ='{email}'"
            cursor.execute(qry)
            temp = True
        else:
            temp = False
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def insert_into_user_result(qname_field, email_field,score_field,total_field):
    u_attempt=None
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")

        cursor = con.cursor()
        qry_u = f"SELECT quiz_id from quiz_detail where quiz_name = '{qname_field}'"
        cursor.execute(qry_u)
        quiz_id = cursor.fetchone()
        qry_q = f"SELECT user_id from user_detail where user_email = '{email_field}'"
        cursor.execute(qry_q)
        user_id = cursor.fetchone()
        qry_u = f"SELECT attempt from user_result where quiz_id = '{quiz_id[0]}' and user_id = '{user_id[0]}' "
        cursor.execute(qry_u)
        user_attempt = cursor.fetchall()
        #num_of_attempt = cursor.rowcount
        #print(num_of_attempt)
        # print("user_attempt",user_attempt)
        u_attempt = len(user_attempt) + 1
        #print(quiz_id[0],user_id[0],u_attempt,score_field,total_field)
        sql2 = f"INSERT INTO user_result (user_id,quiz_id,attempt,score,total_score) VALUES ({user_id[0]}, {quiz_id[0]}, {u_attempt}, {score_field}, {total_field})"
        cursor.execute(sql2)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

ur_rows_data = None


def ur_result(u_name):
    global ur_rows_data
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_query = f"SELECT quiz_detail.quiz_id, quiz_detail.quiz_name, attempt, score, total_score from quiz_detail INNER JOIN user_result ON user_result.quiz_id = quiz_detail.quiz_id where user_id = (select user_id from user_detail where user_name = '{u_name}')"
        cursor = con.cursor()
        cursor.execute(sql_query)
        temp = cursor.fetchall()
        cursor.close()
        con.close()
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


def insert_into_user_data(ur_name, ur_gen, ur_email, ur_mobile, ur_city, ur_state, ur_country, ur_password):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_qry = f"INSERT INTO user_detail (user_name, user_gender, user_email, user_mobile, user_city, user_state, user_country, user_password) VALUES ('{ur_name}','{ur_gen}','{ur_email}',{ur_mobile},'{ur_city}','{ur_state}', '{ur_country}', '{ur_password}')"
        #vals = (qname_field, qdescrp_field, qtimelimit_field, qpermark_field)
        cursor = con.cursor()
        cursor.execute(sql_qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

###############################################################################
#Admin Window


def checkQName(quname):
    if(len(quname) >0):
        if (len(quname) > 4):
            return quname
        else:
            temp = "Quiz Name is Minimum 5 character"
    else:
        temp = "Empty Quiz Name"
    messagebox.showwarning("Warning", temp)
    return 0


aur_rows_data = None


def adm_user_result(quiz_name):
    global aur_rows_data
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_query = f"SELECT user_detail.user_id, user_detail.user_name, attempt, score, total_score from user_detail INNER JOIN user_result ON user_result.user_id = user_detail.user_id where quiz_id = (select quiz_id from quiz_detail where quiz_name = '{quiz_name}')"
        cursor = con.cursor()
        cursor.execute(sql_query)
        temp = cursor.fetchall()
        cursor.close()
        con.close()
        #print(temp)
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def upd_quiz(qz_timelmt,qz_ques_score,qz_attempt_ques,qz_ttl_ques,search_qname):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"UPDATE quiz_detail SET quiz_time_limit={qz_timelmt},quiz_per_qs_mark={qz_ques_score},quiz_attempt_qs={qz_attempt_ques},quiz_total_ques={qz_ttl_ques} where quiz_name='{search_qname}'"
        cursor.execute(qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def del_quiz(search_qname):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        # qry = f"DELETE from quiz_question INNER JOIN quiz_detail ON quiz_detail.quiz_id=quiz_question.quiz_id where quiz_detail.quiz_id=(SELECT quiz_id from quiz_detail where quiz_name='{search_qname}')"
        # cursor.execute(qry)
        qry2 = f"DELETE from quiz_detail where quiz_id=(select quiz_id from quiz_detail where quiz_name = '{search_qname}')"
        cursor.execute(qry2)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def load_quiz_name():
    global rows
    global num_of_rows
    fg_qname=[]
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"SELECT * from quiz_detail"
        cursor.execute(qry)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


def insert_into_data_quiz(qname_field, qtimelimit_field, qpermark_field,qz_attempt_ques, q_total_ques_field,sheet, admin_id_field):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_qry = f"INSERT INTO quiz_detail (quiz_name,quiz_time_limit,quiz_per_qs_mark,quiz_attempt_qs, quiz_total_ques, admin_id) VALUES ('{qname_field}', {qtimelimit_field}, {qpermark_field},{qz_attempt_ques}, {q_total_ques_field}, '{admin_id_field}')"
        cursor = con.cursor()
        cursor.execute(sql_qry)
        con.commit()
        qry = f"SELECT quiz_id from quiz_detail where quiz_name = '{qname_field}'"
        cursor.execute(qry)
        fg_qid = cursor.fetchone()
        sheet.cell_value(0, 0)
        for i in range(1, sheet.nrows):
            ques_val=sheet.cell_value(i, 1)
            opa_val=sheet.cell_value(i, 2)
            opb_val=sheet.cell_value(i, 3)
            opc_val=sheet.cell_value(i, 4)
            opd_val=sheet.cell_value(i, 5)
            answer_val=sheet.cell_value(i, 6)
            sql2 = f"INSERT INTO quiz_question (question, opa, opb, opc, opd, answer, quiz_id) VALUES ('{ques_val}', '{opa_val}', '{opb_val}', '{opc_val}', '{opd_val}', '{answer_val}', {fg_qid[0]})"
            cursor.execute(sql2)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, "Quiz Name Exists\n Please Try Another Name")
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

qdf_data = None


def qzname_detail_fetch(search_name):
    global qdf_data
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"SELECT * from quiz_detail where quiz_name='{search_name}'"
        cursor.execute(qry)
        temp = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


###############################################################
#Root Window

def adm_quiz_detail(adm_id):
    global aur_rows_data
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_query = f"SELECT quiz_detail.quiz_name,quiz_detail.quiz_time_limit,quiz_detail.quiz_per_qs_mark," \
                    f"quiz_detail.quiz_attempt_qs, admin_detail.admin_name from quiz_detail INNER JOIN admin_detail " \
                    f"ON quiz_detail.admin_id = admin_detail.admin_id where quiz_detail.admin_id ={adm_id}"
        cursor = con.cursor()
        cursor.execute(sql_query)
        temp = cursor.fetchall()
        cursor.close()
        con.close()
        #print(temp)
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully



def upd_admin_detail(adm_name, adm_gen, adm_email, adm_mob, search_id):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"UPDATE admin_detail SET admin_name='{adm_name}',admin_gender='{adm_gen}',admin_email='{adm_email}', admin_mobile='{adm_mob}' where admin_id='{search_id}'"
        cursor.execute(qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def del_admin(search_admin_id):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"DELETE from admin_detail where admin_id='{search_admin_id}'"
        cursor.execute(qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def admin_detail_fetch(search_id):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"SELECT * from admin_detail where admin_id='{search_id}'"
        cursor.execute(qry)
        temp = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = temp
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


def insert_into_admindata(admName_field, admGen_field, admEmail_field, admMob_field, admPasswd_field):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_qry = f"INSERT INTO admin_detail (admin_name,admin_gender,admin_email,admin_mobile,admin_password) VALUES ('{admName_field}', '{admGen_field}', '{admEmail_field}', '{admMob_field}', '{admPasswd_field}')"
        # vals = (qname_field, qdescrp_field, qtimelimit_field, qpermark_field)
        cursor = con.cursor()
        cursor.execute(sql_qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully

def load_admin_detail():
    global rows
    global num_of_rows
    fg_qname=[]
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        qry = f"SELECT * from admin_detail"
        cursor.execute(qry)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


def database_error(msgs, err):
    messagebox.showerror(msgs, err)
    return False


def checkName(name):
    if(len(name) >0):
        if (len(name) > 2):
            return name
        else:
            temp = "Name Minimum 3 character"
    else:
        temp = "Empty Name"
    messagebox.showwarning("Warning", temp)
    return 0

def  checkMob(mob):
    if (len(mob) > 0):
        if (mob.isnumeric()):
            if (len(mob) == 10):
                mob = int(mob)
                #print(mob, "S")
                return mob
            else:
                temp = "Mobile number not less than 10 digit"
        else:
            temp = "Mobile number only"
    else:
        temp = "Empty Mobile No."
    messagebox.showwarning("Warning", temp)
    return 0

def checkEmail(email):
    reg = '^[a-z]+(?:[\._]?[a-z0-9]+)*[@]\w+[.]\w{2,3}$'
    # email=input('Enter Email - ').strip()
    if (len(email) > 0):
        if (re.match(reg, email)):
            #print(email)
            return email
        else:
            temp = "Please Enter Valid Email"
    else:
        temp = "Please Enter Email"
    messagebox.showwarning("Warning", temp)
    return 0


def checkPassword(password, repassword):
    flag = 0
    if (len(password)) < 8:
        flag = -1
        messagebox.showinfo("Error", "password must be Minimum 8")
    elif (len(password)) > 7 or len(repassword) > 7:
        while True:
            if not re.search("[a-z]",password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0
                break
        if flag == -1:
            messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
        elif password != repassword:
            flag = -1
            messagebox.showinfo("Error","New and retype password are not some")
    if (flag == 0):
        return 1
    else:
        return 0

################################################################
#Login Check

def fetch_name(login_type_field, email_field):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        if login_type_field == "Admin":
            cursor.execute(f"SELECT admin_name,admin_id from admin_detail where admin_email='{email_field}'")

        elif login_type_field == "User":
            cursor.execute(f"SELECT user_name,user_id from user_detail where user_email='{email_field}'")

        temp = cursor.fetchone()
        #print(temp)
        con.commit()
        cursor.close()
        con.close()
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        database_error(msg, e)
    return temp


tempData = None
def login_check(login_type_field, email_enter_field):
    global tempData
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        cursor = con.cursor()
        if login_type_field == "Root" :             
            if(email_enter_field != "abhijeetraj22@gmail.com"):
                return None
            else:
                tempData = ("Raj@2209","Root")
                return tempData
                
        elif login_type_field == "Admin" :
            qry = f"SELECT admin_password from admin_detail where admin_email='{email_enter_field}'"

        elif login_type_field == "User":
            qry = f"SELECT user_password from user_detail where user_email='{email_enter_field}'"

        cursor.execute(qry)
        temp = cursor.fetchone()
        con.commit()
        cursor.close()
        con.close()
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        database_error(msg, e)
    return temp

##############################register ~~############################################



def insert_into_user_data(ur_name_txt, ur_gen_txt, ur_email_txt, ur_mobile_txt, ur_city_txt, ur_state_txt, ur_country_txt,ur_sec_ques_txt, ur_sec_ans_txt, ur_password_txt):
    try:
        con = sqlite3.connect('Quiz_System.db')
        # con = pymysql.connect(host="localhost",
        #                       user="root",
        #                       passwd="1234",
        #                       port=3306,
        #                       database="quizsystem")
        sql_qry = f"INSERT INTO user_detail (user_name, user_gender, user_email, user_mobile, user_city, user_state,user_country, user_password,user_sec_ques,user_sec_ans) VALUES ('{ur_name_txt}','{ur_gen_txt}','{ur_email_txt}',{ur_mobile_txt},'{ur_city_txt}','{ur_state_txt}', '{ur_country_txt}','{ur_password_txt}','{ur_sec_ques_txt}', '{ur_sec_ans_txt}')"
        cursor = con.cursor()
        cursor.execute(sql_qry)
        con.commit()
        cursor.close()
        con.close()
        has_loaded_successfully = True
    except sqlite3.InternalError as e:
        msg = "Internal Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.OperationalError as e:
        msg = "Operational Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.ProgrammingError as e:
        msg = "Programming Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.DataError as e:
        msg = "Data Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.IntegrityError as e:
        msg = "Integrity Error"
        has_loaded_successfully = database_error(msg, e)
    except sqlite3.NotSupportedError as e:
        msg = "NotSupported Error"
        has_loaded_successfully = database_error(msg, e)
    return has_loaded_successfully


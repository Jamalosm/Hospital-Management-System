import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="root",database="projectagj")
mycursor1=db.cursor()
mycursor1.execute("create table patient_details(p_name varchar(30),p_age varchar(30),p_problems varchar(30),p_phono varchar(30))")
mycursor1.execute("create table doctor_details(d_name varchar(30),d_age varchar(30),d_department varchar(30),d_phoneno varchar(30))")
mycursor1.execute("create table worker_details(w_name varchar(30),w_age varchar(30),w_workname varchar(30),w_phono varchar(30))")

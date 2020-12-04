import os
import re
import mysql.connector
from mysql.connector import Error
connection=mysql.connector.connect(host='localhost',
                                   database='atm',
                                   user='root',
                                   password='root')
acc=''

print("1.Register")
print("2.login")
print("enter 3 for register and 4 for login")
u=int(input("Enter your choice"))

if u==3:
    n = str(input("Enter name"))
    a1 = int(input("Enter account no"))
    p = int(input("Enter password"))
    mn = int(input("Enter amount:"))
    myname = n
    password = p
    acc=a1
    amo=mn
    val = (myname, password,acc,amo)
    sql = "INSERT INTO bank(my_name, pass_word,a_cc,a_mo) VALUES (%s, %s, %s, %s)"
    #print("sql",val)
    mycursor = connection.cursor()
    #mycursor.execute("CREATE TABLE IF NOT EXISTS bank(my_name VARCHAR(20),pass_word VARCHAR(20),a_cc VARCHAR(20),a_mo VARCHAR(20))")
    mycursor.execute(sql,val)
    connection.commit()

if u==4:
    a_c=int(input("Enter account no:"))
    #sql_select_Query = "select * from data"
    mycursor = connection.cursor()
    #mycursor.execute(sql_select_Query)
    #records = mycursor.fetchall()
    #v=(a_c)
    # sql1="""SELECT * FROM bank where a_cc = ('%s')"""
    # mycursor.execute(sql1,v)
    # records = mycursor.fetchone()
    # # print("sql1",mycursor.rowcount)
    #
    # print(records[0])
    mycursor.execute("""SELECT * from bank WHERE a_cc = '%s'""" % (a_c))
    mycursor.fetchone()
    #print(mycursor.rowcount)
    if mycursor.rowcount==1:
        pas=int(input("Enter the password:"))
        mycursor.execute("""SELECT * from bank WHERE pass_word = '%s'""" % (pas))
        mycursor.fetchone()
        if mycursor.rowcount==1:
            print("Welcome")
            while (1):
                print("Press 5 for transaction and 6 for exit")
                t1 = int(input("Enter your choice"))
                if t1 == 5:
                    print("Press 7 for withdrawal and 8 for deposite")
                    trans = int(input("Enter your choice"))
                    if trans == 7:
                        print("Enter amount for withdrawal")
                        w = int(input("Enter amount"))
                        mycursor.execute("""SELECT a_mo from bank WHERE pass_word = '%s'""" %(pas))
                        amo=mycursor.fetchone()
                        li=list(amo)
                        for i in li:
                            amou=int(i)
                        #amou=int(amo)
                        #print(amou)
                            amount = amou - w
                            print(amount)
                        up = ("UPDATE bank SET a_mo='%s' where a_cc='%s'"%(amount,a_c))
                        mycursor.execute(up)
                        connection.commit()
                    if trans == 8:
                        print("Enter amount for deposite")
                        d = int(input("Enter amount"))
                        mycursor.execute("""SELECT a_mo from bank WHERE pass_word = '%s'""" % (pas))
                        amo=mycursor.fetchone()
                        li=list(amo)
                        for i in li:
                            amou=int(i)
                        #amou = int(amo)
                        # print(amou)
                            amount = amou + d
                            print(amount)
                        up = ("UPDATE bank SET a_mo='%s' where a_cc='%s'" %(amount,a_c))
                        mycursor.execute(up)
                        connection.commit()
                if t1 == 6:
                    exit(0)
        if mycursor.rowcount==-1:
            print("Enter correct password")
    if mycursor.rowcount==-1:
        print("account not exist")


from tkinter import *
import os
import random
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="rishabh",
password="1234",
database="bank"
)
cur=mydb.cursor()
def delete2():
    window3.destroy()
def delete3():
    window4.destroy()
def delete4():
    window5.destroy()
def login_success():
    global window3
    window3=Toplevel(window)
    window3.title("WELCOME")
    window3.geometry("600x400")
    Label(window3,text="WELCOME TO YOUR ACCOUNT",font=("Arial","20","bold","italic")).pack()
    Label(window3,text="*********************************************************************************************************************").pack()
    f=open(userid,"r")
    lines=f.readlines()
    x=lines[2]
    n=lines[0]
    n=n.upper()
    balance=100000.00
    bal=str(balance)
    Label(window3,text="ACCOUNT NUMBER : "+x,font=("Arial","12","bold","italic"),width=100).pack()
    Label(window3,text="").pack()
    Label(window3,text="ACCOUNT HOLDER'S NAME : "+n,font=("Arial","12","bold","italic"),width=100).pack()
    Label(window3,text="").pack()
    Label(window3, text='STARTING ACCOUNT BALANCE : ' + bal, font=("Arial", "12", "bold", "italic"), width=100).pack()
def password_wrong():
    global window4
    window4=Toplevel(window)
    window4.title("LOGIN FAILED")
    window4.geometry("150x100")
    Label(window4,text="CHECK THE PASSWORD").pack()
    Button(window4,text="OK",command=delete3).pack()
def user_wrong():
    global window5
    window5=Toplevel(window)
    window5.title("CHECK USER")
    window5.geometry("150x100")
    Label(window5,text="USER NOT FOUND").pack()
    Button(window5,text="ok",command=delete4).pack()
def register_user():
    user_info=username.get()
    pwd_info=password.get()
    if(user_info=="" and pwd_info==""):
        Label(window1,text="PROVIDE A VALID INPUT",bg="black",fg="green").pack()
    else:

        file = open(user_info, "w")
        file.write(user_info + "\n")
        file.write(pwd_info + "\n")
        num=random.randint(10000,99999)
        num1=str(num)
        file.write(num1)
        file.close()
        cur.execute("insert into details values ('%s','%s','%s')"% (user_info,num1,pwd_info))
        mydb.commit()
        user_entry.delete(0, END)
        pwd_entry.delete(0, END)
        Label(window1, text="YOU ARE NOW A REGISTERED USER", fg="green", bg="black", font=("calibri", 12)).pack()
def login_verify():
    global userid
    username1=user_verify.get()
    password1=pwd_verify.get()
    userid =username1
    user_entry1.delete(0,END)
    pwd_entry1.delete(0,END)
    #list_of_files=os.listdir()
    cur.execute("select * from details where name='%s'" % username1)
    result = cur.fetchone()
    if(result==None):
        user_wrong()
    #if(result==None):
     #  user_wrong()
   # elif(username1 in result) and (password1 in result):
   #     login_success()
    #else:
     #   password_wrong()

    if (username1 in result):
        #file1=open(username1,"r")
        #verify=file1.read().splitlines()
        if (password1 in result):
            login_success()
        else:
            password_wrong()
    else:
        user_wrong()
def register():
    global window1
    window1 = Toplevel(window)
    window1.title("REGISTER")
    window1.geometry("600x400")
    window1.resizable(width=False, height=False)
    global username
    global password
    global user_entry
    global pwd_entry
    username=StringVar()
    password=StringVar()
    image3 =PhotoImage(file="C:\\Users\\Owner\\Downloads\\b.gif")
    l2 = Label(window1, image=image3)
    l2.image = image3
    l2.place(x=0, y=0, relwidth=1, relheight=1)
    Label(window1,text="").pack()
    Label(window1,text="").pack()
    Label(window1,text="ENTER DETAILS BELOW",font=("cursive",16,"bold")).pack()
    Label(window1,text="").pack()
    Label(window1,text="USERNAME",bg="green",fg="black",font=("Arial",12,"bold","italic")).pack()
    Label(window1,text="NOTE:ACCOUNT HOLDER's NAME SHOULD BE THE USERNAME",font=("times new",6),bg="red").pack()
    user_entry=Entry(window1,textvariable=username)
    user_entry.pack()
    Label(window1,text="").pack()
    Label(window1,text="PASSWORD",bg="green",fg="black",font=("Arial",12,"bold","italic")).pack()
    Label(window1,text="").pack()
    pwd_entry=Entry(window1,textvariable=password)
    pwd_entry.pack()
    Label(window1,text="").pack()
    Button(window1,text="REGISTER",command=register_user,width="8",font=("Arial",10,"italic","bold"),bg="green",fg="black").pack()
def login():
    global window2
    window2=Toplevel(window)
    window2.geometry("600x400")
    window2.title("LOGIN")
    window2.configure(bg="black")
    window2.resizable(width=False,height=False)
    global user_verify
    global pwd_verify
    user_verify = StringVar()
    pwd_verify = StringVar()
    global user_entry1
    global pwd_entry1
    image2 = PhotoImage(file="C:\\Users\\Owner\\Downloads\\123.png")
    l1 = Label(window2, image=image2)
    l1.image=image2
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    Label(window2,text="USERNAME",bg='royalblue2',fg='black',font=("ARIAL",16,"bold","italic")).pack()
    Label(window2,text="").pack()
    user_entry1=Entry(window2,textvariable= user_verify)
    user_entry1.pack()
    Label(window2, text="").pack()
    Label(window2,text="PASSWORD",bg='royalblue2',fg='black',font=("ARIAL",16,"bold","italic")).pack()
    Label(window2, text="").pack()
    pwd_entry1=Entry(window2,textvariable=pwd_verify)
    pwd_entry1.pack()
    Label(window2, text="").pack()
    button2=Button(window2,width="8",text="LOGIN",command=login_verify,relief='raised',bg='royalblue3',fg='black',font=("ARIAL",16,"bold","italic")).pack()
window=Tk()
window.geometry("600x400")
window.title("WELCOME")
image1=PhotoImage(file="C:\\Users\\Owner\\Downloads\\234.png")
l=Label(window,image=image1)
l.place(x=0,y=0,relwidth=1,relheight=1)
Label(window,text="").pack()
Label(window,text="").pack()
Label(window,text="").pack()
label1=Label(window,width=20,text="MOBILE BANKING",bg="linen",pady=4,font=("arial",16,"bold")).pack()
Label(window,text="").pack()
button1=Button(window,text="EXISTING USER",activebackground="red",font=("arial",10,"bold"),relief='raised',bg='tan1',fg='white',command=login).pack()
Label(window,text="").pack()
button2=Button(window,text="NEW USER",activebackground="red",relief='raised',font=("arial",10,"bold"),bg='tan3',fg='white',command=register).pack()
mydb.commit()
window.resizable(width=False,height=False)
window.mainloop()
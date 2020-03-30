from Tkinter import *
import cv2
import mysql.connector as con
window = Tk()

db = con.connect(host="localhost",user="root",password="root",database="test")
c2 = db.cursor()
def display():
    window5.destroy()
    global window12,Ac
    window12 = Toplevel()
    window12.title("Menu")
    window12.configure(background = "green3")
    window12.geometry('600x400')
    Label(window12,text="Enter the Account number ",bg="green3").pack()
    Ac = Entry(window12,show="",bg="Light cyan")
    Ac.pack()
    Label(window12,text="",bg="green3").pack() 
    Label(window12,text="",bg="green3").pack() 
    Button(window12,text="Submit",width=20,height=2,command= display1).pack()
    window12.mainloop()
def display1():
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    ab = Ac.get()
    q18="select * from transfer where from_user=%s"
    g11 = [ab]
    c2.execute(q18,g11)
    h1 = c2.fetchall()
    window12.destroy()
    global window13
    window13 = Toplevel()
    window13.title("Menu")
    window13.configure(background = "green3")
    window13.geometry('600x400')
    Label(window13,text="SR.No. from  To  Type  Balance",bg="green3").pack()
    for x in h1:
        l = x
        Label(window13,text=l,bg="green3").pack()
    
    
##        print "from:",x[1]
##        print "to:",x[2]
##        print "Type:",x[3]
##        print "Amount:",x[4]
##        print "\n"    
def transaction():
    window5.destroy()
    global window9,Acc
    window9 = Toplevel()
    window9.title("Menu")
    window9.configure(background = "green3")
    window9.geometry('600x400')
    Label(window9,text="Enter the Account number ",bg="green3").pack()
    Acc = Entry(window9,show="",bg="Light cyan")
    Acc.pack()
    Label(window9,text="",bg="green3").pack() 
    Button(window9,text="Submit",width=20,height=3,command= trans).pack()
    window9.mainloop()
def trans():
    global window10,cost
    window10 = Toplevel()
    window10.title("Menu")
    window10.configure(background = "green3")
    window10.geometry('600x400')
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    Label(window10,text="Enter the Money to transfer",bg="green3").pack()
    cost = Entry(window10,show="",bg="Light cyan")
    cost.pack()
    Label(window10,text="",bg="green3").pack() 
    Button(window10,text="Submit",width=20,height=3,command= tran).pack()
    window9.mainloop()
def tran():
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    global v5
    v5=[a]
    print(v5)
    mone = cost.get()
    Acco = Acc.get()
    q6 = "select Balance from register where username=%s"
    c2.execute(q6,v5)
    b4 = c2.fetchone()
    amount = b4[0]
    q7= "select Balance from register where username=%s"
    s = [Acco]
    c2.execute(q7,s)
    a2 = c2.fetchone()
    print(a2[0])
    if(a2!=None):
        if(amount!=0):
            q8 = "update register set Balance=%s where username=%s"
            total2 = int(a2[0]) + int(mone)
            cost2 = [total2,Acco]
            c2.execute(q8,cost2)
            db.commit()
            total3 = int(b4[0])-int(mone)
            cost3 = [total3,a]
            c2.execute(q8,cost3)
            db.commit()
            q9 = "insert into transfer values(%s,%s,%s,%s,%s)"
            val1 = [0,a,Acco,"Debit",mone]
            c2.execute(q9,val1)
            db.commit()
            q9 = "insert into transfer values(%s,%s,%s,%s,%s)"
            val1 = [0,Acco,a,"credit",mone]
            c2.execute(q9,val1)
            db.commit()
        else:
            global window11
            window11 = Toplevel()
            window11.title("Menu")
            window11.configure(background = "green3")
            window11.geometry('600x400')
            Label(window10,text="Account Number not present!",bg="green3").pack   
def Add_Money():
    window5.destroy()
    global window7,Amount
    window7 = Toplevel()
    window7.title("Menu")
    window7.configure(background = "green3")
    window7.geometry('600x400')
    Label(window7,text="Enter the amount to Add",bg="green3").pack()
    Amount = Entry(window7,show="",bg="Light cyan")
    Amount.pack()
    Label(window7,text="",bg="green3").pack() 
    Button(window7,text="Submit",width=20,height=3,command= Add).pack()
    window7.mainloop()
def Add():
    global v
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    am=Amount.get()
    v=[a]
    q3 = "select Balance from register where username=%s"
    c2.execute(q3,v)
    b1 = c2.fetchone()
    total = int(b1[0]) + int(am)
    e = int(total)
    q3="update register set Balance=%s where username=%s"
    v1=[e,a]
    c2.execute(q3,v1)
    db.commit()
def Logindb():
    global b2,c2,a
    import mysql.connector as con
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    a = username.get()
    b = password.get()
    q1 = "select username,password from register where username=%s and password=%s"
    values = [a,b]
    c2.execute(q1,values)
    b2 = c2.fetchone()
    print(b2)
    if(b2!=None):
        global window5,window2
        window3.destroy()
        window5 = Toplevel()
        window5.title("Menu")
        window5.configure(background = "green3")
        window5.geometry('600x400')
        Label(window5,text="***Welcome to Menu****",bg="green3",font=('arial',20)).pack()
        Label(window5,text="",bg="green3").pack()
        Label(window5,text="",bg="green3").pack()
        Button(window5,text="Add Money",command=Add_Money,width=20,height=3).pack()
        Label(window5,text="",bg="green3").pack()
        Button(window5,text="Transactions",command=transaction,width=20,height=3).pack()
        Label(window5,text="",bg="green3").pack()
        Button(window5,text="Passbook",command=display,width=20,height=3 ).pack()
        Label(window5,text="",bg="green3").pack()
        Button(window5,text="Back",width=20,height=3,command= Exit).pack()
        window.mainloop()
    else:
        global window6
        window6 = Toplevel()
        window6.title("Wrong")
        window6.geometry('300x200')
        window6.configure(background = "green3")
        Label(window6,text="Invalid username and password!",bg="green3").pack()
    
def Register1():
    import mysql.connector as con
    db = con.connect(host="localhost",user="root",password="root",database="test")
    c2 = db.cursor()
    l = []
    q = "insert into register values(%s,%s,%s,%s,%s,%s)"
    a = 0
    l.append(a)
    name_st=name.get()
    l.append(name_st)
    email_st=email.get()
    l.append(email_st)
    user = username1.get()
    l.append(user)
    passw = password1.get()
    l.append(passw)
    a = 0
    l.append(a)
    c2.execute(q,l)
    db.commit()
    Label(window2,text="successfully register",bg="green3",font=('arial',20)).pack()
    
    
def Register():
    window.destroy()
    global window2,name,email,username1,password1
    window2 = Toplevel()
    window2.title("Register")
    window2.geometry('500x300')
    window2.configure(background = "green3")
    Label(window2,text="Welcome to Register",bg="green3",font=('arial',20)).pack()
    Label(window2,text="",bg="green3").pack()
    Label(window2,text="",bg="green3").pack()
    Label(window2,text="Name",bg="green3").pack()
    name = Entry(window2,show="",bg="Light cyan")
    name.pack()
    Label(window2,text="Email ID",bg="green3").pack()
    email = Entry(window2,bg="Light cyan")
    email.pack()
    Label(window2,text="Account Number",bg="green3").pack()
    username1 = Entry(window2,bg="Light cyan")
    username1.pack()
    Label(window2,text="Password",bg="green3").pack()
    password1 = Entry(window2,show="*",bg="Light cyan")
    password1.pack()
    Label(window2,bg="green3").pack()
    Button(window2,text="Register",command= Register1,width=20,height=2).pack()
    window2.mainloop()
def Login():
    global window3,username,password
    window3 = Toplevel()
    window3.title("Login")
    window3.geometry('550x300')
    window3.configure(background = "green3")
    Label(window3,text="***Welcome to Login***",bg="green3",font=('arial',30)).pack()
    Label(window3,text="",bg="green3").pack()
    Label(window3,bg="green3").pack()
    Label(window3,text="Account Number",bg="green3").pack()
    username = Entry(window3,show="",bg="Light cyan")
    username.pack()
    Label(window3,text="Password",bg="green3").pack()
    password = Entry(window3,show="*",bg="Light cyan")
    password.pack()
    Label(window3,text="",bg="green3").pack()
    Button(window3,text="Login",command=Logindb,width=20,height=2).pack()
    window3.mainloop()
def Exit():
    window.destroy()
    
window.title("Main Page")
window.geometry('2400x1000')
window.configure(background = "green3")
c = Canvas(width=500,height=300)
a = PhotoImage(file='giphy.gif')
image=c.create_image(600,10,anchor=NE,image=a)
c.pack()
Label(window,text="***Welcome to Bank of Maharastra****",bg="green3",font=('arial',20)).pack()
Label(window,text="",bg="green3").pack()
Label(window,text="",bg="green3").pack()
Button(window,text="Register",width=20,height=3,command=Register).pack()
Label(window,text="",bg="green3").pack() 
Button(window,text="Login",width=20,height=3,command= Login).pack()
Label(window,text="",bg="green3").pack()
Button(window,text="Exit",width=20,height=3,command= Exit).pack()
window.mainloop()


    
    


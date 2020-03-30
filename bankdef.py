import mysql.connector as con
db = con.connect(host="localhost",user="root",password="root",database="demo")
c1 = db.cursor()
q = "insert into account_login values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
login = []
ch =0
monee = []
def register():
        h = 0
        login.append(h)
        a = input("Enter the Account number:")
        login.append(a)
        b = input("Enter the age:")
        login.append(b)
        d = input("Enter the adhar number:")
        login.append(d)
        m = raw_input("Enter the type of account:")
        login.append(m)
        e = input("Enter the mobile number:")
        login.append(e)
        h = raw_input("Enter the address :")
        login.append(h)
        i = raw_input("Enter the email id:")
        login.append(i)
        j = raw_input("Enter the password:")
        login.append(j)
        k = raw_input("Enter the full name:")
        login.append(k)
        l = 0
        login.append(l)
        c1.execute(q,login)
        db.commit()
        print "Register success"
def login():
        b = []
        ul = []
        print "...Welcome to login..."
        x = raw_input("Enter the Account number:")
        y = raw_input("Enter the password:")
        q1 = "select acc,Account_number from account_login where Account_number=%s and password=%s"
        values = [x,y]
        c1.execute(q1,values)
        b2 = c1.fetchone()
        if(b2!=None):
            print "......login succesfully......"
            while(1):
                print "1.ADD money"
                print "2.Tranfer money"
                print "3.Passbook"
                print "4.Exit"
                c =input("Enter your choice:")
                if(c==1):
                    money = input("Enter the money you are add: ")
                    aid=b2[0]
                    q2 = "select Balance from account_login where Account_number='"+x+"'"
                    c1.execute(q2)
                    b1=c1.fetchone()
                    total = b1[0]+money
                    q3="update account_login set Balance=%s where Account_number='"+x+"'"
                    amt=[total]
                    c1.execute(q3,amt)
                    db.commit()
                if(c==2):
                    q4="select Balance from account_login where Account_number='"+x+"'"
                    c1.execute(q4)
                    a1 = c1.fetchone()
                    total = a1[0]
                    ne = input("Enter the account number to transfer:")
                    q5="select Balance from account_login where Account_number=%s"
                    s = [ne]
                    c1.execute(q5,s)
                    a2 = c1.fetchone()
                    if(a2!=None):
                        if(total!=0):
                            q6 = "update account_login set Balance=%s where Account_number=%s"
                            k = input("Enter the amount to transfer:")
                            total2 = a2[0]+k
                            cost2=[total2,ne]
                            c1.execute(q6,cost2)
                            db.commit()
                            total = total-k
                            cost3=[total,b2[0]]
                            c1.execute(q6,cost3)
                            db.commit()
                            q7 = "insert into transcation values(%s,%s,%s,%s)"
                            val1 = [0,b2[1],ne,k]
                            c1.execute(q7,val1)
                            db.commit()
                            q8 = "insert into transcation values(%s,%s,%s,%s)"
                            val2 = [0,ne,b2[1],k]
                            c1.execute(q8,val2)
                            db.commit()
                        else:
                            print "account no balance"
    
                    else:
                        print "invalid acc number!"
def passbook():
                    fm=input("enter account num:")
                    q11="select *from transcation where frome=%s"
                    g11=[fm]
                    c1.execute(q11,g11)
                    h1=c1.fetchall()
                    print h1
                    for x in h1:
                        print "from:",x[1]
                        print "to:",x[2]
                        print "amount:",x[3]
                        print "\n"
while(1):
    print "...Welcome to login...."
    print "1.Login"
    print "2.Register"
    print "3.Exit"
    ch = input("Enter your chice:")
    if(ch==1):
        login()
    elif(ch==2):
        register()
    elif(ch==3):
        passbook()
        
    
    
    
    

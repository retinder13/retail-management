
import datetime
from employee import employee
from employee2 import employee2
import sqlite3
conn=sqlite3.connect(':memory:')
conn.execute('''CREATE TABLE ORDER_RECIVED(ID INTEGER,PRODUCT_NAME TEXT,QUANTITY INTEGER,PRICE INTEGER,EXP_DATE DATE)''')

c=conn.cursor()

username='123'
pass1 ='123'
h=1
while(h<=1):
    h=h+1
    user=str(input("User name:-"))


    if(user==username):
        pass2=str(input("Password:-"))
        if pass2==pass1:
            g = 1
            while (g <= 1):
                print("welcome")
                print("1:Reciving order")
                print("2:billing")
                print("3:log out")
                a=int(input("enter endex no of process you want to do"))
                if a==1:
                    d=1
                    while(d<=1):
                        print("RECIVING ORDER")
                        print("1:Adding items")
                        print("2:view items")
                        print("3:Back")
                        b = int(input("enter endex no of process you want to do"))
                        if b==1:

                            no=int(input("enter no of diffrent products"))
                            y=1
                            while(y<=no):

                                proid=int(input("enter product ID:-"))
                                pname=input("enter product name:-")
                                quan = int(input("enter quantity of product:-"))
                                exy = int(input("enter expiry year:-"))
                                exm = int(input("enter expiry month:-"))
                                exd = int(input("enter expiry day:-"))
                                x = datetime.datetime(exy,exm,exd)
                                pr=int(input("enter price:-"))
                                emp=employee(proid,pname,quan,pr,x)
                                c.execute('INSERT INTO ORDER_RECIVED(ID,PRODUCT_NAME,QUANTITY,PRICE,EXP_DATE) VALUES(:first,:second,:third,:fourth,:fifth)',{'first':emp.first,'second':emp.second,'third':emp.third,'fourth':emp.fourth,'fifth':emp.fifth})


                                y=y+1


                        elif b==2:
                            c.execute("SELECT * FROM ORDER_RECIVED")
                            for row in c.fetchall():
                                print(row)

                        elif b==3:
                            d=d+1

                if a==2:
                    print("Items avilable")
                    c.execute("SELECT * FROM ORDER_RECIVED")
                    for row in c.fetchall():
                        print(row)
                    no1 = int(input("enter no of diffrent products you want to buy:-"))
                    z=1
                    summ=0
                    while (z <= no1):
                        cart=int(input("enter ID of product you want to buy:-"))
                        qut=int(input("enter quantity:-"))
                        emp2 = employee2(cart, qut)
                        c.execute("SELECT QUANTITY FROM ORDER_RECIVED WHERE ID=:first",{'first':emp2.first})
                        mat=c.fetchall()
                        c.execute("UPDATE ORDER_RECIVED SET QUANTITY=QUANTITY-:second WHERE ID=:first",{'second':emp2.second,'first':emp2.first})


                        z=z+1
                if a==3:
                    g=g+1
                    h=h-1

else:
    print("error")











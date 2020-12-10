from tkinter import *
import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()
c.execute('''CREATE TABLE COFFEE(latte INT,espresso INT,cappucino INT);''')
c.execute('''SELECT * FROM COFFEE''')
records=c.fetchall()
for r in records:
    print("Number of Latte Bought:",r[0])
    print("Number of Espresso Bought:",r[1])
    print("Number of Cappucino Bought:",r[2])
conn.commit()
c.close()

class CoffeeMaker(Tk):
    l=0
    e=0
    c=0
    water=3000
    milk=4000
    coffee=7000
    money=0
    def main(self):
        def getinput():
            x=E1.get()
            if(x=="off"):
                top.destroy()
                c.execute('''INSERT INTO COFFEE VALUES(?,?,?)''',(self.l,self.e,self.c))
                return
            if(x=="report"):
                frame.destroy()
                texti.destroy()
                self.report(x)
                return
            frame.destroy()
            texti.destroy()
            self.resources(x)
        texti = Text(top)
        texti.pack()
        texti.insert(INSERT,"MENU CARD\nLatte:$2.50\nEspresso:$3.50\nCappucino:$4.50")
        frame=Frame(top)
        frame.pack()
        L1 = Label(frame, text="What would you like?(espresso/latte/cappucino):")
        L1.pack()
        E1 = Entry(frame)
        E1.pack()
        b=Button(frame,text="Submit",command=getinput)
        b.pack()
        mainloop()
    def __init__(self,value):
        self.value=value
        b1=Button(top,text="Go to Main Menu",command=self.main())
        b1.pack()
    def clean(self,b1):
        b1.pack_forget()
    def report(self,value):
        te=Text(top)
        te.pack()
        te.insert(INSERT,"REPORT\nWater:{}ml\nMilk:{}ml\nCoffee:{}g\nMoney:${}".format(self.water,self.milk,self.coffee,self.money))
        b1=Button(top,text="Go to Main Menu",command=lambda:te.pack_forget()|self.clean(b1)&self.main())
        b1.pack()
    def makecoffee(self,value,textt):
        textt.destroy()
        texttt=Text(top)
        texttt.pack()
        if(value=="latte"):
            self.water=self.water-50
            self.milk=self.milk-70
            self.coffee=self.coffee-50
            self.money=self.money+2.50
            texttt.insert(INSERT,"Here is your latte. Enjoy!")
            self.l=self.l+1
        elif(value=="espresso"):
            self.water=self.water-100
            self.milk=self.milk-10
            self.coffee=self.coffee-100
            self.money=self.money+3.50
            texttt.insert(INSERT,"Here is your espresso. Enjoy!")
            self.e=self.e+1
        else:
            self.water=self.water-70
            self.milk=self.milk-50
            self.coffee=self.coffee-70
            self.money=self.money+4.50
            texttt.insert(INSERT,"Here is your cappucino. Enjoy!")
            self.c=self.c+1
        b1=Button(top,text="Go to Main Menu",command=lambda:texttt.pack_forget()|self.clean(b1) & self.main())
        b1.pack()
    def transac(self,value,amount):
        textt=Text(top)
        textt.pack()
        if(value=="latte"):
            if(amount<2.50):
                textt.insert(INSERT,"Sorry that's not enough money. Money refunded.")
                b1=Button(top,text="Go to Main Menu",command=lambda:textt.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(amount>2.50):
                textt.insert(INSERT,"Here is ${} dollars in change.".format(round(amount-2.50,2)))
                b1=Button(top,text="Make Coffee",command=lambda:textt.pack_forget()|self.clean(b1) & self.makecoffee(value,textt))
                b1.pack()
            else:
                self.makecoffee(value,textt)
        elif(value=="espresso"):
            if(amount<3.50):
                textt.insert(INSERT,"Sorry that's not enough money. Money refunded.")
                b1=Button(top,text="Go to Main Menu",command=lambda:textt.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(amount>3.50):
                textt.insert(INSERT,"Here is ${} dollars in change.".format(round(amount-3.50,2)))
                b1=Button(top,text="Make Coffee",command=lambda:textt.pack_forget()|self.clean(b1) & self.makecoffee(value,textt))
                b1.pack()
            else:
               self.makecoffee(value)
        else:
            if(amount<4.50):
                textt.insert(INSERT,"Sorry that's not enough money. Money refunded.")
                b1=Button(top,text="Go to Main Menu",command=lambda:textt.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(amount>4.50):
                textt.insert(INSERT,"Here is ${}dollars in change.".format(round(amount-4.50,2)))
                b1=Button(top,text="Make Coffee",command=lambda:textt.pack_forget()|self.clean(b1) & self.makecoffee(value,textt))
                b1.pack()
            else:
                self.makecoffee(value)
            
    def coins(self,value):
        quarters=0.25
        dimes=0.10
        nickles=0.05
        pennies=0.01
        def getinputs():
            q=E2.get()
            d=E3.get()
            n=E4.get()
            p=E5.get()
            q=int(q)
            d=int(d)
            n=int(n)
            p=int(p)
            amount=(q*quarters)+(d*dimes)+(n*nickles)+(p*pennies)
            f.destroy()
            t.destroy()
            self.transac(value,amount)
        t=Text(top)
        t.pack()
        t.insert(INSERT,"\nInsert coins!")
        f=Frame(top)
        f.pack()
        L2 = Label(f, text="Enter number of quarters:")
        L2.pack()
        E2 = Entry(f)
        E2.pack()
        L3 = Label(f, text="Enter number of dimes:")
        L3.pack()
        E3 = Entry(f)
        E3.pack()
        L4 = Label(f, text="Enter number of nickles:")
        L4.pack()
        E4 = Entry(f)
        E4.pack()
        L5 = Label(f, text="Enter number of pennies:")
        L5.pack()
        E5 = Entry(f)
        E5.pack()
        b=Button(f,text="Submit",command=getinputs)
        b.pack()
    def resources(self,value):
        text=Text(top)
        if(value=="latte"):
            if(self.water<50):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough water!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.milk<70):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough milk!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.coffee<50):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough coffee!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            else:
                self.coins(value)
        elif(value=="espresso"):
            if(self.water<100):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough water!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.milk<10):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough milk!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.coffee<100):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough coffee!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            else:
                self.coins(value)
        else:
            if(self.water<70):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough water!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.milk<50):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough milk!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            elif(self.coffee<70):
                text.pack()
                text.insert(INSERT,"Sorry there is not enough coffee!")
                b1=Button(top,text="Go to Main Menu",command=lambda:text.pack_forget()|self.clean(b1) & self.main())
                b1.pack()
            else:
                self.coins(value)
                   
x="on"
top=Tk()
s=CoffeeMaker(x)

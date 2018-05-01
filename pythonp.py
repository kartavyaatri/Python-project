from tkinter import *

root=Tk()
root.configure(background='#32BEA6')
root.geometry("730x550")
root.title("Car Management System")


def Add_Record():
    f=open('kartavya.txt','a')
    CAR_NO=s1.get()
    CAR_NAME=s2.get()
    QUANTITY=s3.get()
    PRICE=s4.get()
    MAN_DATE=s5.get()
    EXPIRY=s6.get()
    BUYER=s7.get()
    DEMAND=s8.get()
    if(CAR_NO=='' or CAR_NAME=='' or QUANTITY=='' or PRICE=='' or MAN_DATE=='' or EXPIRY==''or BUYER==''or DEMAND==''):
        print("Details can't be empty!")
        exit()
    f.writelines(CAR_NO.ljust(20)+CAR_NAME.ljust(20)+QUANTITY.ljust(20)+PRICE.ljust(20)+MAN_DATE.ljust(20)+EXPIRY.ljust(20)+BUYER.ljust(20)+DEMAND.ljust(20)+"\n")
    print("The CAR has been registered !!")
    print("CAR id = ",CAR_NO)
    print("Customer id = ",CAR_NO)
    print("Quantity = ",CAR_NO)
    print("Price = ",CAR_NAME)
    print("DATE OF BOOKING= ",MAN_DATE)
    print("DATE OF DELIVERY = ",EXPIRY)
    print("Buyer = ",BUYER)
    print("Demand = ",DEMAND,"\n")
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    s6.set("")
    s7.set("")
    s8.set("")
    f.close()


def update():
    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=s5.get()
    x6=s6.get()
    x7=s7.get()
    x8=s8.get()
    f=open("kartavya.txt",'r')
    k=f.readlines()
    f.close()
    f=open("kartavya.txt",'w')
    z=0
    for i in k:
        j=i.split()
        if(j[0]!=x1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(20)+j[5].ljust(20)+j[6].ljust(20)+j[7].ljust(20)+"\n")
        else:
            f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(20)+x6.ljust(20)+x7.ljust(20)+x8.ljust(20)+"\n")
            z=1
            print("\nThe CAR has successfully been updated!\n")
            print("Updated CAR id = ",x1)
            print("Updated Customer id = ",x2)
            print("Updated Quantity = ",x3)
            print("Updated Price = ",x4)
            print("Updated DATE OF BOOKING= ",x5)
            print("Updated DATE OF DELIVERY = ",x6)
            print("Updated Buyer = ",x7)
            print("Updated Demand = ",x8,"\n")
            print
    if(z==0):
        print("\nThere was an unidentified error, the CAR could not be updated!\n")


def SEARCH_FILE(widget):
    l4.config(fg="black")
    l5.config(fg="black")
    l6.config(fg="black")
    l7.config(fg="black")
    l8.config(fg="black")
    l9.config(fg="black")
    l10.config(text="Enter the details of car to be searched!",fg="white")
    e4.config(bg="black")


def SEARCH():
    k=s1.get()
    f=open('kartavya.txt','r')
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            print("ID FOUND")
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
            s6.set(j[5])
            s7.set(j[6])
            s8.set(j[7])
        else:
            print("CAR ID NOT FOUND")
            s1.set('')
            s2.set('')
            s3.set('')
            s4.set('')
            s5.set('')
            s6.set('')
            s7.set('')
            s8.set('')

    f.close()


def delrec():
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get()]
    f=open("kartavya.txt","r")
    lines=f.readlines()
    print(lines)
    print(k)
    f.close()
    f=open("kartavya.txt","w")
    for i in lines:
        m=i.split()
        print(m)
        if(m!=k):
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+m[5].ljust(20)+m[6].ljust(20)+m[7].ljust(20)+"\n")
    s1.set('')
    s2.set('')
    s3.set('')
    s4.set('')
    s5.set('')
    s6.set('')
    s7.set('')
    s8.set('')
    f.close()


c1=0
def get_previous():
    global c1
    f=open("kartavya.txt",'r')
    ctr= sum(1 for line in open("kartavya.txt"))-1
    print(ctr)
    k=f.readlines()[c1]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    c1=c1-1
    if(c1==-1):
        c1=ctr
    f.close()


def sort_quant():
     print("Sort by quantity")


def sort_price():
     print("Sort by price")


def get_all():
     print("Get All")


def clear():
     f=open("kartavya.txt","r+")
     f.truncate()


l1=Label(root,text="Car Inventry Management tool",font=('Ariel',24,'bold'),bg='#32BEA6'  )
l2=Label(root,text="CAR id",font=('Ariel',15,'bold'),bg='#32BEA6'  )
l3=Label(root,text="Customer id",font=('Ariel',15,'bold'),bg='#32BEA6'  )
l4=Label(root,text="QUANTITY",font=('Ariel',15,'bold') ,bg='#32BEA6' )
l5=Label(root,text="PRICE",font=('Ariel',15,'bold') ,bg='#32BEA6' )
l6=Label(root,text="MANUFACTURE DATE",font=('Ariel',15,'bold'),bg='#32BEA6'  )
l7=Label(root,text="DATE OF DELIVERY",font=('Ariel',15,'bold'),bg='#32BEA6'  )
l8=Label(root,text="PURCHASED BY",font=('Ariel',15,'bold') ,bg='#32BEA6' )
l9=Label(root,text="DEMAND",font=('Ariel',15,'bold') ,bg='#32BEA6' )
l10=Label(root,text="",font=('Ariel',15,'bold'),fg="black",bg='#32BEA6')

l1.place(x=100,y=10)
l2.place(x=10,y=120)
l3.place(x=400,y=120)
l4.place(x=10,y=180)
l5.place(x=400,y=180)
l6.place(x=10,y=240)
l7.place(x=400,y=240)
l8.place(x=10,y=300)
l9.place(x=400,y=300)
l10.place(x=600,y=400)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()

e2=Entry(root,textvariable=s1,bg="white")
e3=Entry(root,textvariable=s2,bg="white")
e4=Entry(root,textvariable=s3,bg="white")
e5=Entry(root,textvariable=s4,bg="white")
e6=Entry(root,textvariable=s5,bg="white")
e7=Entry(root,textvariable=s6,bg="white")
e8=Entry(root,textvariable=s7,bg="white")
e9=Entry(root,textvariable=s8,bg="white")

e2.place(x=240,y=125)
e3.place(x=590,y=125)
e4.place(x=240,y=185)
e5.place(x=590,y=185)
e6.place(x=240,y=245)
e7.place(x=590,y=245)
e8.place(x=240,y=305)
e9.place(x=590,y=305)

b1=Button(root,text="ADD CAR",bg="BROWN",font=('Ariel',10,'bold'),command=Add_Record,width=20).place(x=280,y=390)
b2=Button(root,text="UPDATE",bg="BROWN",font=('Ariel',10,'bold'),command=update,width=20).place(x=190,y=440)
b3=Button(root,text="SEARCH CAR",bg="BROWN",font=('Ariel',10,'bold'),command=SEARCH_FILE,width=20).place(x=370,y=440)
b4=Button(root,text="DELETE CAR",bg="BROWN",font=('Ariel',10,'bold'),command=delrec,width=20).place(x=550,y=440)
b5=Button(root,text="SHOW PREV REC",bg="BROWN",font=('Ariel',10,'bold'),command=get_previous,width=20).place(x=10,y=480)
b6=Button(root,text="SORT BY QUANTITY",bg="BROWN",font=('Ariel',10,'bold'),command=sort_quant,width=20).place(x=190,y=480)
b7=Button(root,text="SORT BY PRICE",bg="BROWN",font=('Ariel',10,'bold'),command=sort_price,width=20).place(x=370,y=480)
b8=Button(root,text="SHOW ALL",bg="BROWN",font=('Ariel',10,'bold'),command=get_all,width=20).place(x=550,y=480)
b9=Button(root,text="REMOVE ALL",bg="BROWN",font=('Ariel',10,'bold'),command=clear,width=20).place(x=280,y=520)
b10=Button(root,text="SEARCH",bg="BROWN",font=('Ariel',10,'bold'),command=SEARCH,width=20).place(x=10,y=440)


root.mainloop()


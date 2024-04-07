from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
# import pymysql
import config
import mysql.connector
import datetime
# Add your own database name and password here to reflect in the code
mypass= config.dbPass
mydatabase=config.db

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor(buffered=True)

# Enter Table Names here
eventTable = "event" #Book Table


allBid = [] #List To store all Book IDs

def add():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    notice = bookInfo1.get("1.0",'end-1c')
    updateStatus = "insert into "+eventTable+"(notice) values('"+notice+"')"
    try:
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success',"Notice Generated Successfully")
    except Exception as e:
        print(e)
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()
    
def addEvent(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Create Notice", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Notice : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Text(labelFrame)
    bookInfo1.place(relx=0.2,rely=0.1, relwidth=0.6, relheight=0.8)
    
    #Submit Button
    RenewBtn = Button(root,text="Create",bg='#d1ccc0', fg='black',command=add)
    RenewBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.58,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
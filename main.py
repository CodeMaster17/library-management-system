from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
# import pymysql
import config
import mysql.connector
from tkinter import messagebox,ttk
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ViewIssuedBooks import *
from ReturnBook import *
from AddEvent import addEvent
from DeleteEvent import deleteEventView

mypass= config.dbPass
mydatabase=config.db

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor(buffered=True)

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)


Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.18,rely=0.3, relwidth=0.35,relheight=0.065)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.18,rely=0.365, relwidth=0.35,relheight=0.065)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.18,rely=0.430, relwidth=0.35,relheight=0.065)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.18,rely=0.495, relwidth=0.35,relheight=0.065)
    
btn6 = Button(root,text="View Issued Books",bg='black', fg='white', command = viewIssuedBooks)
btn6.place(relx=0.18,rely=0.560, relwidth=0.35,relheight=0.065)

btn5 = Button(root,text="Return/Renew Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.18,rely=0.625, relwidth=0.35,relheight=0.065)

btn7 = Button(root,text="Add Notice",bg='black', fg='white', command = addEvent)
btn7.place(relx=0.18,rely=0.690, relwidth=0.35,relheight=0.065)

btn8 = Button(root,text="Delete Notice",bg='black', fg='white', command = deleteEventView)
btn8.place(relx=0.18,rely=0.755, relwidth=0.35,relheight=0.065)

labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.55,rely=0.3,relwidth=0.3,relheight=0.45)

def getNotice():
    for element in labelFrame.winfo_children():
        element.destroy()
    y = 0
    getBooks = f"select id,notice from event"
    Label(labelFrame, text="Notice",bg='black',fg='red').pack()
    separator = ttk.Separator(labelFrame, orient='horizontal')
    separator.pack(fill='x')
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text=f"({i[0]}) {i[1]}",bg='black',fg='white').pack()
            separator = ttk.Separator(labelFrame, orient='horizontal')
            separator.pack(fill='x')
    except Exception as e:
        print(e)
        messagebox.showinfo("Error","Fetch Failed")
btn9 = Button(root,text="Refresh",bg='black', fg='white', command=getNotice)
btn9.place(relx=0.55,rely=0.75, relwidth=0.3,relheight=0.065)
getNotice()
root.mainloop()

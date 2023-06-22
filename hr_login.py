from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
import mysql.connector






def procced():
    point = mysql.connector.connect(host = "localhost", user = "root", password = "anakha", database = "empdata3")
    main_cursor = point.cursor()
    command =" select * from admin_credential where user_id = %s and user_password = %s"
    values = (user_data.get(),password_data.get())
    main_cursor.execute(command,values)
    rel = main_cursor.fetchall()
    if rel:
        for i in rel:
            messagebox.showinfo("Success", "LOGIN SUCCESSFULL !!")
            r.destroy()
            import emp_reg
    else:
        # print("Invalid credentials")
        messagebox.showerror("Failed", "Username or password is incorrect")



def showit():
    if v.get() == 1:
        password_data.config(show = '')
    else:
        password_data.config(show='*')





r = Tk()

r.title("Employee Management System")
r.config(bg="grey")
r.geometry("1100x700")
r.resizable(False, False)


Label_frame = Frame(r,bg="firebrick", bd=5, relief="ridge")
Label_frame.place(x=1, y=1, width=1099, height=62)
main_label = Label(Label_frame, text="Employee Management System", bg="firebrick", fg="goldenrod",font=("arial", 22, "bold"))
main_label.pack(side="top")


img = (Image.open("Resource/workbench3.jpg"))
img2 = img.resize((1094,700))
img1 = ImageTk.PhotoImage(img2)


connectdb = Frame(r)
connectdb.grab_set()
connectdb.place(x = 0,y = 62,width = 1100,height= 900 )

connectdb.config(bg='DarkOrange1')

l1 = Label(connectdb,image= img1)
l1.pack(side="top")



frame = Frame(connectdb, bg = "grey97")
frame.place(x=296,y=220, width =500, height = 300)

imgs = (Image.open("Resource//user.png"))
imgs1 = imgs.resize((30,30))
imgs2 = ImageTk.PhotoImage(imgs1)

image = (Image.open("Resource//lock.png"))
image1 = image.resize((30,30))
image2 = ImageTk.PhotoImage(image1)
#----------------------------------------------------------------------------------------Labels:
user_root = Label(connectdb, text="Username", bg="grey97", font=("verdana", 12, "bold"),
                 borderwidth=3, width=10, anchor='e')
user_root.place(x=350, y=320)

login_img = Label(connectdb,image= imgs2, bg = "grey97")
login_img.place(x =320 ,y=310, width = 40, height = 40)

password = Label(connectdb, text="Password", bg="grey97", font=("verdana", 12, "bold"),
                      borderwidth=3, width=10, anchor='e')
password.place(x=350, y=380)

password_img = Label(connectdb,image= image2, bg = "grey97")
password_img.place(x =320 ,y=370, width = 40, height = 40)

#-----------------------------------------------------------------------------------------Entry:




user_data = Entry(connectdb, font=('Helvetica', 12, 'bold'),bg= "grey95", bd=3, width=20)
user_data.place(x=500, y=320)

password_data = Entry(connectdb, font=('Helvetica', 12, 'bold'),bg= "grey95", bd=3, width=20,show= "*")
password_data.place(x=500, y=380)

#-------------------------------------------------------------------------------------------------
v = IntVar()

show_pass = Checkbutton(connectdb,variable=v,bg="grey97",onvalue=1,offvalue=0, command=showit)
show_pass.place(x = 730, y = 380)

login_button = Button(connectdb, text="Login", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                           width=7,command=procced)
login_button.place(x=518, y=450)

r.mainloop()

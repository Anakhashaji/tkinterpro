from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
import mysql.connector
import time






def add_user():
    adding = Toplevel(master=connectd)
    adding.grab_set()
    adding.geometry('470x660')
    adding.title('Enter details')
    adding.config(bg='light blue')
    adding.resizable(False, False)

    user_name = Label(adding, text="Username", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    user_name.place(x=10, y=30)

    pass_word = Label(adding, text="Password", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                      borderwidth=3, width=11, anchor='w')
    pass_word.place(x=10, y=80)

    user_id = Label(adding, text="User ID", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    user_id.place(x=10, y=130)


    name = Label(adding, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    name.place(x=10, y=180)

    mobile_no = Label(adding, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    mobile_no.place(x=10, y=230)

    email = Label(adding, text="E-mail", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    email.place(x=10, y=280)

    address = Label(adding, text="Address", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                  borderwidth=3, width=11, anchor='w')
    address.place(x=10, y=330)

    gender = Label(adding, text="Gender", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    gender.place(x=10, y=380)

    salary = Label(adding, text="Salary", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')

    salary.place(x=10, y=430)

    dob = Label(adding, text="DOB", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                borderwidth=3, width=11, anchor='w')

    dob.place(x=10, y=480)

    department = Label(adding, text="Department", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                       borderwidth=3, width=11, anchor='w')

    department.place(x=10, y=530)

    positon = Label(adding, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')

    positon.place(x=10, y=580)

    user_name1 = StringVar()
    pass_word1 = StringVar()
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    salaryval = StringVar()
    dobval = StringVar()
    departmentval = StringVar()
    positionval = StringVar()
    user_val = StringVar()
    pass_val = StringVar()

    use_name_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=user_val, bd=3, width=18)
    use_name_enter.place(x=230, y=30)

    password_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=pass_val, bd=3, width=18)
    password_enter.place(x=230, y=80)

    user_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=idval, bd=3, width=18)
    user_enter.place(x=230, y=130)

    name_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=nameval, bd=3, width=18)
    name_enter.place(x=230, y=180)

    mobile_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=mobileval, bd=3, width=18)
    mobile_enter.place(x=230, y=230)

    email_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=emailval, bd=3, width=18)
    email_enter.place(x=230, y=280)

    address_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=addressval, bd=3, width=18)
    address_enter.place(x=230, y=330)

    gender_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=genderval, bd=3, width=18)
    gender_enter.place(x=230, y=380)

    salary_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=salaryval, bd=3, width=18)
    salary_enter.place(x=230, y=430)

    dob_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=dobval, bd=3, width=18)
    dob_enter.place(x=230, y=480)

    department_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=departmentval, bd=3, width=18)
    department_enter.place(x=230, y=530)

    position_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=positionval, bd=3, width=18)
    position_enter.place(x=230, y=580)


    def submitadd():


        user_name_is = use_name_enter.get()
        pass_word_is = password_enter.get()
        id = user_enter.get()  # getting data from entries...or entry lables
        name = name_enter.get()
        mobile = mobile_enter.get()
        email = email_enter.get()
        address = address_enter.get()
        gender = gender_enter.get()
        salary = salary_enter.get()
        dob = dob_enter.get()
        department = department_enter.get()
        position = position_enter.get()
        addedtime = time.strftime("%H:%M:%S")  # to get time
        addeddate = time.strftime("%d/%m/%Y")  # to get date

#----------------------------------------------------------------------------------------------------------------------
        try:
            point1 = mysql.connector.connect(host='localhost', user='root', password='anakha')
            console_p1 = point1.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again')
            return
        try:
            strr1 = 'create database empdata3'
            console_p1.execute(strr1)
            strr1 = 'use empdata3'
            console_p1.execute(strr1)
            strr1 = 'create table employeedata3(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),salary varchar(50),dob varchar(20),department varchar(30),position varchar(30),date varchar(50),time varchar(50))'
            console_p1.execute(strr1)
            strr1 = 'alter table employeedata3 modify column id int not null'
            console_p1.execute(strr1)
            strr1 = 'alter table employeedata3 modify column id int primary key'
            console_p1.execute(strr1)
            strr1 = 'create table login_credential2(user_name varchar(30),password varchar(20),user_id int)'
            console_p1.execute(strr1)
            strr1 = 'alter table login_credential2 modify column id int not null'
            console_p1.execute(strr1)
            strr1 = 'alter table login_credential2 modify column id int primary key'
            console_p1.execute(strr1)
            messagebox.showinfo('Notification',
                                'database created and now you are connected connected to the database ....')
        except:
            strr = 'use empdata3'
            console_p1.execute(strr)
        adding.destroy()



# ----------------------------------------------------------------------------------------------------------------------
        try:
            point1 = mysql.connector.connect(host = "localhost", user = "root", password = "anakha", database = "empdata3")
            console_p1 = point1.cursor()
            strr = 'insert into employeedata3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            console_p1.execute(strr, (id, name, mobile, email, address, gender, salary, dob, department, position, addeddate, addedtime))

            strr2 = 'insert into login_credential2 values(%s,%s,%s)'
            console_p1.execute(strr2,(user_name_is,pass_word_is,id))
            point1.commit()

            messagebox.showinfo("Success","Successfully added user details!")
            # clearing the entry form after adding details to database only if res==true

        except:

            try:
                #messagebox.showinfo('Notifications', 'Id Already Exist ...')
                strr2 = 'insert into login_credential2 values(%s,%s,%s) '
                console_p1.execute(strr2, (user_name_is, pass_word_is, id))
                point1.commit()

            except:
                    messagebox.showwarning("Warning", "Id already exist!")




        adding.destroy()




#--------------------------------------------------------------------------------Add button
    add_button = Button(adding,text = "ADD",relief="raised", bg="light grey", font=("verdana", 14, "bold"),
                width=7,command=submitadd)
    add_button.place(x = 170, y = 630)




e = Tk()
e.title("Employee Login Page")
e.geometry("1100x700")
e.resizable(False, False)
e.resizable(False, False)

def main_frames():
    def displayit():
        k = []
        global  point,console_p
        point = mysql.connector.connect(host="localhost", user="root", password="anakha", database="empdata3")
        console_p = point.cursor()
        command = "select * from employeedata3 where id = %s "
        values = [id_data.get()]
        console_p.execute(command,values)
        l = console_p.fetchall()
        for i in l[0]:
            k.append(i)

        id_container.insert(0, k[0])
        name_container.insert(0, k[1])
        mobile_container.insert(0, k[2])
        email_container.insert(0, k[3])
        address_container.insert(0, k[4])
        gender_container.insert(0, k[5])
        salary_container.insert(0, k[6])
        dob_container.insert(0, k[7])
        department_container.insert(0, k[8])
        position_container.insert(0, k[9])
        date_container.insert(0, k[10])
        time_container.insert(0, k[11])

        welcome_label.config(text="Hello " + k[1] + " !")

    def timeflow():
        timeis = time.strftime("%H:%M:%S")
        dateis = time.strftime("%d/%m/%Y")
        dateset.config(text='Date :' + dateis + "\n" + "Time : " + timeis)
        dateset.after(200, timeflow)


    Label_frame = Frame(e, bg="firebrick", bd=5, relief="ridge")
    Label_frame.place(x=0, y=0, width=1102, height=102)


    dashboard_label = Label(Label_frame,text = "DASHBOARD", bg = "firebrick", fg = "goldenrod", relief= RIDGE,  font=("arial", 22, "bold"),width = 1099 , height= 50)
    dashboard_label.place(x = 0 , y= 0 , width = 1099 , height= 50)
    dashboard_label.pack(side='top')



    welcome_frame = Frame(e,bg = "peach puff",bd = 2, relief=RIDGE)
    welcome_frame.place(x = 0 , y=100, width = 1100, height= 153)

    welcome_label = Label(welcome_frame,text = "Hello...!", bg = "peach puff", fg = "firebrick",   font=("arial", 22, "bold"),width = 1099 , height= 50, anchor='sw')
    welcome_label.place(x = 50 , y=50, width = 160 , height= 50)

    #==================================================================
    dateset = Label(welcome_frame, text="Date:", bg="peach puff", font=("verdana", 12, "bold"), width=15, height=3,
                    relief=GROOVE)
    dateset.place(x=900, y=50)
    timeflow()

    #==================================================================

    employee_details = Frame(e,bg = "navajo white",bd = 2,relief=RIDGE)
    employee_details.place(x = 0 , y=253, width = 1100, height= 446)



    sub_container = Frame(employee_details,bg = "navajo white",relief=GROOVE)
    sub_container.place(x = 100 , y=30, width = 900, height= 389)

    id_label = Label(sub_container,text = "ID: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    name_label = Label(sub_container,text = "Name: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    mobile_label = Label(sub_container,text = "Mobile: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    email_label = Label(sub_container,text = "Email: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    address_label = Label(sub_container,text = "Address: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    gender_label = Label(sub_container,text = "Gender: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    salary_label = Label(sub_container,text = "Salary: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    position_label = Label(sub_container,text = "Position: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    dob_label = Label(sub_container,text = "DOB: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    department_label = Label(sub_container,text = "Department: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    date_label = Label(sub_container,text = "Date: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))
    time_label = Label(sub_container,text = "Time: ", bg = "navajo white", fg = "black",   font=("arial", 20, "bold"))

    id_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    name_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    mobile_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    email_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    address_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    gender_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    salary_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    position_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    dob_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    department_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    date_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)
    time_container = Entry(sub_container, font=('Helvetica', 13, 'bold'),bg= "grey95", bd=3, width=20)

    id_container.grid(row=0 ,column=1, padx= 20, pady= 20)
    name_container.grid(row=0 ,column=3, padx= 20, pady= 20)
    mobile_container.grid(row=1 ,column=1, padx= 20, pady= 20)
    email_container.grid(row=1 ,column=3, padx= 20, pady= 20)
    address_container.grid(row=2 ,column=1, padx= 20, pady= 20)
    gender_container.grid(row=2 ,column=3, padx= 20, pady= 20)
    salary_container.grid(row=3 ,column=1, padx= 20, pady= 20)
    dob_container.grid(row=3, column=3, padx=20, pady=20)
    department_container.grid(row=4, column=1, padx=20, pady=20)
    position_container.grid(row=4 ,column=3, padx= 20, pady= 20)


    id_label.grid(row=0 ,column=0, padx= 20, pady= 20)
    name_label.grid(row=0 ,column=2, padx= 20, pady= 20)
    mobile_label.grid(row=1 ,column=0, padx= 20, pady= 20)
    email_label.grid(row=1 ,column=2, padx= 20, pady= 20)
    address_label.grid(row=2 ,column=0, padx= 20, pady= 20)
    gender_label.grid(row=2 ,column=2, padx= 20, pady= 20)
    salary_label.grid(row=3 ,column=0, padx= 20, pady= 20)
    dob_label.grid(row=3, column=2, padx=20, pady=20)
    department_label.grid(row=4, column=0, padx=20, pady=20)
    position_label.grid(row=4 ,column=2, padx= 20, pady= 20)



    displayit()


#-------------------------------------------------------------------------------------------------------------------
def procced():
    point = mysql.connector.connect(host = "localhost", user = "root", password = "anakha", database = "empdata3")
    main_cursor = point.cursor()
    command =" select * from login_credential2 where user_name = %s and password = %s and user_id = %s"
    values = (user_data.get(),password_data.get(),id_data.get())
    main_cursor.execute(command,values)
    rel = main_cursor.fetchall()
    if rel:
        for i in rel:
            messagebox.showinfo("Success", "LOGIN SUCCESSFULL !!")

        main_frames()
    else:
         print("Invalid credentials")
         messagebox.showerror("Failed", "Username or password is incorrect")





def showit():
    if v.get() == 1:
        password_data.config(show = '')
    else:
        password_data.config(show='*')

Label_frame = Frame(e,bg="firebrick", bd=5, relief="ridge")
Label_frame.place(x=1, y=1, width=1099, height=62)
main_label = Label(Label_frame, text="Employee Login Page", bg="firebrick", fg="goldenrod",font=("arial", 22, "bold"))
main_label.pack(side="top")

img = (Image.open("Resource//workbench4.jfif"))
img2 = img.resize((1094,700))
img1 = ImageTk.PhotoImage(img2)


connectd = Frame(e)
connectd.place(x = 0,y = 62,width = 1100,height= 900)

connectd.config(bg='DarkOrange1')

l1 = Label(connectd,image= img1)
l1.pack(side="top")



imgs = (Image.open("Resource//user.png"))
imgs1 = imgs.resize((30,30))
imgs2 = ImageTk.PhotoImage(imgs1)

image = (Image.open("Resource//lock.png"))
image1 = image.resize((30,30))
image2 = ImageTk.PhotoImage(image1)

user_root = Label(e, text="Username", bg="grey92", font=("verdana", 12, "bold"),
                 borderwidth=3, width=10, anchor='e')
user_root.place(x=390, y=280)

login_img = Label(e,image= imgs2, bg = "grey90")
login_img.place(x =360 ,y=275, width = 40, height = 40)

password = Label(e, text="Password", bg="grey92", font=("verdana", 12, "bold"),
                      borderwidth=3, width=10, anchor='e')
password.place(x=390, y=340)

id_val = Label(e, text="Employee ID", bg="grey92", font=("verdana", 12, "bold"),
                      borderwidth=3, width=10, anchor='e')
id_val.place(x=390, y=400)

password_img = Label(e,image= image2, bg = "grey90")
password_img.place(x =360 ,y=335, width = 40, height = 40)

#-----------------------------------------------------------------------------------------Entry:




user_data = Entry(e, font=('Helvetica', 12, 'bold'),bg= "grey85", bd=3, width=20)
user_data.place(x=540, y=280)

password_data = Entry(e, font=('Helvetica', 12, 'bold'),bg= "grey85", bd=3, width=20,show= "*")
password_data.place(x=540, y=340)

id_data = Entry(e, font=('Helvetica', 12, 'bold'),bg= "grey85", bd=3, width=20)
id_data.place(x=540, y=400)

#-------------------------------------------------------------------------------------------------
v = IntVar()

show_pass = Checkbutton(e,variable=v,bg="grey97",onvalue=1,offvalue=0, command=showit)
show_pass.place(x = 740, y = 340)

login_button = Button(e, text="Login", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                           width=7,command=procced)
login_button.place(x=460, y=480)

registration_button = Button(e, text="New User?", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                           width=9,command=add_user)
registration_button.place(x=580, y=480)







e.mainloop()

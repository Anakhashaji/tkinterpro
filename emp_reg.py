from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
import time
import mysql.connector




def timeflow():
    timeis = time.strftime("%H:%M:%S")
    dateis = time.strftime("%d/%m/%Y")
    dateset.config(text='Date :' + dateis + "\n" + "Time : " + timeis)
    dateset.after(200, timeflow)



def add_user():
    adding = Toplevel(master=Data_frame)
    adding.grab_set()
    adding.geometry('470x600+220+200')
    adding.title('Enter details')
    adding.config(bg='light blue')
    adding.resizable(False, False)

    user_id = Label(adding, text = "User ID",bg = "light grey",font=("verdana", 14, "bold"),relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    user_id.place(x = 10,y = 30)

    name = Label(adding, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    name.place(x=10, y=80)

    mobile_no = Label(adding, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    mobile_no.place(x=10, y=130)

    email = Label(adding, text="E-mail", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    email.place(x=10, y=180)

    address = Label(adding, text="Address", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                  borderwidth=3, width=11, anchor='w')
    address.place(x=10, y=230)

    gender = Label(adding, text="Gender", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    gender.place(x=10, y=280)

    salary = Label(adding, text="Salary", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')

    salary.place(x=10, y=330)

    dob = Label(adding, text="DOB", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                borderwidth=3, width=11, anchor='w')

    dob.place(x=10, y=380)

    department = Label(adding, text="Department", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                       borderwidth=3, width=11, anchor='w')

    department.place(x=10, y=430)

    positon = Label(adding, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')

    positon.place(x=10, y=480)



#------------------------------------------------------------------------------- code for Entry func.
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



    user_enter =  Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=idval, bd=3, width=18)
    user_enter.place(x = 230,y = 30)

    name_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=nameval, bd=3, width=18)
    name_enter.place(x=230, y=80)

    mobile_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=mobileval, bd=3, width=18)
    mobile_enter.place(x=230, y=130)

    email_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=emailval, bd=3, width=18)
    email_enter.place(x=230, y=180)

    address_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=addressval, bd=3, width=18)
    address_enter.place(x=230, y=230)

    gender_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=genderval, bd=3, width=18)
    gender_enter.place(x=230, y=280)

    salary_enter = Entry(adding, font=('Helvetica', 15, 'bold'),textvariable=salaryval, bd=3, width=18)
    salary_enter.place(x=230, y=330)

    dob_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=dobval, bd=3, width=18)
    dob_enter.place(x=230, y=380)

    department_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=departmentval, bd=3, width=18)
    department_enter.place(x=230, y=430)

    position_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=positionval, bd=3, width=18)
    position_enter.place(x=230, y=480)

#---------------------------------------------------------------------------------Func:
    def submitadd():
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

        try:
            strr = 'insert into employeedata3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, salary, dob, department ,position, addeddate, addedtime))
            db_p.commit()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,
                                                                                                                  name),
                                            parent=adding)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                salaryval.set('')
                dobval.set('')
                departmentval.set('')
                positionval.set('')

            # clearing the entry form after adding details to database only if res==true

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=adding)
        strr = 'select * from employeedata3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]  # making data as list to print on treeview
            employeetable.insert('', END,
                                 values=vv)


#--------------------------------------------------------------------------------Add button
    add_button = Button(adding,text = "ADD",relief="raised", bg="light grey", font=("verdana", 14, "bold"),
                width=7,command=submitadd)
    add_button.place(x = 170, y = 530)




def delete_user():
    try:
        cc = employeetable.focus()  # focus on the record which we click and gets data of that record
        content = employeetable.item(cc)
        pp = [content['values'][0]]# it gives the id of the particular record to delete
        strr = 'delete from employeedata3 where id=%s'
        mycursor.execute(strr, pp)
        str1 = 'delete from login_credential2 where user_id=%s'
        mycursor.execute(str1, pp)

        db_p.commit()


        messagebox.showinfo('Notifications', 'Id {} deleted sucessfully...'.format(pp))
        strr = 'select *from employeedata3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8] ,i[9],i[10],i[11]]
            employeetable.insert('', END, values=vv)







    except:
        messagebox.showwarning("Warning","Select a row")


def update_details():
    update = Toplevel(master=Data_frame)
    update.grab_set()
    update.geometry('470x650+220+200')
    update.title('Enter details')
    update.config(bg='light blue')
    update.resizable(False, False)

    user_id = Label(update, text="User ID", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    user_id.place(x=10, y=30)

    userLabel = Label(update, text="User ID", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    userLabel.place(x=230, y=30)

    name = Label(update, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                 borderwidth=3, width=11, anchor='w')
    name.place(x=10, y=80)

    mobile_no = Label(update, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                      borderwidth=3, width=11, anchor='w')
    mobile_no.place(x=10, y=130)

    email = Label(update, text="E-mail", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                  borderwidth=3, width=11, anchor='w')
    email.place(x=10, y=180)

    address = Label(update, text="Address", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    address.place(x=10, y=230)

    gender = Label(update, text="Gender", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')
    gender.place(x=10, y=280)

    salary = Label(update, text="Salary", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')
    salary.place(x=10, y=330)

    dob = Label(update, text="DOB", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                            borderwidth=3, width=11, anchor='w')
    dob.place(x=10, y=380)

    department = Label(update, text="Department", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                     borderwidth=3, width=11, anchor='w')
    department.place(x=10, y=430)

    position = Label(update, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                     borderwidth=3, width=11, anchor='w')
    position.place(x=10, y=480)

    date2 = Label(update, text="Date", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                        borderwidth=3, width=11, anchor='w')
    date2.place(x=10, y=530)

    #---------------------------------------------------------------------------------------------Entry Field:

    user_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18,state="readonly")


    name_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    name_update.place(x=230, y=80)

    mobile_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    mobile_update.place(x=230, y=130)

    email_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    email_update.place(x=230, y=180)

    address_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    address_update.place(x=230, y=230)

    gender_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    gender_update.place(x=230, y=280)

    salary_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    salary_update.place(x=230, y=330)

    dob_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    dob_update.place(x=230, y=380)

    department_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    department_update.place(x=230, y=430)

    position_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    position_update.place(x=230, y=480)

    date_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    date_update.place(x=230, y=530)

#--------------------------------------------------------------------------------Updating function


    try:
        target = employeetable.focus()
        datas = employeetable.item(target)

        list_items = datas['values']
        user_update.insert(0,list_items[0])
        userLabel.config(text = list_items[0])
        name_update.insert(0, list_items[1])
        mobile_update.insert(0, list_items[2])
        email_update.insert(0, list_items[3])
        address_update.insert(0, list_items[4])
        gender_update.insert(0, list_items[5])
        salary_update.insert(0, list_items[6])
        dob_update.insert(0, list_items[7])
        department_update.insert(0, list_items[8])
        position_update.insert(0, list_items[9])
        date_update.insert(0, list_items[10])
        time3 = time.strftime('%H:%M:%S')
        def Update_User_details():
            command = 'update employeedata3 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,salary=%s,dob=%s,department =%s,position=%s,date=%s,time=%s where id = %s'
            mycursor.execute(command,(name_update.get(),mobile_update.get(),email_update.get(),address_update.get(),gender_update.get(),salary_update.get(),dob_update.get(),department_update.get(),position_update.get(),date_update.get(),time3,list_items[0]))
            db_p.commit()
            messagebox.showinfo("Success","The data has been updated!", parent = update)
            update.destroy()
            show_details()


#---------------------------------------------------------------------------------Update Button:
        update_button = Button(update, text="UPDATE", relief="raised", bg="light grey", font=("verdana", 14, "bold"),
                            width=7,command=Update_User_details)
        update_button.place(x=170, y=580)
    except:
        update.destroy()
        messagebox.showwarning("Warning","Select a row to update it.")







#------------------------------------------------------------------------------------Functions:

def show_details():

    try:
        strr = 'select *from employeedata3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            employeetable.insert('', END, values=vv)
    except:
        messagebox.showerror("Error","No data in database")


def search_user():
    searchit = Toplevel(master=Data_frame)
    searchit.grab_set()
    searchit.geometry('470x650+220+200')
    searchit.title('Enter details')
    searchit.config(bg='light blue')
    searchit.resizable(False, False)

    user_search = Label(searchit, text="User ID", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    user_search.place(x=10, y=30)

    name_search = Label(searchit, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                 borderwidth=3, width=11, anchor='w')
    name_search.place(x=10, y=80)

    mobile_search = Label(searchit, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                      borderwidth=3, width=11, anchor='w')
    mobile_search.place(x=10, y=130)

    email_search = Label(searchit, text="E-mail", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                  borderwidth=3, width=11, anchor='w')
    email_search.place(x=10, y=180)

    address_search = Label(searchit, text="Address", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                    borderwidth=3, width=11, anchor='w')
    address_search.place(x=10, y=230)

    gender_search = Label(searchit, text="Gender", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')
    gender_search.place(x=10, y=280)

    salary_search = Label(searchit, text="Salary", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                   borderwidth=3, width=11, anchor='w')
    salary_search.place(x=10, y=330)

    dob_search = Label(searchit, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                            borderwidth=3, width=11, anchor='w')
    dob_search.place(x=10, y=380)

    department_search = Label(searchit, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                       borderwidth=3, width=11, anchor='w')
    department_search.place(x=10, y=430)

    position_search = Label(searchit, text="Position", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                          borderwidth=3, width=11, anchor='w')
    position_search.place(x=10, y=480)

    date_search = Label(searchit, text="Date", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                            borderwidth=3, width=11, anchor='w')
    date_search.place(x=10, y=530)


    # ---------------------------------------------------------------------------------------------Entry Field:

    user_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    user_search_data.place(x=230, y=30)

    name_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    name_search_data.place(x=230, y=80)

    mobile_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    mobile_search_data.place(x=230, y=130)

    email_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    email_search_data.place(x=230, y=180)

    address_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    address_search_data.place(x=230, y=230)

    gender_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    gender_search_data.place(x=230, y=280)

    salary_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    salary_search_data.place(x=230, y=330)

    dob_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    dob_search_data.place(x=230, y=380)

    department_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    department_search_data.place(x=230, y=430)

    position_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    position_search_data.place(x=230, y=480)

    date_search_data = Entry(searchit, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    date_search_data.place(x=230, y=530)

    # --------------------------------------------------------------------------------Update Button:
    def searching():

            id = user_search_data.get()
            name = name_search_data.get()
            mobile = mobile_search_data.get()
            email = email_search_data.get()
            address = address_search_data.get()
            gender = gender_search_data.get()
            salary = salary_search_data.get()
            dob = dob_search_data.get()
            department = dob_search_data.get()
            position = position_search_data.get()
            dateis = date_search_data.get()

            command = 'select * from employeedata3 where id = %s or name = %s or mobile = %s or email = %s or address = %s or gender = %s or salary = %s or dob =%s or department = %s or position = %s or date = %s '
            mycursor.execute(command,(user_search_data.get(),name_search_data.get(),mobile_search_data.get(),email_search_data.get(),address_search_data.get(),gender_search_data.get(),salary_search_data.get(),dob_search_data.get(),department_search_data.get(),position_search_data.get(),date_search_data.get()))
            employeetable.delete(*employeetable.get_children())
            all_data = mycursor.fetchall()
            for data in all_data:
                employeetable.insert('',END,values = data)
            searchit.destroy()


#--------------------------------------------------------------------------------------Search function:
    search_button = Button(searchit, text="Search", relief="raised", bg="light grey", font=("verdana", 14, "bold"),
                           width=7,command=searching)
    search_button.place(x=170, y=580)





def exit_interface():
    opt = messagebox.askyesnocancel("Warning","Do you wish to exit")
    if(opt == True):
        w.destroy()





def db_connect():

    def showpass():
        if v.get() == 1:
            password_data.config(show="")
        else:
            password_data.config(show="*")

    messagebox.showinfo("Login","Enter the correct Host,username and password to connect with DataBase")

    connectdb = Toplevel(master=Data_frame)
    connectdb.grab_set()
    connectdb.geometry('600x300+220+200')
    connectdb.title('Enter details')
    connectdb.config(bg='light blue')
    connectdb.resizable(False, False)

    db_label = Label(connectdb, text="Enter the SQL credentials", bg="#f7e7ce", font=("verdana", 14, "bold"), relief= GROOVE,
                    borderwidth=3, width=50)
    db_label.pack(side="top")
    db_label.place(x=0, y=0)


#----------------------------------------------------------------------------------------Labels:
    host_detail = Label(connectdb, text="Host:", bg="light blue", font=("verdana", 14, "bold"),
                    borderwidth=3, width=11, anchor='e')
    host_detail.place(x=50, y=50)

    user_root = Label(connectdb, text="User Id:", bg="light blue", font=("verdana", 14, "bold"),
                 borderwidth=3, width=11, anchor='e')
    user_root.place(x=50, y=100)

    password = Label(connectdb, text="Password:", bg="light blue", font=("verdana", 14, "bold"),
                      borderwidth=3, width=11, anchor='e')
    password.place(x=50, y=150)

#-----------------------------------------------------------------------------------------Entry:
    host_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    host_data.place(x=230, y=50)

    user_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18)
    user_data.place(x=230, y=100)

    password_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18,show= "*")
    password_data.place(x=230, y=150)

#-------------------------------------------------------------------------------------------------
    v = IntVar()

    show_pass = Checkbutton(connectdb,variable=v,bg="light blue",onvalue=1,offvalue=0,command=showpass)
    show_pass.place(x = 450, y = 150)


    def dbconnection():
        try:
            global  db_p,mycursor
            db_p = mysql.connector.connect(host=host_data.get(), user = user_data.get() ,password = password_data.get())
            mycursor = db_p.cursor()
        except:
            messagebox.showerror("Error","Wrong SQL credentials.")
        try:
            strr = 'create database empdata3'
            mycursor.execute(strr)
            strr = 'use empdata3'
            mycursor.execute(strr)
            strr = 'create table employeedata3(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),salary varchar(50),dob varchar(20),department varchar(30),position varchar(30),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table employeedata3 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table employeedata3 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo("Created","New database has been created!")

        except:
            try:
                strr = 'use empdata3'
                mycursor.execute(strr)
                messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=connectdb)

            except:
                return
        connectdb.destroy()
        show_details()



    login_button = Button(connectdb, text="Login", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                           width=7,command=dbconnection)
    login_button.place(x=290, y=220)










w = Tk()

w.title("Employee Management System")
w.config(bg="grey")
w.geometry("1100x700")
w.resizable(False, False)



Label_frame = Frame(w,bg="#f7e7ce", bd=1, relief="groove")
Label_frame.place(x=5, y=0, width=1090, height=80)
main_label = Label(Label_frame, text="Employee Management System", bg="#f7e7ce", fg="Black",font=("arial", 22, "bold"))
main_label.pack(side="top")

#---------------------------------------------------------Data frame created
Data_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
Data_frame.place(x=5, y=90, width=300, height=500)

# --------------------data entry frame labels
frontlabel = Label(Data_frame, text="Data Management Functions", relief="groove", bg="#f7e7ce", fg="black",
                   font=("arial", 15, "bold"))
frontlabel.pack(side="top", fill=BOTH)

#-------------------------------------------------------Data_frame buttons




add = Button(Data_frame,text = "Add User",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= add_user)
add.place(x = 20,y = 100)

update = Button(Data_frame,text = "Update User Details",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= update_details)
update.place(x = 20,y = 150)

search = Button(Data_frame,text = "Search for user",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= search_user)
search.place(x = 20,y = 200)

delete = Button(Data_frame,text = "Delete User",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= delete_user)
delete.place(x = 20,y = 250)

show = Button(Data_frame,text = "Show User Details",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= show_details)
show.place(x = 20,y = 300)

exitit = Button(Data_frame,text = "Exit",relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20,command= exit_interface)
exitit.place(x = 20,y = 350)


#----------------------------------------------------------------Container for Displaying DB data:


data_display_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
data_display_frame.place(x=330, y=90, width= 760, height=500)



display_label = Label(data_display_frame, text="Database Data", relief="groove", bg="#f7e7ce", fg="black",
                   font=("arial", 15, "bold"))
display_label.pack(side="top", fill=BOTH)


#----------------------------------------------------------------------------------------Using TreeView for Displaying data:

style = ttk.Style()
style.configure('Treeview.Heading', font=('verdana', 12, 'bold'), foreground='navy blue')
style.configure('Treeview', font=('Helvetica', 11, 'bold'), foreground='black', background='lavender')
scroll_x = Scrollbar(data_display_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(data_display_frame, orient=VERTICAL)
employeetable = Treeview(data_display_frame, columns=(
'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Salary', 'DOB', 'Department', 'Position', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=employeetable.xview)
scroll_y.config(command=employeetable.yview)
employeetable.heading('Id', text='Id')
employeetable.heading('Name', text='Name')
employeetable.heading('Mobile No', text='Mobile No')
employeetable.heading('Email', text='Email')
employeetable.heading('Address', text='Address')
employeetable.heading('Gender', text='Gender')
employeetable.heading('Salary', text='Salary')
employeetable.heading('DOB', text='DOB')
employeetable.heading('Department', text='Department')
employeetable.heading('Position', text='Position')
employeetable.heading('Added Date', text='Added Date')
employeetable.heading('Added Time', text='Added Time')
employeetable['show'] = 'headings'
employeetable.column('Id', width=100)
employeetable.column('Name', width=200)
employeetable.column('Mobile No', width=200)
employeetable.column('Email', width=300)
employeetable.column('Address', width=200)
employeetable.column('Gender', width=100)
employeetable.column('Salary', width=150)
employeetable.column('DOB', width=200)
employeetable.column('Department', width=200)
employeetable.column('Position', width=150)
employeetable.column('Added Date', width=150)
employeetable.column('Added Time', width=150)
employeetable.pack(fill=BOTH, expand=1)


#----------------------------------------------------------Bottom Container

Bottom_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
Bottom_frame.place(x=5, y=600, width=1090, height=95)


bb1 = Button(Bottom_frame,text = "Connect DB",relief="raised",fg = "firebrick4", bg="Light blue", font=("verdana", 12, "bold"),
                width=10,height = 3, command=db_connect)
bb1.place(x = 10,y = 17)


dateset = Label(Bottom_frame,text = "Date:",bg ="#DCAE96",font=("verdana", 12, "bold"),width = 15,height=3 ,relief=GROOVE)
dateset.place(x = 900, y = 19)
timeflow()
#-------------------------------------------------------------------Add user Frame

c = messagebox.askyesno("Login to Database ","Please connect to the database first")
if c == True:
    db_connect()






if __name__ == '__main__':
    w.mainloop()

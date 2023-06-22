

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import random,os
import mysql.connector
import time
from time import strftime
import tempfile
from tkinter.ttk import Treeview


def adminrun():
    def procced():

        point = mysql.connector.connect(host="localhost", user="root", password="anakha", database="empdata3")
        main_cursor = point.cursor()
        command = " select * from admin_credential where user_id = %s and user_password = %s"
        values = (user_data.get(), password_data.get())
        main_cursor.execute(command, values)
        rel = main_cursor.fetchall()
        if rel:
            for i in rel:
                messagebox.showinfo("Success", "LOGIN SUCCESSFULL !!")


                def runningit():



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

                        user_id = Label(adding, text="User ID", bg="light grey", font=("verdana", 14, "bold"),
                                        relief=GROOVE,
                                        borderwidth=3, width=11, anchor='w')
                        user_id.place(x=10, y=30)

                        name = Label(adding, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                                     borderwidth=3, width=11, anchor='w')
                        name.place(x=10, y=80)

                        mobile_no = Label(adding, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"),
                                          relief=GROOVE,
                                          borderwidth=3, width=11, anchor='w')
                        mobile_no.place(x=10, y=130)

                        email = Label(adding, text="E-mail", bg="light grey", font=("verdana", 14, "bold"),
                                      relief=GROOVE,
                                      borderwidth=3, width=11, anchor='w')
                        email.place(x=10, y=180)

                        address = Label(adding, text="Address", bg="light grey", font=("verdana", 14, "bold"),
                                        relief=GROOVE,
                                        borderwidth=3, width=11, anchor='w')
                        address.place(x=10, y=230)

                        gender = Label(adding, text="Gender", bg="light grey", font=("verdana", 14, "bold"),
                                       relief=GROOVE,
                                       borderwidth=3, width=11, anchor='w')
                        gender.place(x=10, y=280)

                        salary = Label(adding, text="Salary", bg="light grey", font=("verdana", 14, "bold"),
                                       relief=GROOVE,
                                       borderwidth=3, width=11, anchor='w')

                        salary.place(x=10, y=330)

                        dob = Label(adding, text="DOB", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                                    borderwidth=3, width=11, anchor='w')

                        dob.place(x=10, y=380)

                        department = Label(adding, text="Department", bg="light grey", font=("verdana", 14, "bold"),
                                           relief=GROOVE,
                                           borderwidth=3, width=11, anchor='w')

                        department.place(x=10, y=430)

                        positon = Label(adding, text="Position", bg="light grey", font=("verdana", 14, "bold"),
                                        relief=GROOVE,
                                        borderwidth=3, width=11, anchor='w')

                        positon.place(x=10, y=480)

                        # ------------------------------------------------------------------------------- code for Entry func.
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

                        user_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=idval, bd=3, width=18)
                        user_enter.place(x=230, y=30)

                        name_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=nameval, bd=3, width=18)
                        name_enter.place(x=230, y=80)

                        mobile_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=mobileval, bd=3,
                                             width=18)
                        mobile_enter.place(x=230, y=130)

                        email_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=emailval, bd=3,
                                            width=18)
                        email_enter.place(x=230, y=180)

                        address_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=addressval, bd=3,
                                              width=18)
                        address_enter.place(x=230, y=230)

                        gender_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=genderval, bd=3,
                                             width=18)
                        gender_enter.place(x=230, y=280)

                        salary_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=salaryval, bd=3,
                                             width=18)
                        salary_enter.place(x=230, y=330)

                        dob_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=dobval, bd=3, width=18)
                        dob_enter.place(x=230, y=380)

                        department_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=departmentval,
                                                 bd=3, width=18)
                        department_enter.place(x=230, y=430)

                        position_enter = Entry(adding, font=('Helvetica', 15, 'bold'), textvariable=positionval, bd=3,
                                               width=18)
                        position_enter.place(x=230, y=480)

                        # ---------------------------------------------------------------------------------Func:
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
                                mycursor.execute(strr, (
                                id, name, mobile, email, address, gender, salary, dob, department, position, addeddate,
                                addedtime))
                                db_p.commit()
                                res = messagebox.askyesnocancel('Notificatrions',
                                                                'Id {} Name {} Added sucessfully.. and want to clean the form'.format(
                                                                    id,
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
                                messagebox.showerror('Notifications', 'Id Already Exist try another id...',
                                                     parent=adding)
                            strr = 'select * from employeedata3'
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            employeetable.delete(*employeetable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],
                                      i[11]]  # making data as list to print on treeview
                                employeetable.insert('', END,
                                                     values=vv)

                        # --------------------------------------------------------------------------------Add button
                        add_button = Button(adding, text="ADD", relief="raised", bg="light grey",
                                            font=("verdana", 14, "bold"),
                                            width=7, command=submitadd)
                        add_button.place(x=170, y=530)

                    def delete_user():
                        try:
                            cc = employeetable.focus()  # focus on the record which we click and gets data of that record
                            content = employeetable.item(cc)
                            pp = [content['values'][0]]  # it gives the id of the particular record to delete
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
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                employeetable.insert('', END, values=vv)







                        except:
                            messagebox.showwarning("Warning", "Select a row")

                    def update_details():
                        update = Toplevel(master=Data_frame)
                        update.grab_set()
                        update.geometry('470x650+220+200')
                        update.title('Enter details')
                        update.config(bg='light blue')
                        update.resizable(False, False)

                        user_id = Label(update, text="User ID", bg="light grey", font=("verdana", 14, "bold"),
                                        relief=GROOVE,
                                        borderwidth=3, width=11, anchor='w')
                        user_id.place(x=10, y=30)

                        userLabel = Label(update, text="User ID", bg="light grey", font=("verdana", 14, "bold"),
                                          relief=GROOVE,
                                          borderwidth=3, width=11, anchor='w')
                        userLabel.place(x=230, y=30)

                        name = Label(update, text="Name", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                                     borderwidth=3, width=11, anchor='w')
                        name.place(x=10, y=80)

                        mobile_no = Label(update, text="Mobile No.", bg="light grey", font=("verdana", 14, "bold"),
                                          relief=GROOVE,
                                          borderwidth=3, width=11, anchor='w')
                        mobile_no.place(x=10, y=130)

                        email = Label(update, text="E-mail", bg="light grey", font=("verdana", 14, "bold"),
                                      relief=GROOVE,
                                      borderwidth=3, width=11, anchor='w')
                        email.place(x=10, y=180)

                        address = Label(update, text="Address", bg="light grey", font=("verdana", 14, "bold"),
                                        relief=GROOVE,
                                        borderwidth=3, width=11, anchor='w')
                        address.place(x=10, y=230)

                        gender = Label(update, text="Gender", bg="light grey", font=("verdana", 14, "bold"),
                                       relief=GROOVE,
                                       borderwidth=3, width=11, anchor='w')
                        gender.place(x=10, y=280)

                        salary = Label(update, text="Salary", bg="light grey", font=("verdana", 14, "bold"),
                                       relief=GROOVE,
                                       borderwidth=3, width=11, anchor='w')
                        salary.place(x=10, y=330)

                        dob = Label(update, text="DOB", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                                    borderwidth=3, width=11, anchor='w')
                        dob.place(x=10, y=380)

                        department = Label(update, text="Department", bg="light grey", font=("verdana", 14, "bold"),
                                           relief=GROOVE,
                                           borderwidth=3, width=11, anchor='w')
                        department.place(x=10, y=430)

                        position = Label(update, text="Position", bg="light grey", font=("verdana", 14, "bold"),
                                         relief=GROOVE,
                                         borderwidth=3, width=11, anchor='w')
                        position.place(x=10, y=480)

                        date2 = Label(update, text="Date", bg="light grey", font=("verdana", 14, "bold"), relief=GROOVE,
                                      borderwidth=3, width=11, anchor='w')
                        date2.place(x=10, y=530)

                        # ---------------------------------------------------------------------------------------------Entry Field:

                        user_update = Entry(update, font=('Helvetica', 15, 'bold'), bd=3, width=18, state="readonly")

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

                        # --------------------------------------------------------------------------------Updating function

                        try:
                            target = employeetable.focus()
                            datas = employeetable.item(target)

                            list_items = datas['values']
                            user_update.insert(0, list_items[0])
                            userLabel.config(text=list_items[0])
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
                                mycursor.execute(command, (
                                name_update.get(), mobile_update.get(), email_update.get(), address_update.get(),
                                gender_update.get(), salary_update.get(), dob_update.get(), department_update.get(),
                                position_update.get(), date_update.get(), time3, list_items[0]))
                                db_p.commit()
                                messagebox.showinfo("Success", "The data has been updated!", parent=update)
                                update.destroy()
                                show_details()

                            # ---------------------------------------------------------------------------------Update Button:
                            update_button = Button(update, text="UPDATE", relief="raised", bg="light grey",
                                                   font=("verdana", 14, "bold"),
                                                   width=7, command=Update_User_details)
                            update_button.place(x=170, y=580)
                        except:
                            update.destroy()
                            messagebox.showwarning("Warning", "Select a row to update it.")

                    # ------------------------------------------------------------------------------------Functions:

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
                            messagebox.showerror("Error", "No data in database")

                    def search_user():
                        searchit = Toplevel(master=Data_frame)
                        searchit.grab_set()
                        searchit.geometry('470x650+220+200')
                        searchit.title('Enter details')
                        searchit.config(bg='light blue')
                        searchit.resizable(False, False)

                        user_search = Label(searchit, text="User ID", bg="light grey", font=("verdana", 14, "bold"),
                                            relief=GROOVE,
                                            borderwidth=3, width=11, anchor='w')
                        user_search.place(x=10, y=30)

                        name_search = Label(searchit, text="Name", bg="light grey", font=("verdana", 14, "bold"),
                                            relief=GROOVE,
                                            borderwidth=3, width=11, anchor='w')
                        name_search.place(x=10, y=80)

                        mobile_search = Label(searchit, text="Mobile No.", bg="light grey",
                                              font=("verdana", 14, "bold"), relief=GROOVE,
                                              borderwidth=3, width=11, anchor='w')
                        mobile_search.place(x=10, y=130)

                        email_search = Label(searchit, text="E-mail", bg="light grey", font=("verdana", 14, "bold"),
                                             relief=GROOVE,
                                             borderwidth=3, width=11, anchor='w')
                        email_search.place(x=10, y=180)

                        address_search = Label(searchit, text="Address", bg="light grey", font=("verdana", 14, "bold"),
                                               relief=GROOVE,
                                               borderwidth=3, width=11, anchor='w')
                        address_search.place(x=10, y=230)

                        gender_search = Label(searchit, text="Gender", bg="light grey", font=("verdana", 14, "bold"),
                                              relief=GROOVE,
                                              borderwidth=3, width=11, anchor='w')
                        gender_search.place(x=10, y=280)

                        salary_search = Label(searchit, text="Salary", bg="light grey", font=("verdana", 14, "bold"),
                                              relief=GROOVE,
                                              borderwidth=3, width=11, anchor='w')
                        salary_search.place(x=10, y=330)

                        dob_search = Label(searchit, text="Position", bg="light grey", font=("verdana", 14, "bold"),
                                           relief=GROOVE,
                                           borderwidth=3, width=11, anchor='w')
                        dob_search.place(x=10, y=380)

                        department_search = Label(searchit, text="Position", bg="light grey",
                                                  font=("verdana", 14, "bold"), relief=GROOVE,
                                                  borderwidth=3, width=11, anchor='w')
                        department_search.place(x=10, y=430)

                        position_search = Label(searchit, text="Position", bg="light grey",
                                                font=("verdana", 14, "bold"), relief=GROOVE,
                                                borderwidth=3, width=11, anchor='w')
                        position_search.place(x=10, y=480)

                        date_search = Label(searchit, text="Date", bg="light grey", font=("verdana", 14, "bold"),
                                            relief=GROOVE,
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
                            mycursor.execute(command, (
                            user_search_data.get(), name_search_data.get(), mobile_search_data.get(),
                            email_search_data.get(), address_search_data.get(), gender_search_data.get(),
                            salary_search_data.get(), dob_search_data.get(), department_search_data.get(),
                            position_search_data.get(), date_search_data.get()))
                            employeetable.delete(*employeetable.get_children())
                            all_data = mycursor.fetchall()
                            for data in all_data:
                                employeetable.insert('', END, values=data)
                            searchit.destroy()

                        # --------------------------------------------------------------------------------------Search function:
                        search_button = Button(searchit, text="Search", relief="raised", bg="light grey",
                                               font=("verdana", 14, "bold"),
                                               width=7, command=searching)
                        search_button.place(x=170, y=580)

                    def exit_interface():
                        opt = messagebox.askyesnocancel("Warning", "Do you wish to exit")
                        if (opt == True):
                            w.destroy()
                            r.destroy()
                            k.deiconify()

                    def db_connect():

                        def showpass():
                            if v.get() == 1:
                                password_data.config(show="")
                            else:
                                password_data.config(show="*")

                        messagebox.showinfo("Login",
                                            "Enter the correct Host,username and password to connect with DataBase")

                        connectdb = Toplevel(master=Data_frame)
                        connectdb.grab_set()
                        connectdb.geometry('600x300+220+200')
                        connectdb.title('Enter details')
                        connectdb.config(bg='light blue')
                        connectdb.resizable(False, False)

                        db_label = Label(connectdb, text="Enter the SQL credentials", bg="#f7e7ce",
                                         font=("verdana", 14, "bold"), relief=GROOVE,
                                         borderwidth=3, width=50)
                        db_label.pack(side="top")
                        db_label.place(x=0, y=0)

                        # ----------------------------------------------------------------------------------------Labels:
                        host_detail = Label(connectdb, text="Host:", bg="light blue", font=("verdana", 14, "bold"),
                                            borderwidth=3, width=11, anchor='e')
                        host_detail.place(x=50, y=50)

                        user_root = Label(connectdb, text="User Id:", bg="light blue", font=("verdana", 14, "bold"),
                                          borderwidth=3, width=11, anchor='e')
                        user_root.place(x=50, y=100)

                        password = Label(connectdb, text="Password:", bg="light blue", font=("verdana", 14, "bold"),
                                         borderwidth=3, width=11, anchor='e')
                        password.place(x=50, y=150)

                        # -----------------------------------------------------------------------------------------Entry:
                        host_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18)
                        host_data.place(x=230, y=50)

                        user_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18)
                        user_data.place(x=230, y=100)

                        password_data = Entry(connectdb, font=('Helvetica', 15, 'bold'), bd=3, width=18, show="*")
                        password_data.place(x=230, y=150)

                        # -------------------------------------------------------------------------------------------------
                        v = IntVar()

                        show_pass = Checkbutton(connectdb, variable=v, bg="light blue", onvalue=1, offvalue=0,
                                                command=showpass)
                        show_pass.place(x=450, y=150)

                        def dbconnection():
                            try:
                                global db_p, mycursor
                                db_p = mysql.connector.connect(host=host_data.get(), user=user_data.get(),
                                                               password=password_data.get())
                                mycursor = db_p.cursor()
                            except:
                                messagebox.showerror("Error", "Wrong SQL credentials.")
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
                                messagebox.showinfo("Created", "New database has been created!")

                            except:
                                try:
                                    strr = 'use empdata3'
                                    mycursor.execute(strr)
                                    messagebox.showinfo('Notification', 'Now you are connected to the database ....',
                                                        parent=connectdb)

                                except:
                                    return
                            connectdb.destroy()
                            show_details()

                        login_button = Button(connectdb, text="Login", relief="raised", bg="light grey",
                                              font=("verdana", 11, "bold"),
                                              width=7, command=dbconnection)
                        login_button.place(x=290, y=220)

                    w = Toplevel()

                    w.title("Employee Management System")
                    w.config(bg="grey")
                    w.geometry("1100x700")
                    w.resizable(False, False)
                    r.bind('<FocusOut>',r.withdraw())
                    k.bind('<FocusOut>', k.withdraw())

                    Label_frame = Frame(w, bg="#f7e7ce", bd=1, relief="groove")
                    Label_frame.place(x=5, y=0, width=1090, height=80)
                    main_label = Label(Label_frame, text="Employee Management System", bg="#f7e7ce", fg="Black",
                                       font=("arial", 22, "bold"))
                    main_label.pack(side="top")

                    # ---------------------------------------------------------Data frame created
                    Data_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
                    Data_frame.place(x=5, y=90, width=300, height=500)

                    # --------------------data entry frame labels
                    frontlabel = Label(Data_frame, text="Data Management Functions", relief="groove", bg="#f7e7ce",
                                       fg="black",
                                       font=("arial", 15, "bold"))
                    frontlabel.pack(side="top", fill=BOTH)

                    # -------------------------------------------------------Data_frame buttons

                    add = Button(Data_frame, text="Add User", relief="raised", bg="light blue",
                                 font=("verdana", 14, "bold"),
                                 width=20, command=add_user)
                    add.place(x=20, y=100)

                    update = Button(Data_frame, text="Update User Details", relief="raised", bg="light blue",
                                    font=("verdana", 14, "bold"),
                                    width=20, command=update_details)
                    update.place(x=20, y=150)

                    search = Button(Data_frame, text="Search for user", relief="raised", bg="light blue",
                                    font=("verdana", 14, "bold"),
                                    width=20, command=search_user)
                    search.place(x=20, y=200)

                    delete = Button(Data_frame, text="Delete User", relief="raised", bg="light blue",
                                    font=("verdana", 14, "bold"),
                                    width=20, command=delete_user)
                    delete.place(x=20, y=250)

                    show = Button(Data_frame, text="Show User Details", relief="raised", bg="light blue",
                                  font=("verdana", 14, "bold"),
                                  width=20, command=show_details)
                    show.place(x=20, y=300)

                    exitit = Button(Data_frame, text="Exit", relief="raised", bg="light blue",
                                    font=("verdana", 14, "bold"),
                                    width=20, command=exit_interface)
                    exitit.place(x=20, y=350)

                    # ----------------------------------------------------------------Container for Displaying DB data:

                    data_display_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
                    data_display_frame.place(x=330, y=90, width=760, height=500)

                    display_label = Label(data_display_frame, text="Database Data", relief="groove", bg="#f7e7ce",
                                          fg="black",
                                          font=("arial", 15, "bold"))
                    display_label.pack(side="top", fill=BOTH)

                    # ----------------------------------------------------------------------------------------Using TreeView for Displaying data:

                    style = ttk.Style()
                    style.configure('Treeview.Heading', font=('verdana', 12, 'bold'), foreground='navy blue')
                    style.configure('Treeview', font=('Helvetica', 11, 'bold'), foreground='black',
                                    background='lavender')
                    scroll_x = Scrollbar(data_display_frame, orient=HORIZONTAL)
                    scroll_y = Scrollbar(data_display_frame, orient=VERTICAL)
                    employeetable = Treeview(data_display_frame, columns=(
                        'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Salary', 'DOB', 'Department',
                        'Position', 'Added Date', 'Added Time'),
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

                    # ----------------------------------------------------------Bottom Container

                    Bottom_frame = Frame(w, bg="#DCAE96", bd=1, relief="groove")
                    Bottom_frame.place(x=5, y=600, width=1090, height=95)

                    bb1 = Button(Bottom_frame, text="Connect DB", relief="raised", fg="firebrick4", bg="Light blue",
                                 font=("verdana", 12, "bold"),
                                 width=10, height=3, command=db_connect)
                    bb1.place(x=10, y=17)

                    dateset = Label(Bottom_frame, text="Date:", bg="#DCAE96", font=("verdana", 12, "bold"), width=15,
                                    height=3, relief=GROOVE)
                    dateset.place(x=900, y=19)
                    timeflow()
                    # -------------------------------------------------------------------Add user Frame


                    db_connect()

                    if __name__ == '__main__':
                        w.mainloop()

                runningit()
        else:
            # print("Invalid credentials")
            messagebox.showerror("Failed", "Username or password is incorrect")

    def showit():
        if v.get() == 1:
            password_data.config(show='')
        else:
            password_data.config(show='*')

    r = Toplevel()

    r.title("Employee Management System")
    r.config(bg="grey")
    r.geometry("1100x700")
    r.resizable(False, False)
    k.bind('<FocusOut>', k.withdraw())
    Label_frame = Frame(r, bg="firebrick", bd=5, relief="ridge")
    Label_frame.place(x=1, y=1, width=1099, height=62)
    main_label = Label(Label_frame, text="Employee Management System", bg="firebrick", fg="goldenrod",
                       font=("arial", 22, "bold"))
    main_label.pack(side="top")

    img = (Image.open("Resource/workbench3.jpg"))
    img2 = img.resize((1094, 700))
    img1 = ImageTk.PhotoImage(img2)

    connectdb = Frame(r)
    connectdb.grab_set()
    connectdb.place(x=0, y=62, width=1100, height=900)

    connectdb.config(bg='DarkOrange1')

    l1 = Label(connectdb, image=img1)
    l1.pack(side="top")

    frame = Frame(connectdb, bg="grey97")
    frame.place(x=296, y=220, width=500, height=300)

    imgs = (Image.open("Resource/user.png"))
    imgs1 = imgs.resize((30, 30))
    imgs2 = ImageTk.PhotoImage(imgs1)

    image = (Image.open("Resource/lock.png"))
    image1 = image.resize((30, 30))
    image2 = ImageTk.PhotoImage(image1)
    # ----------------------------------------------------------------------------------------Labels:
    user_root = Label(connectdb, text="Username", bg="grey97", font=("verdana", 12, "bold"),
                      borderwidth=3, width=10, anchor='e')
    user_root.place(x=350, y=320)

    login_img = Label(connectdb, image=imgs2, bg="grey97")
    login_img.place(x=320, y=310, width=40, height=40)

    password = Label(connectdb, text="Password", bg="grey97", font=("verdana", 12, "bold"),
                     borderwidth=3, width=10, anchor='e')
    password.place(x=350, y=380)

    password_img = Label(connectdb, image=image2, bg="grey97")
    password_img.place(x=320, y=370, width=40, height=40)

    # -----------------------------------------------------------------------------------------Entry:

    user_data = Entry(connectdb, font=('Helvetica', 12, 'bold'), bg="grey95", bd=3, width=20)
    user_data.place(x=500, y=320)

    password_data = Entry(connectdb, font=('Helvetica', 12, 'bold'), bg="grey95", bd=3, width=20, show="*")
    password_data.place(x=500, y=380)

    # -------------------------------------------------------------------------------------------------
    v = IntVar()

    show_pass = Checkbutton(connectdb, variable=v, bg="grey97", onvalue=1, offvalue=0, command=showit)
    show_pass.place(x=730, y=380)

    login_button = Button(connectdb, text="Login", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                          width=7, command=procced)
    login_button.place(x=518, y=450)

    if __name__ == '__main__':
        r.mainloop()


def employeerun():
    k.bind('<FocusOut>', k.withdraw())

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

            # ----------------------------------------------------------------------------------------------------------------------
            try:
                point1 = mysql.connector.connect(host='localhost', user='root', password='Yadu2286')
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
                point1 = mysql.connector.connect(host="localhost", user="root", password="anakha",
                                                 database="empdata3")
                console_p1 = point1.cursor()
                strr = 'insert into employeedata3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                console_p1.execute(strr, (
                id, name, mobile, email, address, gender, salary, dob, department, position, addeddate, addedtime))

                strr2 = 'insert into login_credential2 values(%s,%s,%s)'
                console_p1.execute(strr2, (user_name_is, pass_word_is, id))
                point1.commit()

                messagebox.showinfo("Success", "Successfully added user details!")
                # clearing the entry form after adding details to database only if res==true

            except:

                try:
                    # messagebox.showinfo('Notifications', 'Id Already Exist ...')
                    strr2 = 'insert into login_credential2 values(%s,%s,%s) '
                    console_p1.execute(strr2, (user_name_is, pass_word_is, id))
                    point1.commit()

                except:
                    messagebox.showwarning("Warning", "Id already exist!")

            adding.destroy()

        # --------------------------------------------------------------------------------Add button
        add_button = Button(adding, text="ADD", relief="raised", bg="light grey", font=("verdana", 14, "bold"),
                            width=7, command=submitadd)
        add_button.place(x=170, y=630)

    e = Toplevel()
    e.title("Employee Login Page")
    e.geometry("1100x700")
    e.resizable(False, False)

    def main_frames():
        k.bind('<FocusOut>', k.withdraw())
        def displayit():

            k = []
            global point, console_p
            point = mysql.connector.connect(host="localhost", user="root", password="Yadu2286", database="empdata3")
            console_p = point.cursor()
            command = "select * from employeedata3 where id = %s "
            values = [id_data.get()]
            console_p.execute(command, values)
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

        def returning():
            e.destroy()
            k.deiconify()

        Label_frame = Frame(e, bg="firebrick", bd=5, relief="ridge")
        Label_frame.place(x=0, y=0, width=1102, height=102)

        dashboard_label = Label(Label_frame, text="DASHBOARD", bg="firebrick", fg="goldenrod", relief=RIDGE,
                                font=("arial", 22, "bold"), width=1099, height=50)
        dashboard_label.place(x=0, y=0, width=1099, height=50)
        dashboard_label.pack(side='top')



        welcome_frame = Frame(e, bg="peach puff", bd=2, relief=RIDGE)
        welcome_frame.place(x=0, y=100, width=1100, height=153)

        return_button = Button(Label_frame, text="Go Back", relief="raised", bg="firebrick", font=("verdana", 11, "bold"),
                              width=7, command=returning)
        return_button.place(x=1000, y=30)

        welcome_label = Label(welcome_frame, text="Hello...!", bg="peach puff", fg="firebrick",
                              font=("arial", 22, "bold"), width=1099, height=50, anchor='sw')
        welcome_label.place(x=50, y=50, width=160, height=50)

        # ==================================================================
        dateset = Label(welcome_frame, text="Date:", bg="peach puff", font=("verdana", 12, "bold"), width=15, height=3,
                        relief=GROOVE)
        dateset.place(x=900, y=50)
        timeflow()

        # ==================================================================

        employee_details = Frame(e, bg="navajo white", bd=2, relief=RIDGE)
        employee_details.place(x=0, y=253, width=1100, height=446)

        sub_container = Frame(employee_details, bg="navajo white", relief=GROOVE)
        sub_container.place(x=100, y=30, width=900, height=389)

        id_label = Label(sub_container, text="ID: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        name_label = Label(sub_container, text="Name: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        mobile_label = Label(sub_container, text="Mobile: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        email_label = Label(sub_container, text="Email: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        address_label = Label(sub_container, text="Address: ", bg="navajo white", fg="black",
                              font=("arial", 20, "bold"))
        gender_label = Label(sub_container, text="Gender: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        salary_label = Label(sub_container, text="Salary: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        position_label = Label(sub_container, text="Position: ", bg="navajo white", fg="black",
                               font=("arial", 20, "bold"))
        dob_label = Label(sub_container, text="DOB: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        department_label = Label(sub_container, text="Department: ", bg="navajo white", fg="black",
                                 font=("arial", 20, "bold"))
        date_label = Label(sub_container, text="Date: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))
        time_label = Label(sub_container, text="Time: ", bg="navajo white", fg="black", font=("arial", 20, "bold"))

        id_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        name_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        mobile_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        email_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        address_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        gender_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        salary_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        position_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        dob_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        department_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        date_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)
        time_container = Entry(sub_container, font=('Helvetica', 13, 'bold'), bg="grey95", bd=3, width=20)

        id_container.grid(row=0, column=1, padx=20, pady=20)
        name_container.grid(row=0, column=3, padx=20, pady=20)
        mobile_container.grid(row=1, column=1, padx=20, pady=20)
        email_container.grid(row=1, column=3, padx=20, pady=20)
        address_container.grid(row=2, column=1, padx=20, pady=20)
        gender_container.grid(row=2, column=3, padx=20, pady=20)
        salary_container.grid(row=3, column=1, padx=20, pady=20)
        dob_container.grid(row=3, column=3, padx=20, pady=20)
        department_container.grid(row=4, column=1, padx=20, pady=20)
        position_container.grid(row=4, column=3, padx=20, pady=20)

        id_label.grid(row=0, column=0, padx=20, pady=20)
        name_label.grid(row=0, column=2, padx=20, pady=20)
        mobile_label.grid(row=1, column=0, padx=20, pady=20)
        email_label.grid(row=1, column=2, padx=20, pady=20)
        address_label.grid(row=2, column=0, padx=20, pady=20)
        gender_label.grid(row=2, column=2, padx=20, pady=20)
        salary_label.grid(row=3, column=0, padx=20, pady=20)
        dob_label.grid(row=3, column=2, padx=20, pady=20)
        department_label.grid(row=4, column=0, padx=20, pady=20)
        position_label.grid(row=4, column=2, padx=20, pady=20)

        displayit()

    # -------------------------------------------------------------------------------------------------------------------
    def procced():
        point = mysql.connector.connect(host="localhost", user="root", password="anakha", database="empdata3")
        main_cursor = point.cursor()
        command = " select * from login_credential2 where user_name = %s and password = %s and user_id = %s"
        values = (user_data.get(), password_data.get(), id_data.get())
        main_cursor.execute(command, values)
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
            password_data.config(show='')
        else:
            password_data.config(show='*')

    Label_frame = Frame(e, bg="firebrick", bd=5, relief="ridge")
    Label_frame.place(x=1, y=1, width=1099, height=62)
    main_label = Label(Label_frame, text="Employee Login Page", bg="firebrick", fg="goldenrod",
                       font=("arial", 22, "bold"))
    main_label.pack(side="top")

    img = (Image.open("Resource/workbench4.jfif"))
    img2 = img.resize((1094, 700))
    img1 = ImageTk.PhotoImage(img2)

    connectd = Frame(e)
    connectd.place(x=0, y=62, width=1100, height=900)

    connectd.config(bg='DarkOrange')

    l1 = Label(connectd, image=img1)
    l1.pack(side="top")

    imgs = (Image.open("Resource/user.png"))
    imgs1 = imgs.resize((30, 30))
    imgs2 = ImageTk.PhotoImage(imgs1)

    image = (Image.open("Resource/lock.png"))
    image1 = image.resize((30, 30))
    image2 = ImageTk.PhotoImage(image1)

    user_root = Label(e, text="Username", bg="grey92", font=("verdana", 12, "bold"),
                      borderwidth=3, width=10, anchor='e')
    user_root.place(x=390, y=280)

    login_img = Label(e, image=imgs2, bg="grey90")
    login_img.place(x=360, y=275, width=40, height=40)

    password = Label(e, text="Password", bg="grey92", font=("verdana", 12, "bold"),
                     borderwidth=3, width=10, anchor='e')
    password.place(x=390, y=340)

    id_val = Label(e, text="Employee ID", bg="grey92", font=("verdana", 12, "bold"),
                   borderwidth=3, width=10, anchor='e')
    id_val.place(x=390, y=400)

    password_img = Label(e, image=image2, bg="grey90")
    password_img.place(x=360, y=335, width=40, height=40)

    # -----------------------------------------------------------------------------------------Entry:

    user_data = Entry(e, font=('Helvetica', 12, 'bold'), bg="grey85", bd=3, width=20)
    user_data.place(x=540, y=280)

    password_data = Entry(e, font=('Helvetica', 12, 'bold'), bg="grey85", bd=3, width=20, show="*")
    password_data.place(x=540, y=340)

    id_data = Entry(e, font=('Helvetica', 12, 'bold'), bg="grey85", bd=3, width=20)
    id_data.place(x=540, y=400)

    # -------------------------------------------------------------------------------------------------
    v = IntVar()

    show_pass = Checkbutton(e, variable=v, bg="grey97", onvalue=1, offvalue=0, command=showit)
    show_pass.place(x=740, y=340)

    login_button = Button(e, text="Login", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                          width=7, command=procced)
    login_button.place(x=450, y=480)

    registration_button = Button(e, text="New User?", relief="raised", bg="light grey", font=("verdana", 11, "bold"),
                                 width=9, command=add_user)
    registration_button.place(x=570, y=480)

    e.mainloop()


def customerrun():

    def customerrun1():

        def customerrun22():
            point = mysql.connector.connect(host="localhost", user="root", password="anakha", database="empdata3")
            main_cursor = point.cursor()
            command = " select * from login_credential2 where user_name = %s and password = %s"
            values = (userenter.get(), passenter.get())
            main_cursor.execute(command, values)
            rel = main_cursor.fetchall()
            if rel:
                for i in rel:
                    messagebox.showinfo("Success", "LOGIN SUCCESSFULL !!")

                    def runningit():
                        top.bind('<FocusOut>', top.withdraw())

                        class Employee:
                            def __init__(self, root):
                                self.root = root
                                self.root.geometry("1530x790+0+0")
                                self.root.title("employee management")

                                # variables
                                self.var_cat = StringVar()
                                self.var_name = StringVar()
                                self.var_cat_name = StringVar()
                                self.var_email = StringVar()
                                self.var_address = StringVar()
                                self.var_married = StringVar()
                                self.var_dob = StringVar()
                                self.var_doj = StringVar()
                                self.var_idproofcomb = StringVar()
                                self.var_idproof = StringVar()
                                self.var_gender = StringVar()
                                self.var_phone = StringVar()
                                self.var_country = StringVar()
                                self.var_prod_amount = StringVar()

                                lbl_title = Label(self.root, text="CUSTOMER MANAGEMENT",
                                                  font=("times to newroman", 37, "bold"),
                                                  fg="red", bg="white")
                                lbl_title.place(x=0, y=0, width=1530, height=50)
                                ##logo
                                img_logo = Image.open('Resource/emp4.jpg')
                                img_logo = img_logo.resize((540, 160), Image.ANTIALIAS)
                                self.photo_logo = ImageTk.PhotoImage(img_logo)

                                self.logo = Label(self.root, image=self.photo_logo)
                                self.logo.place(x=270, y=0, width=50, height=50)
                                # image frame
                                img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
                                img_frame.place(x=0, y=50, width=1530, height=160)

                                # 1st
                                img1 = Image.open('Resource/emp6.jpeg')
                                img1 = img1.resize((540, 160), Image.ANTIALIAS)
                                self.photo1 = ImageTk.PhotoImage(img1)

                                self.img_1 = Label(img_frame, image=self.photo1)
                                self.img_1.place(x=0, y=0, width=540, height=160)
                                # 2nd
                                img_2 = Image.open('Resource/emp5.jpeg')
                                img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
                                self.photo2 = ImageTk.PhotoImage(img_2)

                                self.img_2 = Label(img_frame, image=self.photo2)
                                self.img_2.place(x=540, y=0, width=540, height=160)

                                # 3rd
                                img_3 = Image.open('Resource/emp7.png')
                                img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
                                self.photo3 = ImageTk.PhotoImage(img_3)

                                self.img_3 = Label(img_frame, image=self.photo3)
                                self.img_3.place(x=1000, y=0, width=540, height=160)

                                # MAIN FRAME
                                Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
                                Main_frame.place(x=10, y=220, width=1500, height=560)
                                # upper frame
                                upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                                         text="CUSTOMER INFORMATION",
                                                         font=('times new roman', 37, 'bold'),
                                                         fg='red')

                                upper_frame.place(x=10, y=10, width=1480, height=270)

                                # labels and entry FIELDS

                                lbl_dep = Label(upper_frame, text='CATEGORY', font=('arial', 12, 'bold'), bg='white')
                                lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

                                # combobox
                                combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_cat,
                                                         font=('arial', 12, 'bold'),
                                                         width=17, state='readonly')
                                combo_dep['value'] = ("select cateogry", 'sotwarepro', 'service', 'manitanance')
                                combo_dep.current(0)

                                combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)
                                # name
                                lbl_Name = Label(upper_frame, font=("arial", 12, "bold"), text="NAME", bg="white")
                                lbl_Name.grid(row=0, column=2, sticky=W, padx=2, ipady=7)

                                txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22,
                                                     font=("arial", 12, "bold"))
                                txt_name.grid(row=0, column=3, padx=2, pady=7)

                                ##lbl_Designation

                                lbl_Desigination = Label(upper_frame, font=("arial", 12, "bold"), text="productname",
                                                         bg="white")
                                lbl_Desigination.grid(row=1, column=0, sticky=W, padx=2, pady=7)

                                txt_Desigination = ttk.Entry(upper_frame, textvariable=self.var_cat_name, width=22,
                                                             font=("arial", 12, "bold"))
                                txt_Desigination.grid(row=1, column=1, sticky=W, padx=2, pady=7)

                                # email

                                lbl_email = Label(upper_frame, font=("arial", 12, "bold"), text="EMAIL", bg="white")
                                lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

                                txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=22,
                                                      font=("arial", 12, "bold"))
                                txt_email.grid(row=1, column=3, padx=2, pady=7)

                                # address

                                lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="ADDRESS", bg="white")
                                lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

                                txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22,
                                                        font=("arial", 12, "bold"))
                                txt_address.grid(row=2, column=1, padx=2, pady=7)

                                ##married

                                lbl_married_status = Label(upper_frame, font=("arial", 12, "bold"),
                                                           text="MARRIED STATUS",
                                                           bg="white")
                                lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

                                com_txt_married = ttk.Combobox(upper_frame, textvariable=self.var_married, width=22,
                                                               font=("arial", 12, "bold"), state="readonly")
                                com_txt_married['values'] = ("select status", "Married", "unmarried")
                                com_txt_married.current(0)
                                com_txt_married.grid(row=2, column=3, sticky=W, padx=2, pady=7)
                                ###DOB
                                lbl_dob = Label(upper_frame, font=("arial", 12, "bold"), text="DOB:", bg="white")
                                lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

                                txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob, width=22,
                                                    font=("arial", 12, "bold"))
                                txt_dob.grid(row=3, column=1, padx=2, pady=7)
                                ##doj
                                lbl_doj = Label(upper_frame, font=("arial", 12, "bold"), text="DOJ:", bg="white")
                                lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

                                txt_doj = ttk.Entry(upper_frame, textvariable=self.var_doj, width=22,
                                                    font=("arial", 12, "bold"))
                                txt_doj.grid(row=3, column=3, padx=2, pady=7)

                                ##idproof

                                com_txt_proof = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb,
                                                             state="readonly",
                                                             font=("arial", 12, "bold"), width=15)
                                com_txt_proof['values'] = ("select id proof", "pan card", "drivinglicence")
                                com_txt_proof.current(0)
                                com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)

                                txt_proof = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22,
                                                      font=("arial", 11, "bold"))
                                txt_proof.grid(row=4, column=1, padx=2, pady=7)

                                ##gender

                                lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="GENDER", bg="white")
                                lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)

                                com_txt_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, width=22,
                                                              font=("arial", 12, "bold"), state="readonly")

                                com_txt_gender['values'] = ("select gender", "Male", "Female", "Other")
                                com_txt_gender.current(0)
                                com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

                                # phone
                                lbl_doj = Label(upper_frame, font=("arial", 12, "bold"), text="PHNO:", bg="white")
                                lbl_doj.grid(row=0, column=4, sticky=W, padx=2, pady=7)

                                txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22,
                                                      font=("arial", 11, "bold"))
                                txt_phone.grid(row=0, column=5, padx=2, pady=7)

                                # country

                                lbl_country = Label(upper_frame, font=("arial", 12, "bold"), text="COUNTRY:",
                                                    bg="white")
                                lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

                                txt_country = ttk.Entry(upper_frame, textvariable=self.var_country, width=22,
                                                        font=("arial", 11, "bold"))
                                txt_country.grid(row=1, column=5, padx=2, pady=7)
                                ##salary
                                lbl_ctc = Label(upper_frame, font=("arial", 12, "bold"), text="AMOUNT", bg="white")
                                lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

                                txt_ctc = ttk.Entry(upper_frame, textvariable=self.var_prod_amount, width=22,
                                                    font=("arial", 11, "bold"))
                                txt_ctc.grid(row=2, column=5, padx=2, pady=7)

                                ###button frame
                                button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
                                button_frame.place(x=1100, y=10, width=170, height=210)

                                btn_add = Button(button_frame, text="save", command=self.add_data,
                                                 font=("arial", 15, "bold"),
                                                 width=13, bg='blue', fg="white")
                                btn_add.grid(row=0, column=0, padx=1, pady=5)

                                btn_update = Button(button_frame, text="update", command=self.update_data,
                                                    font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
                                btn_update.grid(row=1, column=0, padx=1, pady=5)

                                btn_delete = Button(button_frame, text="delete", command=self.delete_data,
                                                    font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
                                btn_delete.grid(row=2, column=0, padx=1, pady=5)

                                btn_clear = Button(button_frame, command=self.reset_data, text="clear",
                                                   font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
                                btn_clear.grid(row=3, column=0, padx=1, pady=5)

                                # down frame
                                down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white',
                                                        text="CUSTOMER INFORMATION",
                                                        font=('times new roman', 25, 'bold'), fg='red')

                                down_frame.place(x=10, y=280, width=1480, height=300)
                                # search fRMANE
                                search_frmae = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                                          text="CUSTOMER information",
                                                          font=('times new roman', 25, 'bold'),
                                                          fg='red')
                                search_frmae.place(x=0, y=0, width=1470, height=80)

                                search_by = Label(search_frmae, font=("arial", 12, "bold"), text="search by",
                                                  fg="white",
                                                  bg='red')
                                search_by.grid(row=0, column=0, sticky=W, padx=5)

                                # search
                                self.var_com_search = StringVar()
                                com_txt_search = ttk.Combobox(search_frmae, textvariable=self.var_com_search,
                                                              font=('arial', 12, 'bold'), width=17, state='readonly')
                                com_txt_search['value'] = ("select option", 'phone', 'id')
                                com_txt_search.current(0)

                                com_txt_search.grid(row=0, column=1, padx=5, sticky=W)
                                self.var_search = StringVar()

                                txt_search = ttk.Entry(search_frmae, textvariable=self.var_search, width=22,
                                                       font=("arial", 11, "bold"))
                                txt_search.grid(row=0, column=2, padx=5)

                                btn_search = Button(search_frmae, text="search", font=("arial", 11, "bold"), width=14)
                                btn_search.grid(row=0, column=3, padx=5)

                                btn_showAll = Button(search_frmae, text="show all", font=("arial", 11, "bold"),
                                                     width=10)
                                btn_showAll.grid(row=0, column=4, padx=5)

                                # ======employee=======
                                # table
                                table_frame = Frame(down_frame, bd=2, relief=RIDGE)
                                table_frame.place(x=0, y=80, width=1320, height=80)

                                scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
                                scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

                                self.employee_table = ttk.Treeview(table_frame, column=(
                                    'cat', 'name', 'cat_name', 'email', 'address', 'married', 'dob', 'doj',
                                    "idproofcomb",
                                    'idproof', 'gender', 'phone', 'country', 'prod_amount',),
                                                                   xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y.set)

                                scroll_x.pack(side=BOTTOM, fill=X)
                                scroll_y.pack(side=RIGHT, fill=Y)

                                scroll_x.config(command=self.employee_table.xview)
                                scroll_y.config(command=self.employee_table.yview)

                                self.employee_table.heading('cat', text='Category')
                                self.employee_table.heading('name', text='Name')
                                self.employee_table.heading('cat_name', text='CateName')
                                self.employee_table.heading('email', text='email')
                                self.employee_table.heading('address', text='Address')
                                self.employee_table.heading('married', text='married status')
                                self.employee_table.heading('dob', text='DOB')
                                self.employee_table.heading('doj', text='DOJ')
                                self.employee_table.heading('idproofcomb', text='ID Type')
                                self.employee_table.heading('idproof', text='ID Proof')
                                self.employee_table.heading('gender', text='Gender')
                                self.employee_table.heading('phone', text='phone')
                                self.employee_table.heading('country', text='Country')
                                self.employee_table.heading('prod_amount', text='ProAmount')

                                self.employee_table['show'] = 'headings'
                                self.employee_table.column('cat', width=100)
                                self.employee_table.column('name', width=100)
                                self.employee_table.column('cat_name', width=100)
                                self.employee_table.column('email', width=100)
                                self.employee_table.column('address', width=100)
                                self.employee_table.column('married', width=100)
                                self.employee_table.column('dob', width=100)
                                self.employee_table.column('doj', width=100)
                                self.employee_table.column('idproofcomb', width=100)
                                self.employee_table.column('idproof', width=100)
                                self.employee_table.column('gender', width=100)
                                self.employee_table.column('phone', width=100)
                                self.employee_table.column('country', width=100)
                                self.employee_table.column('prod_amount', width=100)

                                self.employee_table.pack(fill=BOTH, expand=1)
                                self.employee_table.bind("<ButtonRelease>", self.get_cursor)
                                self.fetch_data()
                                ####function declaration####

                            def add_data(self):
                                if self.var_cat.get() == "" or self.var_email.get() == "":
                                    messagebox.showerror('error', 'all fields are required')
                                else:
                                    try:
                                        conn = mysql.connector.connect(host='localhost', username='root',
                                                                       password='anakha',
                                                                       database='empdata3')
                                        my_cursor = conn.cursor()
                                        my_cursor.execute(
                                            'insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                                                self.var_cat.get(),
                                                self.var_name.get(),
                                                self.var_cat_name.get(),
                                                self.var_email.get(),
                                                self.var_address.get(),
                                                self.var_married.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_idproofcomb.get(),
                                                self.var_idproof.get(),
                                                self.var_gender.get(),
                                                self.var_phone.get(),
                                                self.var_country.get(),
                                                self.var_prod_amount.get()))
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()
                                        messagebox.showinfo('success', 'customer added has been added',
                                                            parent=self.root)

                                    except Exception as es:
                                        messagebox.showerror('Error', f'due to :{str(es)}', parent=self.root)

                            # fetch data
                            def fetch_data(self):
                                conn = mysql.connector.connect(host='localhost', username='root', password='anakha',
                                                               database='empdata3')
                                my_cursor = conn.cursor()
                                my_cursor.execute('select * from customer')
                                data = my_cursor.fetchall()
                                if len(data) != 0:
                                    self.employee_table.delete(*self.employee_table.get_children())
                                    for i in data:
                                        self.employee_table.insert("", END, values=i)
                                    conn.commit()
                                conn.close()

                            # GET CURSOR

                            def get_cursor(self, event=""):
                                cursor_row = self.employee_table.focus()
                                content = self.employee_table.item(cursor_row)
                                data = content['values']
                                self.var_cat.set(data[0])
                                self.var_name.set(data[1])
                                self.var_cat_name.set(data[2])
                                self.var_email.set(data[3])
                                self.var_address.set(data[4])
                                self.var_married.set(data[5])
                                self.var_dob.set(data[6])
                                self.var_doj.set(data[7])
                                self.var_idproofcomb.set(data[8])
                                self.var_idproof.set(data[9])
                                self.var_gender.set(data[10])
                                self.var_phone.set(data[11])
                                self.var_country.set(data[12])
                                self.var_prod_amount.set(data[13])

                            def update_data(self):
                                if self.var_cat.get() == "" or self.var_email.get() == "":
                                    messagebox.showerror('error', 'all fields are required')
                                else:
                                    try:
                                        update = messagebox.askyesno('update', 'are you shure update customer data')
                                        if update > 0:
                                            conn = mysql.connector.connect(host='localhost', username='root',
                                                                           password='anakha',
                                                                           database='empdata3')
                                            my_cursor = conn.cursor()
                                            my_cursor.execute(
                                                'update customer set cate=%s, name=%s, cat_name=%s, email=%s, address=%s, married=%s, dob=%s, doj=%s, idproofcomb=%s, gender=%s, phone=%s, country=%s, prod_amount=%s where idproof=%s',
                                                (

                                                    self.var_cat.get(),
                                                    self.var_name.get(),
                                                    self.var_cat_name.get(),
                                                    self.var_email.get(),
                                                    self.var_address.get(),
                                                    self.var_married.get(),
                                                    self.var_dob.get(),
                                                    self.var_doj.get(),
                                                    self.var_idproofcomb.get(),

                                                    self.var_gender.get(),
                                                    self.var_phone.get(),
                                                    self.var_country.get(),
                                                    self.var_prod_amount.get(),
                                                    self.var_idproof.get(),

                                                ))
                                        else:
                                            if not update:
                                                return
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()
                                        messagebox.showinfo("success", "customer update success", parent=self.root)
                                    except Exception as es:
                                        messagebox.showerror('Error', f'due to :{str(es)}', parent=self.root)

                            def delete_data(self):
                                if self.var_idproof.get() == "":
                                    messagebox.showerror('Error', 'all field are require')

                                else:
                                    try:
                                        Delete = messagebox.askyesno('Delete', 'are you sure delete  this customer',
                                                                     parent=self.root)
                                        if Delete > 0:
                                            conn = mysql.connector.connect(host='localhost', username='root',
                                                                           password='anakha',
                                                                           database='empdata3')
                                            my_cursor = conn.cursor()
                                            sql = 'delete from customer where idproof=%s'
                                            value = (self.var_idproof.get(),)
                                            my_cursor.execute(sql, value)
                                        else:
                                            if not Delete:
                                                return
                                        conn.commit()
                                        self.fetch_data()
                                        conn.close()
                                        messagebox.showinfo("delete", "customer delete success", parent=self.root)
                                    except Exception as es:
                                        messagebox.showerror('Error', f'due to :{str(es)}', parent=self.root)

                            def reset_data(self):
                                self.var_cat.set("select cateogry")
                                self.var_name.set("")
                                self.var_cat_name.set("")
                                self.var_email.set("")
                                self.var_address.set("")
                                self.var_married.set("married status")
                                self.var_dob.set("")
                                self.var_doj.set("")
                                self.var_idproofcomb.set("select id proof")
                                self.var_idproof.set("")
                                self.var_gender.set("")
                                self.var_phone.set("")
                                self.var_country.set("")
                                self.var_prod_amount.set("")

                            def search_data(self):
                                if self.var_com_search.get() == '' or self.var_search.get() == '':
                                    messagebox.showerror('Error', 'please select option')
                                else:
                                    try:
                                        conn = mysql.connector.connect(host='localhost', username='root',
                                                                       password='anakha',
                                                                       database='empdata3')
                                        my_cursor = conn.cursor()
                                        my_cursor.execute(
                                            'select * from customer where' + str(
                                                self.var_com_search.get()) + " LIKE'%" + str(
                                                self.var_search.get() + "%'"))
                                        rows = my_cursor.fetchall()
                                        if len(rows) != 0:
                                            self.employee_table.delete(*self.employee_table.get_children())
                                            for i in rows:
                                                self.employee_table.insert("", END, values=i)
                                        conn.commit
                                        conn.close()
                                    except Exception as es:
                                        messagebox.showerror('Error', f'due to :{str(es)}', parent=self.root)

                        if __name__ == "__main__":
                            root1 = Toplevel()
                            obj = Employee(root1)
                            root1.mainloop()

                    runningit()

            else:
                # print("Invalid credentials")
                messagebox.showerror("Failed", "Username or password is incorrect")

        def showit():
            if v.get() == 1:
                passenter.config(show='')
            else:
                passenter.config(show='*')

        top = Toplevel()
        top.geometry('800x400')
        top.resizable(False, False)
        top.title("Customer Details login page")

        image1 = (Image.open("Resource/back3.jpg"))
        image2 = image1.resize((800, 400))
        image3 = ImageTk.PhotoImage(image2)

        img_label = Label(top, image=image3)
        img_label.place(x=0, y=0)

        login_frame = Frame(top, bg="grey20", highlightbackground="white", highlightthickness=2)
        login_frame.place(x=160, y=60, width=500, height=250)

        userlabel = Label(login_frame, text="Username: ", fg="white", bg="grey20", font=('times', 15, 'bold'), width=10)
        userlabel.place(x=50, y=60)

        passlabel = Label(login_frame, text="Password: ", fg="white", bg="grey20", font=('times', 15, 'bold'), width=10)
        passlabel.place(x=50, y=130)

        userenter = Entry(login_frame, font=('times', 15, 'bold'), bd=3, width=15)
        userenter.place(x=250, y=58)

        passenter = Entry(login_frame, font=('times', 15, 'bold'), bd=3, width=15, show="*")
        passenter.place(x=250, y=128)

        v = IntVar()
        check_box = Checkbutton(login_frame, bg="grey20", variable=v, onvalue=1, offvalue=0, command=showit)
        check_box.place(x=450, y=135)

        loginbutn = Button(login_frame, text="Login", font=('times', 13, 'bold'), width=5, relief=RAISED, bd=5,
                           command=customerrun22)
        loginbutn.place(x=220, y=190)

        top.mainloop()

    #=========================================================================================================================
    def billrun():

        def customerrun22():
            point = mysql.connector.connect(host="localhost", user="root", password="anakha", database="empdata3")
            main_cursor = point.cursor()
            command = " select * from login_credential2 where user_name = %s and password = %s"
            values = (userenter.get(), passenter.get())
            main_cursor.execute(command, values)
            rel = main_cursor.fetchall()
            if rel:
                for i in rel:
                    messagebox.showinfo("Success", "LOGIN SUCCESSFULL !!")

                    def runningit():
                        top.bind('<FocusOut>', top.withdraw())
                        top.bind('<FocusOut>', top.withdraw())
                        top.bind('<FocusOut>', top.withdraw())

                        class Bill_App:
                            def __init__(self, root):
                                self.root = root
                                self.root.geometry("1570x1200+0+0")
                                self.root.title("Billing Software")
                                self.input_value = True

                                # variables
                                self.product = StringVar()
                                self.prices = IntVar()
                                self.qty = IntVar()
                                self.sub_total = StringVar()
                                self.tax_input = StringVar()
                                self.total = StringVar()

                                # ===================Total product price & tax variables===============
                                self.clothing_price = StringVar()
                                self.lifestyle_price = StringVar()
                                self.mobiles_price = StringVar()

                                self.clothing_tax = StringVar()
                                self.lifestyle_tax = StringVar()
                                self.mobiles_tax = StringVar()

                                #  Customer
                                self.c_name = StringVar()
                                self.c_phon = StringVar()
                                self.bill_no = StringVar()
                                self.c_email = StringVar()
                                x = random.randint(1000, 9999)
                                self.bill_no.set(str(x))
                                self.search_bill = StringVar()

                                # Product categories lists
                                self.Category = ['Select Option', 'Clothing', 'LifeStyle', 'Mobiles']

                                self.ClothingSubCat = ['Pant', 'T-Shirt', 'Shirt']
                                self.Pant = ['Levis', 'Mufti', 'Spykar']
                                self.price_pant = 5000
                                self.price_pantlocal = 7000
                                self.price_pantmax = 8000
                                self.T_shirt = ['Polo', 'Roadster', 'Jack&Jones']
                                self.price_polo = 1500
                                self.price_Roadster = 1800
                                self.price_JackJones = 1700
                                self.Shirt = ['Peter England', 'Louis Phillipe', 'Park Avenue']
                                self.price_Peter = 2100
                                self.price_Louis = 2700
                                self.price_Park = 1740

                                self.LifStyleSubCat = ['Bath Soap', 'Face Creame', 'Hair Oil']
                                self.Bath_soap = ['LifeBoy', 'Lux', 'Santoor', 'Pears']
                                self.price_life = float(20)
                                self.price_lux = 20
                                self.price_santoor = 20
                                self.price_pearl = 30

                                self.Face_creame = ['Fair&Lovely', 'Ponds', 'Olay', 'Garnier']
                                self.price_fair = 20
                                self.price_ponds = 20
                                self.price_olay = 20
                                self.price_garnier = 30

                                self.Hair_oil = ['Parachute', 'Jashmin', 'Bajaj']
                                self.price_para = 25
                                self.price_jashmin = 22
                                self.price_bajaj = 30

                                self.MobilesSubCat = ['Iphone', 'Sumsung', 'Xiome', 'RealMe', "One+"]
                                self.Iphone = ['Iphone_X', 'Iphone_11', 'Iphone_12']
                                self.price_ix = 40000
                                self.price_i11 = 60000
                                self.price_i12 = 85000

                                self.Samsung = ['Samsung M16', 'Sumsung M12', 'Sumsung M21']
                                self.price_sm16 = 16000
                                self.price_sm12 = 12000
                                self.price_sm21 = 18000

                                self.Xiome = ['Red11', 'Redme-12', 'RedmePro']
                                self.price_r11 = 11000
                                self.price_r12 = 12000
                                self.price_rpro = 9000

                                self.RealMe = ['RealMe 12', 'RealMe 13', 'RealMe Pro']
                                self.price_rel12 = 25000
                                self.price_rel13 = 22000
                                self.price_relpro = 30000

                                self.OnePlus = ['OnePlus1', 'OnePlus2', 'OnePlus3']
                                self.price_one1 = 45000
                                self.price_one12 = 60000
                                self.price_one3 = 45800

                                # Images
                                img10 = Image.open("Resource/pay.png")
                                img10 = img10.resize((500, 130), Image.ANTIALIAS)
                                self.photoImg10 = ImageTk.PhotoImage(img10)
                                bg_lbl = Label(self.root, image=self.photoImg10)
                                bg_lbl.place(x=0, y=0, width=500, height=130)

                                img11 = Image.open("Resource/phonp.png")
                                img11 = img11.resize((500, 130), Image.ANTIALIAS)
                                self.photoImg11 = ImageTk.PhotoImage(img11)
                                bg_lbl = Label(self.root, image=self.photoImg11)
                                bg_lbl.place(x=500, y=0, width=500, height=130)

                                img13 = Image.open("Resource/paytm.png")
                                img13 = img13.resize((500, 130), Image.ANTIALIAS)
                                self.photoImg13 = ImageTk.PhotoImage(img13)
                                bg_lbl = Label(self.root, image=self.photoImg13)
                                bg_lbl.place(x=1000, y=0, width=500, height=130)

                                # Project title
                                title = Label(self.root, text="........BILLING.......",
                                              font=("times new roman", 35, "bold"),
                                              bg="white", fg="red")
                                title.place(x=0, y=130, width=1540, height=45)

                                def time():
                                    string = strftime('%H:%M:%S %p')
                                    lbl.config(text=string)
                                    lbl.after(1000, time)

                                lbl = Label(title, font=('times new roman', 16, 'bold'), background='white',
                                            foreground='blue')
                                lbl.place(x=0, y=(-15), width=120, height=50)
                                time()

                                self.bg_color = "white"

                                Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg=self.bg_color)
                                Main_Frame.place(x=0, y=175, width=1535, height=620)

                                # Customer LabelFrame
                                CustFrame = LabelFrame(Main_Frame, text="Customer", bg=self.bg_color, fg="red",
                                                       font=("arial", 12, "bold"))
                                CustFrame.place(x=10, y=0, width=350, height=140)

                                self.lblMobile = Label(CustFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                       text="Mobile No.", bd=4)
                                self.lblMobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)

                                self.txtMobile = ttk.Entry(CustFrame, font=('arial', 10, 'bold'),
                                                           textvariable=self.c_phon,
                                                           width=24)
                                self.txtMobile.grid(row=0, column=1, sticky=W, padx=5, pady=2)

                                self.lblCustName = Label(CustFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                         text="Customer Name", bd=4)
                                self.lblCustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

                                self.txtCustName = ttk.Entry(CustFrame, font=('arial', 10, 'bold'),
                                                             textvariable=self.c_name,
                                                             width=24)
                                self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

                                self.lblEmail = Label(CustFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                      text="Email",
                                                      bd=4)
                                self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

                                self.txtEmail = ttk.Entry(CustFrame, font=('arial', 10, 'bold'),
                                                          textvariable=self.c_email,
                                                          width=24)
                                self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

                                # Product LabelFrame
                                ProductFrame = LabelFrame(Main_Frame, text="Product", bg=self.bg_color, fg="red",
                                                          font=("arial", 12, "bold"))
                                ProductFrame.place(x=370, y=0, width=620, height=140)

                                # search LabelFrame
                                SerachFrame = Frame(Main_Frame, bd=2, bg="white")
                                SerachFrame.place(x=1020, y=10, width=500, height=40)

                                cbill_label = Label(SerachFrame, text="Bill Number", bg="red", fg="white",
                                                    font=("times new roman", 14, "bold")).grid(row=0, column=0)
                                cbill_txt = ttk.Entry(SerachFrame, width=15, textvariable=self.search_bill,
                                                      font="arial 14").grid(row=0, column=1, padx=2)

                                bill_btn = Button(SerachFrame, text="Search", command=self.find_bill, width=18,
                                                  font="arial 11 bold", bg="orangered", fg="white").grid(row=0,
                                                                                                         column=2,
                                                                                                         padx=2)

                                # MiddleFrmae
                                MiddleFame = Frame(Main_Frame, bd=10)
                                MiddleFame.place(x=10, y=150, width=980, height=350)

                                imgm1 = Image.open("Resource/casher.jpg")
                                imgm1 = imgm1.resize((490, 350), Image.ANTIALIAS)
                                self.photoImgm1 = ImageTk.PhotoImage(imgm1)
                                bg_lbl = Label(MiddleFame, image=self.photoImgm1)
                                bg_lbl.place(x=0, y=0, width=490, height=350)

                                imgm2 = Image.open("Resource/shop.jpg")
                                imgm2 = imgm2.resize((490, 350), Image.ANTIALIAS)
                                self.photoImgm2 = ImageTk.PhotoImage(imgm2)
                                bg_lbl = Label(MiddleFame, image=self.photoImgm2)
                                bg_lbl.place(x=490, y=0, width=490, height=350)

                                # Rightlabelframe Bill Area
                                RightFame = LabelFrame(Main_Frame, text="Bill Area ", bd=2, bg='white',
                                                       font=('arial', 12, 'bold'), fg="red")
                                RightFame.place(x=1020, y=45, width=480, height=440)
                                bill_title = Label(RightFame, text="Bill Reciept", fg="blue", bg="white",
                                                   font="arial 15 bold",
                                                   bd=7, relief=GROOVE).pack(fill=X)

                                scroll_y = Scrollbar(RightFame, orient=VERTICAL)
                                self.textarea = Text(RightFame, yscrollcommand=scroll_y.set, bg="white", fg='blue',
                                                     font=('arial', 12, 'bold'))
                                scroll_y.pack(side=RIGHT, fill=Y)
                                scroll_y.config(command=self.textarea.yview)
                                self.textarea.pack(fill=BOTH, expand=1)

                                self.lblCategories = Label(ProductFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                           text="Select Category.", bd=4)
                                self.lblCategories.grid(row=0, column=0, sticky=W, padx=5, pady=2)

                                self.ComboCategories = ttk.Combobox(ProductFrame, value=self.Category,
                                                                    font=('arial', 10, 'bold'), width=24,
                                                                    state="readonly")
                                self.ComboCategories.grid(row=0, column=1, sticky=W, padx=5, pady=2)
                                self.ComboCategories.current(0)
                                self.ComboCategories.bind("<<ComboboxSelected>>", self.Categories)

                                self.lblSubCategory = Label(ProductFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                            text="Subcategory", bd=4)
                                self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

                                self.ComboSubCategory = ttk.Combobox(ProductFrame, state="readonly", value=[""],
                                                                     font=('arial', 10, 'bold'), width=24)
                                self.ComboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
                                self.ComboSubCategory.current(0)
                                self.ComboSubCategory.bind("<<ComboboxSelected>>", self.Product_Add)

                                self.lblproduct = Label(ProductFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                        text="Product Name", bd=4)
                                self.lblproduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

                                self.ComboProduct = ttk.Combobox(ProductFrame, value=[""], textvariable=self.product,
                                                                 state="readonly", font=('arial', 10, 'bold'), width=24)
                                self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
                                self.ComboProduct.bind("<<ComboboxSelected>>", self.price)

                                self.lblPrice = Label(ProductFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                      text="Price",
                                                      bd=4)
                                self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

                                self.ComboPrice = ttk.Combobox(ProductFrame, state="readonly", textvariable=self.prices,
                                                               value=[""], font=('arial', 10, 'bold'), width=24)
                                self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

                                self.lblQty = Label(ProductFrame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                    text="Qty",
                                                    bd=4)
                                self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

                                self.ComboQty = ttk.Entry(ProductFrame, textvariable=self.qty,
                                                          font=('arial', 10, 'bold'),
                                                          width=26)
                                self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

                                # BottomlabelFrmae
                                BottomFame = LabelFrame(Main_Frame, text="Bill Counter", bd=2, bg='white',
                                                        font=('arial', 12, 'bold'), fg="red")
                                BottomFame.place(x=0, y=485, width=1520, height=125)

                                # Total Poduct Price tax
                                self.lblTotal = Label(BottomFame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                      text="Sub Total", bd=4)
                                self.lblTotal.grid(row=0, column=2, sticky=W, padx=5, pady=2)

                                self.txtTotal = ttk.Entry(BottomFame, textvariable=self.sub_total,
                                                          font=('arial', 10, 'bold'),
                                                          width=24)
                                self.txtTotal.grid(row=0, column=3, sticky=W, padx=5, pady=2)

                                self.lbl_tax = Label(BottomFame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                     text=" Tax",
                                                     bd=4)
                                self.lbl_tax.grid(row=1, column=2, sticky=W, padx=5, pady=2)

                                self.txt_tax = ttk.Entry(BottomFame, font=('arial', 10, 'bold'),
                                                         textvariable=self.tax_input,
                                                         width=24)
                                self.txt_tax.grid(row=1, column=3, sticky=W, padx=5, pady=2)

                                self.lblAmountTotal = Label(BottomFame, font=('arial', 12, 'bold'), bg=self.bg_color,
                                                            text="Total", bd=4)
                                self.lblAmountTotal.grid(row=2, column=2, sticky=W, padx=5, pady=2)

                                self.txtAmountTotal = ttk.Entry(BottomFame, font=('arial', 10, 'bold'),
                                                                textvariable=self.total,
                                                                width=24)
                                self.txtAmountTotal.grid(row=2, column=3, sticky=W, padx=5, pady=2)

                                # Buttons
                                btnFrame = Frame(BottomFame, bd=2, bg=self.bg_color)
                                btnFrame.place(x=320, y=0)

                                self.btn_AddToCart = Button(btnFrame, height=2, text="Add To Cart",
                                                            command=self.iaddItem,
                                                            width=15, bg="orangered", fg="white",
                                                            font=('arial', 15, 'bold'))
                                self.btn_AddToCart.grid(row=0, column=0, padx=1, pady=5)

                                self.btn_generate_bill = Button(btnFrame, height=2, text="Generate Bill",
                                                                command=self.gen_bill,
                                                                width=15, bg="orangered", fg="white",
                                                                font=('arial', 15, 'bold'))
                                self.btn_generate_bill.grid(row=0, column=1, padx=1, pady=5)

                                self.btn_save = Button(btnFrame, height=2, text="Save Bill", command=self.save_bill,
                                                       width=15,
                                                       bg="orangered", fg="white", font=('arial', 15, 'bold'))
                                self.btn_save.grid(row=0, column=2, padx=1, pady=5)

                                self.btn_save = Button(btnFrame, height=2, text="Print", command=self.iPrint, width=15,
                                                       bg="orangered", fg="white", font=('arial', 15, 'bold'))
                                self.btn_save.grid(row=0, column=3, padx=1, pady=5)

                                self.btn_Clear = Button(btnFrame, height=2, text="Clear", command=self.clear, width=15,
                                                        bg="orangered", fg="white", font=('arial', 15, 'bold'))
                                self.btn_Clear.grid(row=0, column=4, padx=1, pady=5)

                                self.btn_Exit = Button(btnFrame, height=2, command=self.root.destroy, text="Exit",
                                                       width=15,
                                                       bg="orangered", fg="white", font=('arial', 15, 'bold'))
                                self.btn_Exit.grid(row=0, column=5, padx=1, pady=5)

                                self.welcome()

                                self.l = []

                            def clear(self):
                                self.textarea.delete(1.0, END)
                                self.c_name.set("")
                                self.c_phon.set("")
                                # self.bill_no.set("")
                                self.c_email.set("")
                                x = random.randint(1000, 9999)
                                self.bill_no.set(str(x))
                                # self.search_bill.set("")
                                self.product.set("")
                                self.prices.set(0)
                                self.qty.set(0)
                                self.l = [0]
                                self.total.set("")
                                self.sub_total.set("")
                                self.tax_input.set('')
                                self.welcome()

                            def iPrint(self):
                                q = self.textarea.get("1.0", "end-1c")
                                filename = tempfile.mktemp(".txt")
                                open(filename, "w").write(q)
                                os.startfile(filename, "print")

                            def welcome(self):
                                self.textarea.delete(1.0, END)
                                self.textarea.insert(END, "\t ....STEM Robotics....")
                                self.textarea.insert(END, f"\n Bill Number:\t{self.bill_no.get()}")
                                self.textarea.insert(END, "\n GST no :  32AACCF8045D1ZM ")
                                self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
                                self.textarea.insert(END, f"\n Phone Number:{self.c_phon.get()}")
                                self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

                                self.textarea.insert(END, "\n ==================================================")
                                self.textarea.insert(END, "\n Products\t\t\tQTY\t\tPrice")
                                self.textarea.insert(END, "\n ==================================================\n")

                            def iaddItem(self):
                                Tax = 2
                                self.n = self.prices.get()
                                self.m = self.qty.get() * self.n
                                self.l.append(self.m)
                                if self.product.get() == "":
                                    messagebox.showerror('Error', "Plaese Enter Mobile No. & Select The Product")
                                else:
                                    self.textarea.insert(END,
                                                         f'\n {self.product.get()}\t\t\t{self.qty.get()} \t\t{self.m}')
                                    self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
                                    self.tax_input.set(
                                        str('Rs.%.2f' % ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
                                    self.total.set(str('Rs.%.2f' % (
                                        ((sum(self.l)) + ((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))))

                            def gen_bill(self):
                                if self.product.get() == "":
                                    messagebox.showerror('Error', "Plaese Add To Cart Product")
                                else:
                                    text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
                                    self.welcome()
                                    self.textarea.insert(END, text)
                                    self.textarea.insert(END, "\n ==================================================")
                                    self.textarea.insert(END, f"\n Sub Amount:\t\t\t\t{self.sub_total.get()}")
                                    self.textarea.insert(END, f"\n GST Amount:\t\t\t\t{self.tax_input.get()}")
                                    self.textarea.insert(END, f"\n Total Amount:\t\t\t\t{self.total.get()}")
                                    self.textarea.insert(END, "\n ==================================================\n")

                            def save_bill(self):
                                op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
                                if op > 0:
                                    self.bill_data = self.textarea.get("1.0", END)
                                    f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
                                    f1.write(self.bill_data)
                                    messagebox.showinfo("Saved", f"Bill No: {self.bill_no.get()} saved Successfully")
                                    f1.close()

                            def find_bill(self):
                                present = "no"
                                for i in os.listdir("bills/"):
                                    if i.split(".")[0] == self.search_bill.get():
                                        f1 = open(f"bills/{i}", "r")
                                        self.textarea.delete("1.0", END)
                                        for d in f1:
                                            self.textarea.insert(END, d)
                                        f1.close()
                                        present = "yes"
                                if present == "no":
                                    messagebox.showerror("Error", "Invalid Bill No.")

                            def Categories(self, event=""):
                                if self.ComboCategories.get() == "Clothing":
                                    self.ComboSubCategory.config(value=self.ClothingSubCat)
                                    self.ComboSubCategory.current(0)

                                if self.ComboCategories.get() == "LifeStyle":
                                    self.ComboSubCategory.config(value=self.LifStyleSubCat)
                                    self.ComboSubCategory.current(0)

                                if self.ComboCategories.get() == "Mobiles":
                                    self.ComboSubCategory.config(value=self.MobilesSubCat)
                                    self.ComboSubCategory.current(0)

                            def Product_Add(self, event=""):
                                if self.ComboSubCategory.get() == "Pant":
                                    self.ComboProduct.config(value=self.Pant)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "T-Shirt":
                                    self.ComboProduct.config(value=self.T_shirt)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "Shirt":
                                    self.ComboProduct.config(value=self.Shirt)
                                    self.ComboProduct.current(0)

                                    # Lifestyle
                                if self.ComboSubCategory.get() == "Bath Soap":
                                    self.ComboProduct.config(value=self.Bath_soap)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "Face Creame":
                                    self.ComboProduct.config(value=self.Face_creame)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "Hair Oil":
                                    self.ComboProduct.config(value=self.Hair_oil)
                                    self.ComboProduct.current(0)

                                    # Mobile
                                if self.ComboSubCategory.get() == "Iphone":
                                    self.ComboProduct.config(value=self.Iphone)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "Sumsung":
                                    self.ComboProduct.config(value=self.Samsung)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "Xiome":
                                    self.ComboProduct.config(value=self.Xiome)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "RealMe":
                                    self.ComboProduct.config(value=self.RealMe)
                                    self.ComboProduct.current(0)

                                if self.ComboSubCategory.get() == "One+":
                                    self.ComboProduct.config(value=self.OnePlus)
                                    self.ComboProduct.current(0)

                            def price(self, event=""):
                                # pant
                                if self.ComboProduct.get() == "Levis":
                                    self.ComboPrice.config(value=self.price_pant)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Mufti":
                                    self.ComboPrice.config(value=self.price_pantlocal)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Spykar":
                                    self.ComboPrice.config(value=self.price_pantmax)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                    # T-Shirt
                                if self.ComboProduct.get() == "Polo":
                                    self.ComboPrice.config(value=self.price_polo)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Roadster":
                                    self.ComboPrice.config(value=self.price_Roadster)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Jack&Jones":
                                    self.ComboPrice.config(value=self.price_JackJones)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                    # Shirt
                                if self.ComboProduct.get() == "Peter England":
                                    self.ComboPrice.config(value=self.price_Peter)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Louis Phillipe":
                                    self.ComboPrice.config(value=self.price_Louis)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Park Avenue":
                                    self.ComboPrice.config(value=self.price_Park)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "LifeBuy":
                                    self.ComboPrice.config(value=self.price_life)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Lux":
                                    self.ComboPrice.config(value=self.price_lux)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Santoor":
                                    self.ComboPrice.config(value=self.price_santoor)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Pears":
                                    self.ComboPrice.config(value=self.price_pearl)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Fair&Lovel":
                                    self.ComboPrice.config(value=self.price_fair)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Ponds":
                                    self.ComboPrice.config(value=self.price_ponds)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Olay":
                                    self.ComboPrice.config(value=self.price_olay)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Garnier":
                                    self.ComboPrice.config(value=self.price_garnier)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Parachute":
                                    self.ComboPrice.config(value=self.price_para)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Jashmin":
                                    self.ComboPrice.config(value=self.price_jashmin)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Bajaj":
                                    self.ComboPrice.config(value=self.price_bajaj)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Iphone_X":
                                    self.ComboPrice.config(value=self.price_ix)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Iphone_11":
                                    self.ComboPrice.config(value=self.price_i11)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Iphone_12":
                                    self.ComboPrice.config(value=self.price_i12)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Samsung M16":
                                    self.ComboPrice.config(value=self.price_sm16)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Sumsung M12":
                                    self.ComboPrice.config(value=self.price_sm12)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Sumsung M21":
                                    self.ComboPrice.config(value=self.price_sm21)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Red11":
                                    self.ComboPrice.config(value=self.price_r11)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "Redme-12":
                                    self.ComboPrice.config(value=self.price_r12)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "RedmePro":
                                    self.ComboPrice.config(value=self.price_rpro)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "RealMe 12":
                                    self.ComboPrice.config(value=self.price_rel12)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "RealMe 13":
                                    self.ComboPrice.config(value=self.price_rel13)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "RealMe Pro":
                                    self.ComboPrice.config(value=self.price_relpro)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "OnePlus1":
                                    self.ComboPrice.config(value=self.price_one1)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "OnePlus2":
                                    self.ComboPrice.config(value=self.price_one12)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                                if self.ComboProduct.get() == "OnePlus3":
                                    self.ComboPrice.config(value=self.price_one3)
                                    self.ComboPrice.current(0)
                                    self.qty.set(1)

                        if __name__ == "__main__":
                            root = Toplevel()
                            obj = Bill_App(root)
                            root.mainloop()

                    runningit()

            else:
                # print("Invalid credentials")
                messagebox.showerror("Failed", "Username or password is incorrect")

        def showit():
            if v.get() == 1:
                passenter.config(show='')
            else:
                passenter.config(show='*')

        top = Toplevel()
        top.geometry('800x400')
        top.resizable(False, False)
        top.title("Bill Details login page")

        image1 = (Image.open("Resource/back1.jfif"))
        image2 = image1.resize((800, 400))
        image3 = ImageTk.PhotoImage(image2)

        img_label = Label(top, image=image3)
        img_label.place(x=0, y=0)

        login_frame = Frame(top, bg="grey20", highlightbackground="white", highlightthickness=2)
        login_frame.place(x=160, y=60, width=500, height=250)

        userlabel = Label(login_frame, text="Username: ", fg="white", bg="grey20", font=('times', 15, 'bold'), width=10)
        userlabel.place(x=50, y=60)

        passlabel = Label(login_frame, text="Password: ", fg="white", bg="grey20", font=('times', 15, 'bold'), width=10)
        passlabel.place(x=50, y=130)

        userenter = Entry(login_frame, font=('times', 15, 'bold'), bd=3, width=15)
        userenter.place(x=250, y=58)

        passenter = Entry(login_frame, font=('times', 15, 'bold'), bd=3, width=15, show="*")
        passenter.place(x=250, y=128)

        v = IntVar()
        check_box = Checkbutton(login_frame, bg="grey20", variable=v, onvalue=1, offvalue=0, command=showit)
        check_box.place(x=450, y=135)

        loginbutn = Button(login_frame, text="Login", font=('times', 13, 'bold'), width=5, relief=RAISED, bd=5,
                           command=customerrun22)
        loginbutn.place(x=220, y=190)

        top.mainloop()
        # =========================================================================================================================

    h = Toplevel()
    h.geometry("1000x500")
    h.title("Customer's Details Page")
    h.resizable(False, False)

    img = (Image.open("Resource/back3.jpg"))
    img2 = img.resize((1000, 700))
    img1 = ImageTk.PhotoImage(img2)

    styles = ttk.Style()
    styles.theme_use('clam')

    container_frame = Frame(h, bg="Orange red")
    container_frame.place(x=0, y=0, width=1000, height=700)

    imge_label = Label(container_frame, image=img1)
    imge_label.place(x=0, y=0, width=1000, height=700)

    menu_frame = Frame(h, bg="midnightblue", highlightbackground="red3", highlightthickness=1)
    menu_frame.place(x=260, y=100, width=500, height=300)

    mean_label = Label(menu_frame, text="Menu", bg='midnightblue', fg="White",
                       font=('times', 20, 'italic', 'underline'))
    mean_label.place(x=200, y=0, width=100, height=50)

    button1 = Button(menu_frame, text="Customer Detail Management System", fg="black", bg="royalblue1", relief=RAISED,
                     bd=4,
                     font=('times', 12, 'bold'), width=40, command=customerrun1)
    button1.place(x=70, y=90)

    button2 = Button(menu_frame, text="Bill Details Management System", fg="black", bg="royalblue1", relief=RAISED,
                     bd=4,
                     font=('times', 12, 'bold'), width=40, command=billrun)
    button2.place(x=70, y=180)

    k.mainloop()


k = Tk()
k.geometry("1000x500")
k.title("Main Page")
k.resizable(False, False)

img = (Image.open("Resource/gradient.jpeg"))
img2 = img.resize((1000, 700))
img1 = ImageTk.PhotoImage(img2)

styles = ttk.Style()
styles.theme_use('clam')

container_frame = Frame(k, bg="Orange red")
container_frame.place(x=0, y=0, width=1000, height=700)

imge_label = Label(container_frame, image=img1)
imge_label.place(x=0, y=0, width=1000, height=700)

menu_frame = Frame(k, bg="grey12", highlightbackground="Ghost White", highlightthickness=1)
menu_frame.place(x=260, y=100, width=500, height=300)

mean_label = Label(menu_frame, text="Menu", bg='grey12', fg="White", font=('times', 20, 'italic', 'underline'))
mean_label.place(x=200, y=0, width=100, height=50)

button1 = Button(menu_frame, text="Admin Login", fg="black", bg="snow", relief=RAISED, bd=4, font=('times', 12, 'bold'),
                 width=20, command=adminrun)
button1.place(x=160, y=70)

button2 = Button(menu_frame, text="Employee Login", fg="black", bg="snow", relief=RAISED, bd=4,
                 font=('times', 12, 'bold'), width=20, command=employeerun)
button2.place(x=160, y=140)

button3 = Button(menu_frame, text="Customer Details", fg="black", bg="snow", relief=RAISED, bd=4,
                 font=('times', 12, 'bold'), width=20, command=customerrun)
button3.place(x=160, y=210)

k.mainloop()


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("employee management")

        #variables
        self.var_cat=StringVar()
        self.var_name = StringVar()
        self.var_cat_name = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married=StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender= StringVar()
        self.var_phone = StringVar()
        self.var_country=StringVar()
        self.var_prod_amount= StringVar()


        lbl_title=Label(self.root,text="CUSTOMER MANAGEMENT",font=("times to newroman",37,"bold"),fg="red",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)
        ##logo
        img_logo=Image.open('Resources/emp4.jpg')
        img_logo=img_logo.resize((540,160),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
             #image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st
        img1 = Image.open('Resources/emp6.jpeg')
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)
        #2nd
        img_2 = Image.open('Resources/emp5.jpeg')
        img_2= img_2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img_2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

        #3rd
        img_3 = Image.open('Resources/emp7.png')
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img_3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1000, y=0, width=540, height=160)



        #MAIN FRAME
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)
        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text="CUSTOMER INFORMATION",font=('times new roman',37,'bold'),fg='red')

        upper_frame.place(x=10,y=10,width=1480,height=270)

        #labels and entry FIELDS

        lbl_dep=Label(upper_frame,text='CATEGORY',font=('arial',12,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

       #combobox
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_cat,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=("select cateogry",'sotwarepro','service','manitanance')
        combo_dep.current(0)

        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    #name
        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="NAME",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,ipady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",12,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        ##lbl_Designation


        lbl_Desigination=Label(upper_frame,font=("arial",12,"bold"),text="productname",bg="white")
        lbl_Desigination.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Desigination = ttk.Entry(upper_frame,textvariable=self.var_cat_name, width=22, font=("arial", 12, "bold"))
        txt_Desigination.grid(row=1, column=1, sticky=W, padx=2, pady=7)

       #email

        lbl_email = Label(upper_frame, font=("arial", 12, "bold"), text="EMAIL", bg="white")
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(upper_frame,textvariable=self.var_email,width=22, font=("arial", 12, "bold"))
        txt_email.grid(row=1, column=3,  padx=2, pady=7)


       #address

        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="ADDRESS", bg="white")
        lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address,width=22, font=("arial", 12, "bold"))
        txt_address.grid(row=2, column=1, padx=2, pady=7)

      ##married

        lbl_married_status = Label(upper_frame, font=("arial", 12, "bold"), text="MARRIED STATUS", bg="white")
        lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        com_txt_married= ttk.Combobox(upper_frame,textvariable=self.var_married, width=22, font=("arial", 12, "bold"),state="readonly")
        com_txt_married['values']=("select status","Married","unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2, column=3,sticky=W, padx=2, pady=7)
    ###DOB
        lbl_dob=Label(upper_frame, font=("arial", 12, "bold"), text="DOB:", bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)



        txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob,width=22, font=("arial", 12, "bold"))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)
##doj
        lbl_doj=Label(upper_frame, font=("arial", 12, "bold"), text="DOJ:", bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",12,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

##idproof

        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",12,"bold"),width=15)
        com_txt_proof['values']=("select id proof","pan card","drivinglicence")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        ##gender

        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="GENDER", bg="white")
        lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        com_txt_gender = ttk.Combobox(upper_frame,textvariable=self.var_gender, width=22, font=("arial", 12, "bold"), state="readonly")

        com_txt_gender['values'] = ("select gender","Male", "Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        #phone
        lbl_doj=Label(upper_frame, font=("arial", 12, "bold"), text="PHNO:", bg="white")
        lbl_doj.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

#country

        lbl_country = Label(upper_frame, font=("arial", 12, "bold"), text="COUNTRY:", bg="white")
        lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_country = ttk.Entry(upper_frame, textvariable=self.var_country,width=22, font=("arial", 11, "bold"))
        txt_country.grid(row=1, column=5, padx=2, pady=7)
##salary
        lbl_ctc = Label(upper_frame, font=("arial", 12, "bold"), text="AMOUNT", bg="white")
        lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_ctc = ttk.Entry(upper_frame, textvariable=self.var_prod_amount,width=22, font=("arial", 11, "bold"))
        txt_ctc.grid(row=2, column=5, padx=2, pady=7)


###button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1100,y=10,width=170,height=210)

        btn_add=Button(button_frame,text="save",command=self.add_data,font=("arial",15,"bold"),width=13,bg='blue',fg="white" )
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update = Button(button_frame, text="update", command=self.update_data, font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text="delete", command=self.delete_data,font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, command=self.reset_data,text="clear", font=("arial", 15, "bold"), width=13, bg='blue', fg="white")
        btn_clear.grid(row=3, column=0, padx=1, pady=5)


        # down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text="CUSTOMER INFORMATION",
                                 font=('times new roman', 25, 'bold'), fg='red')

        down_frame.place(x=10, y=280, width=1480, height=300)
        #search fRMANE
        search_frmae=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text="CUSTOMER information",font=('times new roman',25,'bold'),fg='red')
        search_frmae.place(x=0,y=0,width=1470,height=80)

        search_by = Label(search_frmae, font=("arial", 12, "bold"), text="search by", fg="white",bg='red')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        #search
        self.var_com_search=StringVar()
        com_txt_search = ttk.Combobox(search_frmae,textvariable=self.var_com_search, font=('arial', 12, 'bold'), width=17, state='readonly')
        com_txt_search['value'] = ("select option", 'phone', 'id')
        com_txt_search.current(0)

        com_txt_search.grid(row=0, column=1, padx=5, sticky=W)
        self.var_search=StringVar()


        txt_search = ttk.Entry(search_frmae,textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search=Button(search_frmae,text="search",font=("arial",11,"bold"),width=14)
        btn_search.grid(row=0,column=3,padx=5)

        btn_showAll=Button(search_frmae,text="show all",font=("arial",11,"bold"),width=10)
        btn_showAll.grid(row=0,column=4,padx=5)

#======employee=======
#table
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=80,width=1320,height=80)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('cat','name','cat_name','email','address','married','dob','doj',"idproofcomb",'idproof','gender','phone','country','prod_amount',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

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

        self.employee_table['show']='headings'
        self.employee_table.column('cat',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('cat_name',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb', width=100)
        self.employee_table.column('idproof',  width=100)
        self.employee_table.column('gender',  width=100)
        self.employee_table.column('phone',  width=100)
        self.employee_table.column('country',  width=100)
        self.employee_table.column('prod_amount',  width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        ####function declaration####
    def add_data(self):
        if self.var_cat.get()=="" or self.var_email.get()=="":
            messagebox.showerror('error','all fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='anakha',database='hr_emp')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                self.var_cat.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_cat_name.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob .get(),
                                                                                                                self.var_doj .get(),
                                                                                                                self.var_idproofcomb.get(),
                                                                                                                self.var_idproof .get(),
                                                                                                                self.var_gender .get(),
                                                                                                                self.var_phone .get(),
                                                                                                                self.var_country .get(),
                                                                                                                self.var_prod_amount.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','customer added has been added',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)
#fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='anakha', database='hr_emp')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from customer')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #GET CURSOR

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']
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
                update=messagebox.askyesno('update','are you shure update customer data')
                if update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='anakha', database='hr_emp')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update customer set cate=%s, name=%s, cat_name=%s, email=%s, address=%s, married=%s, dob=%s, doj=%s, idproofcomb=%s, gender=%s, phone=%s, country=%s, prod_amount=%s where idproof=%s' ,(

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
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)
    def delete_data(self):
        if self.var_idproof.get()=="":
              messagebox.showerror('Error','all field are require')

        else:
            try:
                Delete=messagebox.askyesno('Delete','are you sure delete  this customer',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='anakha', database='hr_emp')
                    my_cursor = conn.cursor()
                    sql='delete from customer where idproof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "customer delete success", parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)
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
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='anakha', database='hr_emp')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from customer where'+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'due to :{str(es)}',parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

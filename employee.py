import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk,messagebox,END
class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")  # Fixed geometry
        self.root.title("Inventory Management System | developed by Aarti")
        self.root.config(bg="white")
        self.root.focus_force()
        #==========================
        # All Variables======
        self.var_Searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        
        
        #===searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy oldsd style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy oldsd style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #===title====
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        #====content=====
        #===row1====
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
                                                                                                              
        #===row2===
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
                             
      #===row3===
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_password,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
                             
        #===row4===
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salery=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salery=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
      #===buttons====
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy oldsd style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy oldsd style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy oldsd style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy oldsd style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
     #====Employee Details===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================

    def add(self):
       con = sqlite3.connect(database=r'ims.db')
       cur = con.cursor()
       try:
        if self.var_emp_id.get() == "":
            messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
        else:
            cur.execute("SELECT * from employee where eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row!=None:
                messagebox.showerror("Error", "This Employee ID already assigned, try different", parent=self.root)
            else:
                cur.execute("INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),

                                        self.var_dob.get(),
                                        self.var_doj.get(),

                                        self.var_password.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get(1.0, END),
                                        self.var_salary.get(),
                ))
                con.commit()
        messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
        self.show()
       except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
         con = sqlite3.connect(database=r'ims.db')
         cur = con.cursor()
         try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
               self.EmployeeTable.insert('',END,values=row)
               
         except Exception as ex:
          messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



    def get_data(self,ev):
       f=self.EmployeeTable.focus()
       content=(self.EmployeeTable.item(f))
       row=content ['values']
       # print(row)
       self.var_emp_id.set(row[0])
       self.var_name.set(row[1])
       self.var_email.set(row[2])
       self.var_gender.set(row[3])
       self.var_contact.set(row[4])
       self.var_dob.set(row[5])
       self.var_doj.set(row[6])
       self.var_password.set(row[7])
       self.var_utype.set(row[8])
       self.txt_address.delete(1.0, END),
       self.txt_address.insert(END,row[9]),
       self.var_salary.set(row[10])
      
      
    def Update(self):
       con = sqlite3.connect(database=r'ims.db')
       cur = con.cursor()
       if row and len(row) > 0:
        self.var_emp_id.set(row[0])
       else:
        print("Row is empty or doesn't have enough elements.")

       try:
        if self.var_emp_id.get() == "":
            messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
        else:
            cur.execute("SELECT * FROM employee where eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
            else:
                cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where eid=?", (
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_password.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get(1.0, END),
                                        self.var_salary.get(),
                                        self.var_emp_id.get(),
                ))
                con.commit()
        messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
        self.show()
       except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)   
   
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
              cur.execute("SELECT * FROM employee where eid=?", (self.var_emp_id.get(),))
              row = cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                  cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                  con.commit()
                messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                self.clear()
        except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)   
   
    def clear(self):
       self.var_emp_id.set("")
       self.var_name.set("")
       self.var_email.set("")
       self.var_gender.set("Select")
       self.var_contact.set("")
       self.var_dob.set("")
       self.var_doj.set("")
       self.var_password.set("")
       self.var_utype.set("Admin")
       self.txt_address.delete(1.0, END),
       self.var_salary.set("")
       self.var_searchtxt.set("")
       self.var_Searchby.set("Select")
       self.show()

    def search(self):
     con = sqlite3.connect(database=r'ims.db')
     cur = con.cursor()
     try:
        # Get the selected search option and the search text
        search_by = self.var_Searchby.get()
        search_txt = self.var_searchtxt.get()

        # Input validation
        if search_by == "Select":
            messagebox.showerror("Error", "Please select a search option.", parent=self.root)
        elif search_txt == "":
            messagebox.showerror("Error", "Search input is required.", parent=self.root)
        else:
            # Using a parameterized query to avoid SQL injection
            query = f"SELECT * FROM employee WHERE {search_by} LIKE ?"
            cur.execute(query, ('%' + search_txt + '%',))  # Parameterized query
            rows = cur.fetchall()

            # Check if any records are returned
            if rows:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())  # Clear the table
                for row in rows:
                    self.EmployeeTable.insert('', 'end', values=row)  # Insert fetched records
            else:
                messagebox.showinfo("No Results", "No records found.", parent=self.root)

     except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Database error: {str(e)}", parent=self.root)
     except Exception as ex:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(ex)}", parent=self.root)
     finally:
         con.close()  # Ensure the connection is closed



if __name__ == "__main__":
 root = Tk()
 obj = employeeClass(root)
 root.mainloop()

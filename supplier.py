import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk,messagebox
class supplierClass:
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
        
        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
       
        
        
        
        #===searchFrame=====
        lbl_search = Label(self.root, text="Invoice No.", bg="white", font=("goudy old style", 15))
        lbl_search.place(x=700, y=80)

      # Entry for searching
        self.txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        self.txt_search.place(x=800, y=80, width=160)

     # Search Button
        self.btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2")
        self.btn_search.place(x=980, y=79, width=100, height=28)

     # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=10, width=1000, height=40)

    # Supplier Invoice
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white")
        lbl_supplier_invoice.place(x=50, y=80)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow")
        txt_supplier_invoice.place(x=180, y=80, width=180)

                                                                                                              
        #===row2===
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
        
      #===row3===
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
      
                             
        #===row4===
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=120)
       
      #===buttons====
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy oldsd style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy oldsd style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy oldsd style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy oldsd style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)
     #====Employee Details===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,relwidth=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

    # Create a frame for the supplier table
        supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=700, y=120, relwidth=380, height=350)

# Add scrollbars
        scrolly = Scrollbar(supplier_frame, orient=VERTICAL)
        scrollx = Scrollbar(supplier_frame, orient=HORIZONTAL)

# Create the Treeview
        self.supplierTable = ttk.Treeview(supplier_frame, columns=("invoice", "name", "contact", "desc"),
                                   yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

# Configure scrollbars for supplier table
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)


# Define column headings
        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")


# Show only the headings
        self.supplierTable["show"] = "headings"


# Set column widths
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=200)


# Pack the Treeview
        self.supplierTable.pack(fill=BOTH,expand=1)

# Bind the selection event to a method
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)


        self.show()
#========================================================================================================
  
    def add(self):
      con = sqlite3.connect(database=r'ims.db')
      cur = con.cursor()
      try:
          if self.var_sup_invoice.get() == "":
            messagebox.showerror("Error", "Invoice must be required", parent=self.root)
          else:
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Invoice no. already assigned, try a different one", parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)",
                    (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get(1.0, END).strip(),  # Remove extra newline
                    )
                )
                con.commit()
                messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
      finally:
        con.close()  # Ensure connection is closed


    def show(self):
     con = sqlite3.connect(database=r'ims.db')
     cur = con.cursor()
     try:
        cur.execute("SELECT * FROM supplier")
        rows = cur.fetchall()
        if rows:  # Only clear and update if there are rows
         self.supplierTable.delete(*self.supplierTable.get_children())
        for row in rows:
                self.supplierTable.insert('', END, values=row)
     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     finally:
        con.close()  # Ensure connection is closed


    def get_data(self, ev):
     f = self.supplierTable.focus()
     content = self.supplierTable.item(f)
     row = content['values']
    
     if row:  # Check to ensure a row is selected
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete(1.0, END)
        self.txt_desc.insert(END, row[3])

      
    def Update(self):
     con = sqlite3.connect(database=r'ims.db')
     cur = con.cursor()
     try:
        if self.var_sup_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
        else:
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
            else:
                cur.execute(
                    "UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?",
                    (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get(1.0, END).strip(),  # Remove extra newline
                        self.var_sup_invoice.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                self.show()  # Refresh the supplier list after updating
     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     finally:
        con.close()  # Ensure connection is closed


    def delete(self):
     con = sqlite3.connect(database=r'ims.db')
     cur = con.cursor()
     try:
        if self.var_sup_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
        else:
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                if op:
                    cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Supplier deleted successfully", parent=self.root)
                    self.clear()  # Clear input fields after deletion
     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     finally:
        con.close()  # Ensure connection is closed


   
    def clear(self):
     self.var_sup_invoice.set("")  # Clear the invoice field
     self.var_name.set("")          # Clear the name field
     self.var_contact.set("")       # Clear the contact field
     self.txt_desc.delete(1.0, END) # Clear the description field
     self.var_searchtxt.set("")     # Clear the search field
     self.show()                    # Refresh the displayed supplier list



    def search(self):
     con = sqlite3.connect(database=r'ims.db')
     cur = con.cursor()
     try:
        if self.var_searchtxt.get() == "":
            messagebox.showerror("Error", "Invoice no. is required", parent=self.root) 
        else:
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
            rows = cur.fetchall()
            if rows:
                self.supplierTable.delete(*self.supplierTable.get_children())  # Clear previous results
                for row in rows:
                    self.supplierTable.insert('', END, values=row)
            else:
                messagebox.showinfo("No Results", "No records found!", parent=self.root)  # Info instead of error
     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
     finally:
        con.close()


               
if __name__ == "__main__":
 root = Tk()
 obj = supplierClass(root)
 root.mainloop()

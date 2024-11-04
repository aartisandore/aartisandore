from msilib import add_data
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import tkinter as tk
import sqlite3
import time
class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | developed by Aarti")
        self.root.config(bg="white")
        self.cart_list=[]
        # ===title====
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        # ===btn_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)
        # ===clock=====
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
  
        #===Product_Frame===
       

        
        Product_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Product_Frame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(Product_Frame1,text="AllProducts",font=("gowdy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
         #====Product Search Frame===========
        self.var_search=StringVar()
        Product_Frame2=Frame(Product_Frame1,bd=2,relief=RIDGE,bg="white")
        Product_Frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(Product_Frame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(Product_Frame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(Product_Frame2,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(Product_Frame2,text="Search",command=self.search,font=("gowdy old style",),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(Product_Frame2,text="Show All",command=self.show,font=("gowdy old style",),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
         #====Product Details Frame===========
        ProductFrame3=Frame(Product_Frame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.Product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)

        self.Product_Table.heading("pid",text="P ID")
        self.Product_Table.heading("name",text="Name")
        self.Product_Table.heading("price",text="Price")
        self.Product_Table.heading("qty",text="QTY")
        self.Product_Table.heading("status",text="Status")
        
        self.Product_Table["show"]="headings"

        self.Product_Table.column("pid",width=40)
        self.Product_Table.column("name",width=100)
        self.Product_Table.column("price",width=100)
        self.Product_Table.column("qty",width=40)
        self.Product_Table.column("status",width=90)
        self.Product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(Product_Frame1,text="Note:'Enter 0 Quantity to remove product from the Cart'",font=("gowdy old style",12),anchor="w",bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #======CustomerFrame=======
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("gowdy old style",15),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

       #====Cal Cart Frame===========
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

       #====Calculator Frame===========
        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly')
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('_'),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=3)

        #==== Cart Frame===========
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Products: [0]",font=("gowdy old style",12),bg="lightgrey")
        self.cartTitle.pack(side=TOP,fill=X)
        
        
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
  
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #====ADD Cart Widgets Frame===========
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_cal_input = StringVar()

        
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_instock=Label(Add_CartWidgetsFrame,text="In stock",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

        #=================billing area=========
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)

        bTitle=Label(billFrame,text="Customer Bill Area",font=("gowdy old style",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # ============billing button========================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("gowdy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text='Discount\n[5%]',font=("gowdy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=("gowdy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)


        btn_print=Button(billMenuFrame,text='Print',cursor='hand2',font=("gowdy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(billMenuFrame,text='Clear All',cursor='hand2',font=("gowdy old style",15,"bold"),bg="grey",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text='Generate/SaveBill',command=self.generate_bill,cursor='hand2',font=("gowdy old style",12,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #========footer=====
        footer=Label(self.root,text="IMS-Inventory Management System |Developed by GD Global\n For any Technical Issue contact:8308340371 ",font=("times new roman",11),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)
        
        self.show()
        #self.bill_top()
# =============All Function====================
   
    def get_input(self, num):
        # Get the current input
        current_input = self.var_cal_input.get()
        
        # Concatenate the new number/input
        new_input = current_input + str(num)
        
        # Set the updated input back to the StringVar
        self.var_cal_input.set(new_input)

    def clear_cal(self):
       self.var_cal_input.set('')
    
    def perform_cal(self):
       result=self.var_cal_input.get()
       self.var_cal_input.set(eval(result))
       


    def show(self):
         con = sqlite3.connect(database=r'ims.db')
         cur = con.cursor()
         try:
           
            cur.execute("Select pid,name,price,qty,status from product")
            rows=cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
               self.Product_Table.insert('',END,values=row)
               
         except Exception as ex:
          messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try: 
           if self.var_search.get()=="":
              messagebox.showerror("Error","Search input should be required",parent=self.root) 
           else:
              cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                 self.Product_Table.delete(self.Product_Table.get_children())
                 for row in rows:
                    self.Product_Table.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)   


    def get_data(self,ev):
       f=self.Product_Table.focus()
       content=(self.Product_Table.item(f))
       row=content ['values']
       self.var_pid.set(row[0])
       self.var_pname.set(row[1])
       self.var_price.set(row[2])
       self.var_qty.set('3')
       self.lbl_instock.config(text=f"In stock[{str(row[3])}]")
       self.var_stock.set('4')


    def add_update_cart(self):
     if self.var_pid.get() == '':
        messagebox.showerror('Error', "Please Select Product from the list", parent=self.root) 
     elif self.var_qty.get() == '': 
        messagebox.showerror('Error', "Quantity is Required", parent=self.root) 
    
     if int(self.var_qty.get()) > int(self.var_stock.get()):
       print("Quantity requested exceeds available stock.")
    # You might want to display a warning message or disable a button here.
     else: 
       # price_cal = int(self.var_qty.get()) * float(self.var_price.get())
       #cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get()]
      price_cal=self.var_price.get()

      present = 'no'
      index_ = -1

        # Check if the product already exists in the cart
      for i, row in enumerate(self.cart_list):
            if self.var_pid.get() == row[0]:  # row[0] is the product ID
                present = 'yes'
                index_ = i
                break

            if present == 'yes':
             op = messagebox.askyesno('Confirm', "Product already present.\nDo you want to Update | Remove from the Cart?", parent=self.root)
            if op:
                if self.var_qty.get() == "0":
                    self.cart_list.pop(index_)
                else:
                    # Update quantity and price if product exists
                    self.cart_list[index_][2] = price_cal  # Update price
                    self.cart_list[index_][3] = self.var_qty.get()  # Update quantity
            else:
            # Append new product if it doesn't exist in the cart
               self.cart_list.append(cart_data)

        # Refresh cart table display
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
      self.bill_amt = 0
      self.net_pay = 0
      self.discount=0
       #pid,name,price,qty,stock
      for row in self.cart_list:
       self.bill_amt +=self.bill_amt+(float(row[2])*int(row[3]))  # Sum total price for all items
      self.discount=(self.bill_amt*5)/100
      self.net_pay = self.bill_amt - self.discount  
      self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amt)}')
      self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
      self.cartTitle.config(text=f"Cart \t Total Products: [{str(len(self.cart_list))}]")

    def show_cart(self):
     try:
        self.CartTable.delete(*self.CartTable.get_children())
        for row in self.cart_list:
            self.CartTable.insert('', END, values=row)
     except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data_cart(self, ev):
     try:
        # Get the focused item in the CartTable
        f = self.CartTable.focus()
        
        # Retrieve the item details from the selected row
        content = self.CartTable.item(f)
        row = content.get('values', [])

        # Proceed only if row data is available
        if row:
            # Unpack row data into variables
            # Assuming row format: [pid, name, price, qty, stock]
            self.var_pid.set(row[0])
            self.var_pname.set(row[1])
            self.var_price.set(row[2])
            self.var_qty.set(row[3])
            self.lbl_instock.config(text=f"In stock [{str(row[4])}]")
            self.var_stock.set(row[4])
        else:
            messagebox.showinfo("Selection Error", "No item selected in the cart.", parent=self.root)

     except IndexError:
        messagebox.showerror("Error", "Error retrieving item data from cart.", parent=self.root)
   

    def generate_bill(self):
     if self.var_cname.get() == '' or self.var_contact.get() == '':
        messagebox.showerror("Error", "Customer Details are required", parent=self.root)
     elif len(self.cart_list)==0:
         messagebox.showerror("Error", "Please add product to the cart", parent=self.root)
       
     else:
        # ==== Bill Top ====
        self.bill_top()
        # ==== Bill Middle ====
        self.bill_middle()
        # ==== Bill Bottom ====
        self.bill_bottom()
           
    def bill_top(self):
     invoice = str(time.strftime("%H%M%S")) + str(time.strftime("%d%m%y"))
     bill_top_temp = f'''
\t\tXYZ-Inventory
\tPhone No. 98725*****, Delhi-123450
{str("=" * 47)}
Customer Name: {self.var_cname.get()}
 Ph no.: {self.var_contact.get()}
 Bill No. {invoice} \t\tDate: {time.strftime('%d/%m/%Y')}
 {str("="*47)}
 Product Name \t\tQTY \tPrice
{str("=" * 47)}
      '''
     self.txt_bill_area.delete('1.0', END)
     self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
      bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tRs.{self.bill_amt}
Discount\t\t\t\tRS.{self.discount}
Net Pay \t\t\t\tRS.{self.net_pay}
{str("="*47)}\n
      '''
      self.txt_bill_area.insert(END, bill_bottom_temp)


    def Middle(self):
     for row in self.cart_list:
      #pid,name,price,qty,stock
         name=row[1]
         qty=row[3]
         price=float(row[2])*int(row[3])
         price=str(price)
         self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRS."+price)




if __name__=="__main__":   
 root = Tk()
 obj = BillClass(root)
root.mainloop()          

  
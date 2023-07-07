from tkinter import font as tkFont
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkcalendar import Calendar
import tkinter as tk
from PIL import ImageTk, Image,ImageGrab
import tkinter.font as font
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#from googleapiclient.discovery import build
import webbrowser
import datetime



class main:
    def new(self):
        self.root = Tk()
        self.root.title("ATTENDANCE SYSTEM")
        self.root.state('zoomed')
        #self.root.geometry("800x800")
        p1 = PhotoImage(file = 'images2/logo.png')
  
        self.root.iconphoto(True, p1)
        self.root.resizable(False, False)
        self.cred = credentials.Certificate('cred/gateactivities.json')
        firebase_admin.initialize_app(self.cred)
        cred2 = credentials.Certificate('cred/gsheets.json')

        firebase_admin.initialize_app(cred2,name='second-app')
        
        self.db = firestore.client()
        self.collection_ref = self.db.collection('EmployeeDetails')

        helv36 = tkFont.Font(family='Helvetica', size=9, weight=tkFont.BOLD)

        self.dframe = Frame(self.root, height=801, width=1456,bg='white',highlightthickness=7,highlightbackground="black")
        self.dframe.place(x=200, y=-2)
        pictured = PhotoImage(file="images2/logo2.png")
        labeld = Label(self.dframe, image=pictured,bg='white')
        labeld.place(relx=0.5, rely=0.5, anchor="center")
        self.sidefr=Frame(self.root, height=800, width=200,bg='#00047B').place(x=0,y=0)
        # Create a button
        button1 = tk.Button(self.sidefr, text="VIEW\nATTENDANCE",command=self.set_frame_1)

# Configure the button's appearance
        button1.config(width=19, height=2, font=("Arial", 12,'bold'))
        button1.place(x=1,y=200)

        button2 = tk.Button(self.sidefr, text="VIEW\nEMPLOYEE DETAILS",command=self.frame_2)

# Configure the button's appearance
        button2.config(width=19, height=2, font=("Arial", 12,'bold'))
        button2.place(x=2,y=265)

        button3 = tk.Button(self.sidefr, text="GENERATE\nGOOGLE SHEETS",command=self.frame_3)

# Configure the button's appearance
        button3.config(width=19, height=2, font=("Arial", 12,'bold'))
        button3.place(x=3,y=330)

        button3 = tk.Button(self.sidefr, text="GENERATE\nGOOGLE SHEETS",command=self.frame_3)

# Configure the button's appearance
        button4 = tk.Button(self.sidefr, text="VIEW\nGOOGLE SHEETS",command=self.frame_4)

        button4.config(width=19, height=2, font=("Arial", 12,'bold'))
        button4.place(x=4,y=395)
# Place the button in the window
        
        image = Image.open("images2/user.png")
        image = image.resize((140, 160))  # Resize the image to fit the frame

# Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

# Create a label within the frame and set the image
        label = tk.Label(self.sidefr, image=photo,bd=0)
        label.place(x=30,y=20)
        lb=tk.Label(self.sidefr,text="Welcome Admin",font=("Helvetica", 19,"bold"),bg="#00047B",fg='white')
        lb.place(x=3,y=150)

        self.frame1 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="#CDCDC1")
        self.subframe=Frame(self.frame1, height=595, width=1330, bg="black",highlightthickness=5,highlightbackground="blue")

        self.frame2 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="#CDCDC1")
        self.frame3 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="grey")
        self.frame4 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="grey")


        lb2=tk.Label(self.root,text="▇ BAJAJ ENGINEERING WORKS",font=("Helvetica", 19,"bold"),fg='RED')
        lb2.place(x=1100,y=802)
        phb= PhotoImage(file ="images2/search.png")
        self.pic3= PhotoImage(file ="images2/casting.png")
  
        # Resizing image to fit on button
        self.cast = self.pic3.subsample(2,1)
  
        # Resizing image to fit on button
        self.photo2 = phb.subsample(6,7)
        self.root.mainloop()

    def set_frame_1(self):
        self.hide_frame()
        self.frame1.place(x=200, y=-2)
        self.subframe.place(x=0, y=190)
        lbf1=tk.Label(self.frame1,text="*SELECT DATE :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf1.place(x=300,y=50)
        cvalues = ['01', '02', '03', '04', '05', '06', '07','08','09','10','11','12']
        self.combobox = ttk.Combobox(self.frame1, values=cvalues, state="readonly")
        self.combobox.config(height=5, width=28, font=('Arial', 12), foreground='blue')
        self.combobox.bind("<<ComboboxSelected>>",self.motnhrec)
        self.combobox.set("SELECT MONTH(monthly record)")
        self.combobox.place(x=900,y=140)

        buttonf1 = tk.Button(self.frame1, text="SELECT",command=self.selectdate)

# Configure the button's appearance
        buttonf1.config(width=19, height=2, font=("Arial", 12,'bold'),bg='blue',fg='white')
        buttonf1.place(x=300,y=100)
        custom_font = font.Font(weight="bold",size=20)
        lbf2=tk.Label(self.frame1,text="*ENTER NAME TO SEARCH :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf2.place(x=900,y=50)
        self.entry = tk.Entry(self.frame1,font=custom_font,fg='grey',bg='white',highlightthickness=2, highlightbackground="sky blue")
        #entry.config(width=19, height=2)
        
        self.entry.place(x=900,y=100,width=300,height=30)


        button2 = tk.Button(self.frame1, image=self.photo2,width=28, height=23,command=self.search2)
        button2.place(x=1200,y=101)

        self.cal = Calendar(self.frame1, selectmode = 'day',date_pattern='dd-MM-yy')

        self.cal.place(x=20,y=5)
        pic= PhotoImage(file ="images2/refresh.png")
  
        # Resizing image to fit on button
        self.photo5 = pic.subsample(2,1)

        button4 = tk.Button(self.subframe,width=143, height=320,image=self.photo5,bg='black',command=self.re2)

        button4.place(x=1170,y=0)



        pic2= PhotoImage(file ="images2/print.png")
  
        # Resizing image to fit on button
        self.photo6 = pic2.subsample(4,3)
        button5 = tk.Button(self.subframe,width=143, height=300,image=self.photo6,bg='white',command=self.print2)
        button5.place(x=1170,y=280)
        
        self.treea = ttk.Treeview(self.subframe,show="tree")
        self.treea["columns"] = ("ID","NAME","IN","OUT")
        self.treea.column("#0", width=0)
        #self.tree.column("column1", width=200)
        self.treea.column("ID", width=50,anchor="center")
        self.treea.column("NAME", width=373,anchor="center")
        self.treea.column("IN", width=373,anchor="center")
        self.treea.column("OUT", width=373,anchor="center")
        #self.treea.heading("#0", text="ID")
        #self.tree.heading("column1", text="ID")
        self.treea.heading("ID", text="ID",anchor="center")
        self.treea.heading("NAME", text="NAME",anchor="center")
        self.treea.heading("IN", text="IN",anchor="center")
        self.treea.heading("OUT", text="OUT",anchor="center")
        self.treea.tag_configure("heading", font=("Arial", 20, "bold"))

        style = ttk.Style()
        style.configure("Treeview",anchor="center", borderwidth=1, font=("Arial", 15),background='white',foreground='blue',rowheight=25)
        self.treea["show"] = "tree headings"
        
        self.scrollbar2 = ttk.Scrollbar(self.subframe, orient=tk.VERTICAL, command=self.treea.yview)
        self.scrollbar2.place(x=1153, y=0, height=583)  # Position the Scrollbar next to the Treeview using place

        self.treea.configure(yscrollcommand=self.scrollbar2.set)

        pen = self.collection_ref.get()
        docs = sorted(pen, key=lambda doc: doc.get('idd'))

        self.treea.place(x=0,y=0,height=585)
 
                        
        for doc in docs:
                doc_data = doc.to_dict()
                #print(doc_data)
                #doc_id = int(doc.id)
                #name = doc_data.get('id', '')
                age = doc_data.get('name', '')
                #print(age)
                country = doc_data.get('inTime', '')
                id=(doc_data.get('idd', ''))
                dept=doc_data.get('outTime', '')
                
                
                if str(country)=="null":
                    #self.treea.insert("", tk.END, text=id, values=(age, country,dept),tag='gray')

                    self.treea.insert("", tk.END, values=(id,age, country,dept),tag='red')
                    self.treea.tag_configure('red',foreground="red")
                    self.treea.insert("", tk.END, values=('---------------------------------','-------------------------------','--------------------------------','----------------------------------'),tag='gray')
                elif str(dept)!="null":
                    #self.treea.insert("", tk.END, text=id, values=(age, country,dept),tag='gray')

                    self.treea.insert("", tk.END, values=(id,age, country,dept),tag='green')
                    self.treea.tag_configure('green',foreground="green")
                    self.treea.insert("", tk.END, values=('---------------------------------','-------------------------------','--------------------------------','----------------------------------'),tag='gray')
                                
                else:
                    self.treea.insert("", tk.END, values=(id,age, country,dept))
                    self.treea.insert("", tk.END, values=('---------------------------------','-------------------------------','--------------------------------','----------------------------------'),tag='gray')

                
    def selectdate(self):
        selected_date = self.cal.get_date()
        
        date_obj = datetime.datetime.strptime(selected_date, "%d-%m-%y")
        formatted_date = date_obj.strftime("%d-%m-%Y")
        
        data_ref = self.db.collection("Attendance").document(formatted_date)
        data = data_ref.get().to_dict()

        
        #print(array_data)

        # Clear existing data in the TreeView if needed
        self.treea.delete(*self.treea.get_children())

        array_data1 = data["ids"]
        array_data2 = data["names"]
        array_data3 = data["inTime"]
        array_data4 = data["outTime"]

        for item1, item2, item3,item4 in zip(array_data1, array_data2, array_data3,array_data4):
            self.treea.insert("", "end", values=(item1, item2, item3,item4))
            self.treea.insert("", tk.END, values=('---------------------------------','-------------------------------','--------------------------------','----------------------------------'),tag='gray')

    def search2(self):
        query = str(self.entry.get())
        print(query)
        selections = []
        flag = 0

        for child in self.treea.get_children():
            values = self.treea.set(child)
            if any(query.lower() in str(value).lower() for value in values.values()):
                selections.append(child)

        if selections:
            self.treea.selection_set(selections)
            self.treea.focus(selections[-1])  # Focus on the last matching item
            flag = 1

        if flag == 0:
            messagebox.showerror("Error", "EMPLOYEE NAME DOESN'T EXIST\nOR\nTYPE NAME CORRECTLY", icon=messagebox.ERROR)

        self.entry.delete(0, tk.END)

    def motnhrec(self,v):
        #print(v)
        selected_month = str(self.combobox.get())  # July
        #print(selected_month)

        # Build a query to fetch the documents matching the selected month
        query = self.db.collection('Attendance')
        #print(1)
        # Execute the query and iterate over the results
        docs = query.stream()
        #print(2)
        flag=0
        for doc in docs:
            date = doc.id
            #print("m=",date)
            document_month = date.split('-')[1]

            # Check if the document's month matches the selected month
            if document_month == selected_month:
                flag=1
                #print(date)

                data_ref = self.db.collection("Attendance").document(date)
                data = data_ref.get().to_dict()

                #print(data)             #print(array_data)

                # Clear existing data in the TreeView if needed
                self.treea.delete(*self.treea.get_children())

                array_data1 = data["ids"]
                array_data2 = data["names"]
                array_data3 = data["inTime"]
                array_data4 = data["outTime"]

                for item1, item2, item3,item4 in zip(array_data1, array_data2, array_data3,array_data4):
                    self.treea.insert("", "end", values=(item1, item2, item3,item4))
                    self.treea.insert("", tk.END, values=('---------------------------------','-------------------------------','--------------------------------','----------------------------------'),tag='gray')
        if flag ==0:
            messagebox.showerror("Error", "SORRY NO DATA EXIST FOR SELECTED MONTH", icon=messagebox.ERROR)
        else:
            messagebox.showinfo("INFO", f"DISPLAYING DATA FOR {selected_month} MONTH", icon=messagebox.INFO)



    def re2(self):
        self.set_frame_1() 

    def print2(self):
        value='---------------------------------'
        itemsd = self.treea.get_children()
        for itemd in itemsd:
            item_values = self.treea.item(itemd)['values']
            if value in item_values:
                self.treea.delete(itemd)
        data = []
        for item in self.treea.get_children():
            values = self.treea.item(item)["values"]
            data.append(values)

        # Define the table columns and rows
        num_columns = len(self.treea["columns"])
        num_rows = len(data)

        # Define the column widths
        column_widths = [100] * num_columns

        # Define the row heights
        row_height = 20

        # Create a list to hold the table data
        table_data = []

        # Add column names as the first row of the table data
        column_names = self.treea["columns"]
        table_data.append(column_names)

        # Add the data rows to the table data
        for row in data:
            table_data.append(row)

        # Define the table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),  # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header row text color
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Data row background color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header row font
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header row font size
            ('BOTTOMPADDING', (0, 0), (0, 0), 5),  # Header row bottom padding
            ('TOPPADDING', (0, 0), (0, 0), 5),  # Header row top padding
            ('BOTTOMPADDING', (0, 1), (-1, -1), 5),  # Data row bottom padding
            ('TOPPADDING', (0, 1), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Data row top padding
        ])

        # Create the PDF document
        pdf_file = "attendance.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Create the table and apply the table style
        table = Table(table_data, colWidths=column_widths, rowHeights=row_height)
        table.setStyle(table_style)

        # Build the PDF document with the table
        elements = [table]
        doc.build(elements)

        #print("TreeView converted to PDF successfully.")
        self.pdf_file_path2 = pdf_file

        webbrowser.open_new(self.pdf_file_path2)

        self.re2()

    def frame_2(self):
        self.hide_frame()
        self.frame2.place(x=200, y=-2)
        self.subframe2=Frame(self.frame2, height=687, width=1330, bg="black",highlightthickness=5,highlightbackground="blue")
        self.subframe2.place(x=0, y=100)

        custom_font = font.Font(weight="bold",size=20)
        lbf3=tk.Label(self.frame2,text="*ENTER NAME TO SEARCH :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf3.place(x=450,y=25)
        self.entry2 = tk.Entry(self.frame2,font=custom_font,fg='grey',bg='white',highlightthickness=2, highlightbackground="sky blue")
        #entry.config(width=19, height=2)
        
        self.entry2.place(x=450,y=65,width=300,height=30)


        button3 = tk.Button(self.frame2, image=self.photo2,width=28, height=22,command=self.search)
        button3.place(x=750,y=65)
        self.root.bind("<Return>", lambda event: self.search())
        self.tree = ttk.Treeview(self.subframe2,show="tree")
        self.tree["columns"] = ( "NAME", "CONTACT","DEPARTMENT")
        self.tree.column("#0", width=50)
        #self.tree.column("column1", width=200)
        self.tree.column("NAME", width=300,anchor="center")
        self.tree.column("CONTACT", width=400,anchor="center")
        self.tree.column("DEPARTMENT", width=400,anchor="center")
        self.tree.heading("#0", text="ID")
        #self.tree.heading("column1", text="ID")
        self.tree.heading("NAME", text="NAME",anchor="center")
        self.tree.heading("CONTACT", text="CONTACT",anchor="center")
        self.tree.heading("DEPARTMENT", text="DEPARTMENT",anchor="center")
        self.tree.tag_configure("heading", font=("Arial", 20, "bold"))

        

  
        # Reference a specific collection
        

        # Retrieve all documents in the collection
        pen = self.collection_ref.get()
        docs = sorted(pen, key=lambda doc: doc.get('idd'))
 
                        
        for doc in docs:
                doc_data = doc.to_dict()
                #print(doc_data)
                #doc_id = int(doc.id)
                #name = doc_data.get('id', '')
                age = doc_data.get('name', '')
                #print(age)
                country = doc_data.get('contact', '')
                id=int(doc_data.get('idd', ''))
                dept=doc_data.get('department', '')
                if id%2==0:
                    self.tree.insert("", tk.END, text=id, values=(age, country,dept),tag='gray')
                    self.tree.tag_configure('gray', background='#cccccc')
                else:
                    self.tree.insert("", tk.END, text=id, values=(age, country,dept))
        style = ttk.Style()
        style.configure("Treeview",anchor="center", borderwidth=1, font=("Arial", 15),background='white',foreground='blue',rowheight=25)
        self.tree["show"] = "tree headings"

        
        self.tree.place(x=0,y=0,height=665)




# Bind the item selection event to the function
        self.tree.bind("<<TreeviewSelect>>", self.handle_select)
        self.scrollbar = ttk.Scrollbar(self.subframe2, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.place(x=1150, y=0, height=665)  # Position the Scrollbar next to the Treeview using place

        self.tree.configure(yscrollcommand=self.scrollbar.set)
        pic= PhotoImage(file ="images2/refresh.png")
  
        # Resizing image to fit on button
        self.photo3 = pic.subsample(2,1)

        button4 = tk.Button(self.subframe2,bg='black',width=143, height=320,image=self.photo3,command=self.refresh)
        #button4.config(width=8, height=9,font=("Arial", 20,'bold'))
        button4.configure(relief="flat")
        button4.place(x=1170,y=15)


        #button5.config(width=8, height=9,font=("Arial", 20,'bold'))
        pic2= PhotoImage(file ="images2/print.png")
  
        # Resizing image to fit on button
        self.photo4 = pic2.subsample(4,3)
        button5 = tk.Button(self.subframe2,width=143, height=320,image=self.photo4,bg='white',command=self.print)
        button5.place(x=1170,y=340)


    def handle_select(self,event):
        selected_item = self.tree.focus()
        print(selected_item)
        item_text = self.tree.item(selected_item)["text"]
        print(item_text)
        print(int(item_text))
        #det = self.db.collection("EmployeeDetails").document(str(item_text))
        query = self.db.collection("EmployeeDetails").where("idd", "==", (item_text))

        # Fetch the documents that match the query
        pen = query.get()
        print(pen)

        #pen = det.get()
        

        # Iterate over the matching documents
        for doc in pen:
            doc_data = doc.to_dict()
            print(doc_data)
            

        self.root2=tk.Toplevel()
        self.root2.geometry("1000x600")
        self.root2.title("DETAILS")
        self.root2.configure(bg="#F2F2F2")
        self.root2.resizable(False, False)
                        
        
        #doc_data = pen.to_dict()
        e1 = doc_data.get('name', '')
                                                                    
        e2= doc_data.get('contact', '')
        e3=int(doc_data.get('idd', ''))
        e4=doc_data.get('department', '')
        e5=doc_data.get('dateOfJoining', '')
        e6=doc_data.get('vehicle', '')
        e7=doc_data.get('localAddress', '')
        e8=doc_data.get('permanentAddress', '')
        e9=doc_data.get('dob', '')
        e10=doc_data.get('familyMemberContact', '')
        e11=doc_data.get('fatherName', '')
        e12=doc_data.get('ifscCode', '')
        e13=doc_data.get('panNo', '')
        e14=doc_data.get('bankAccount', '')
        e15=doc_data.get('aadhaar', '')
        e16=doc_data.get('image', '')
        e17=doc_data.get('experience', '')
        e18=doc_data.get('education', '')
        e19=doc_data.get('email', '')
        
        #print (e16)

        self.firebase_image_url = e16

        pic= PhotoImage(file ="images2/Aadhar-Card.png")
  

        photo = pic.subsample(3,4)
                


        image_label = tk.Button(self.root2,image=photo,command=self.imagebrowse)

        image_label.image = photo

        image_label.place(relx=0.5, rely=0.8, anchor="center")  


        data = [("Name", e1), ("ID", e3), ("DEPARTMENT", e4),("CONTACT", e2),("DATE OF JOINING", e5),("VEHICLE", e6),("ADDRESS", e7),("PERMANENT ADDRESS", e8),("DOB", e9),("OTHER CONTACT", e10),("IFSC-CODE", e12),("BANK ACCOUNT", e14),("PAN NUMBER", e13),("AADHAAR NO:",e15),("Experience", e18),("Education", e17),("email", e19),("Father's name", e11)]

        num_columns = 2

        # Iterate over the data list and create labels and entries
        for idx, (label_text, entry_text) in enumerate(data):
            # Calculate the row and column indices
            row = idx // num_columns
            col = idx % num_columns

            # Create label
            label = tk.Label(self.root2, text=label_text,font=("Arial", 15,"bold"))
            label.grid(row=row, column=col * 2, padx=5, pady=5, sticky="e")

            # Create entry
            entry = tk.Entry(self.root2,bg="lightgray", fg="red", font=("Arial", 15))
            entry.insert(tk.END, entry_text)
            entry.grid(row=row, column=col * 2 + 1, padx=5, pady=5, sticky="w")
            entry.config(state='readonly')
                

            


    


        ''' lbh = tk.Label(self.root2, text="NAME :",font=("Helvetica", 13,"bold"),fg='RED')
        lbh.place(x=20,y=30)
        d1=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d1.place(x=120,y=32)

        lbh2 = tk.Label(self.root2, text="ID :",font=("Helvetica", 13,"bold"),fg='RED')
        lbh2.place(x=20,y=80)
        d2=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d2.place(x=120,y=82)

        lbh3 = tk.Label(self.root2, text="DEPARTMENT :",font=("Helvetica", 13,"bold"),fg='RED')
        lbh3.place(x=2,y=130)
        d3=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d3.place(x=135,y=132)

        lbh4 = tk.Label(self.root2, text="CONTACT :",font=("Helvetica", 13,"bold"),fg='RED')
        lbh4.place(x=300,y=30)
        d4=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d4.place(x=400,y=32)
        

        lbh5 = tk.Label(self.root2, text="ADDRESS:",font=("Helvetica", 13,"bold"),fg='RED')
        lbh5.place(x=300,y=80)
        d5=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d5.place(x=400,y=82)

        lbh6 = tk.Label(self.root2, text="VEHICLE:",font=("Helvetica", 13,"bold"),fg='RED')
        lbh6.place(x=300,y=130)
        d6=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d6.place(x=400,y=132)

        lbh7 = tk.Label(self.root2, text="FATHER'S NAME:",font=("Helvetica", 13,"bold"),fg='RED')
        lbh7.place(x=300,y=180)
        d7=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d7.place(x=450,y=182)

        lbh8 = tk.Label(self.root2, text="PERMANENET ADDRESS:",font=("Helvetica", 13,"bold"),fg='RED')
        lbh8.place(x=300,y=230)
        d8=Entry(self.root2,font=("Helvetica", 12,"bold"),fg='RED')
        d8.place(x=450,y=232)

        #self.frevent=Frame(self.root2,width=)'''
    
        





    def refresh(self):
        self.frame_2()



    def print(self):
        data = []
        for item in self.tree.get_children():
            values = self.tree.item(item)["values"]
            data.append(values)

        # Define the table columns and rows
        num_columns = len(self.tree["columns"])
        num_rows = len(data)

        # Define the column widths
        column_widths = [100] * num_columns

        # Define the row heights
        row_height = 20

        # Create a list to hold the table data
        table_data = []

        # Add column names as the first row of the table data
        column_names = self.tree["columns"]
        table_data.append(column_names)

        # Add the data rows to the table data
        for row in data:
            table_data.append(row)

        # Define the table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),  # Header row background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header row text color
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Data row background color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header row font
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header row font size
            ('BOTTOMPADDING', (0, 0), (0, 0), 5),  # Header row bottom padding
            ('TOPPADDING', (0, 0), (0, 0), 5),  # Header row top padding
            ('BOTTOMPADDING', (0, 1), (-1, -1), 5),  # Data row bottom padding
            ('TOPPADDING', (0, 1), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Data row top padding
        ])

        # Create the PDF document
        pdf_file = "treeview.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Create the table and apply the table style
        table = Table(table_data, colWidths=column_widths, rowHeights=row_height)
        table.setStyle(table_style)

        # Build the PDF document with the table
        elements = [table]
        doc.build(elements)

        #print("TreeView converted to PDF successfully.")
        self.pdf_file_path = pdf_file

        webbrowser.open_new(self.pdf_file_path)


    def search(self):
        query = str(self.entry2.get())
        print(query)
        selections = []
        
        flag=0
        
        for child in self.tree.get_children():
            t=str(self.tree.item(child)['text'])
            #print(self.tree.item(child)['values'])
            if query in self.tree.item(child)['values']:   # compare strings in  lower cases.
                #print(self.tree.item(child)['values'])
                selections.append(child)
                #print(selections)
                self.tree.selection_set(selections)
                self.tree.focus(selections)
                flag=1
                #self.refresh()
                
                
            elif query ==t:
                selections.append(child)
                #print(selections)
                self.tree.selection_set(selections)
                self.tree.focus(selections)
                flag=1
                #self.refresh()

                
        if(flag ==0) :
            messagebox.showerror("Error", "EMPLOYEE NAME  DOESNT EXIST \n OR SEARCH USING ID", icon=messagebox.ERROR)
            #self.refresh()
        self.entry2.delete(0, tk.END)
        
        
           
        
    def imagebrowse(self):
        webbrowser.open(self.firebase_image_url)
    


    def frame_3(self):
        self.hide_frame()
        self.frame3.place(x=200, y=-2)


        button = tk.Button(self.frame3,bg='black',width=210, height=320,image=self.cast)
        #button4.config(width=8, height=9,font=("Arial", 20,'bold'))
        button.configure(relief="flat")
        button.place(x=80,y=35)
        lb=tk.Label(self.frame3,text="CASTING SHEET",font=("Helvetica", 19,"bold"),bg='white',fg='blue',width=14)
        lb.place(x=80,y=359)
        #button.grid(row=1, column=1)
    def gsheet(self):


        # Create a Firestore client
        db = firestore.client(app=firebase_admin.get_app(name='second-app'))

        # Authenticate and authorize Google Sheets API
        scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/spreadsheets'
        ]
        credentials1 = ServiceAccountCredentials.from_json_keyfile_name('cred/cred.json', scope)
        client = gspread.authorize(credentials1)

        # Source sheet details
        source_sheet_id = '1BwjtmxB2Vvh6WKV9oQpfayfof7OBtMOHjLmpSFa2KeU'  # Replace with the source sheet ID
        drive_service = build('drive', 'v3', credentials=credentials1)

        # Create a new blank spreadsheet
        new_file_metadata = {
        'name': 'new casting sheet 1',  # Replace with the desired name for the new spreadsheet
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        }
        created_file = drive_service.files().create(body=new_file_metadata).execute()

        # Get the ID of the new spreadsheet
        new_spreadsheet_id = created_file['id']

        print('New spreadsheet ID:', new_spreadsheet_id)

        # Destination document details
        destination_document_id = new_spreadsheet_id  # Replace with the destination document ID

        # Open the source sheet
        source_sheet = client.open_by_key(source_sheet_id)

        # Get the sheet ID
        sheet_id = source_sheet.sheet1.id

        # Create a copy request
        copy_request = {
        'destinationSpreadsheetId': destination_document_id,
        'sourceSheetId': sheet_id,
        }

        # Call the Google Drive API to copy the sheet to the new document
        drive_service = build('drive', 'v3', credentials=credentials1)

        # Copy the sheet to a new document
        current_date = datetime.date.today()
        new_document_metadata = {
        'name': f"Casting {current_date}"  # Replace with the desired name for the new document
            # Replace with the ID of the destination folder (optional)
        }
        copied_document = drive_service.files().copy(fileId=source_sheet_id, body=new_document_metadata).execute()

        # Get the ID of the new document
        new_document_id = copied_document['id']



        #print('Sheet copied successfully!')
        #print('New sheet ID:', new_document_id)
        # Share the copied sheet for collaboration
        drive_service.permissions().create(
        fileId=new_document_id,
        body={
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'sanchitbajaj2003@gmail.com'  # Replace with the desired collaborator email address
        }
        ).execute()
        drive_service.permissions().create(
        fileId=new_document_id,
        body={
            'type': 'user',
            'role': 'writer',
            'emailAddress': 'SupervisorBajaj@gmail.com'  # Replace with the desired collaborator email address
        }
        ).execute()

        #print('Sheet copied and shared successfully!')
        new_sheet_url = f'https://docs.google.com/spreadsheets/d/{new_document_id}'
        #webbrowser.open(new_sheet_url)


        # Specify the collection and document ID
        collection_name = 'gsheet'
        document_id = 'casting'

        # Specify the string data
        string_data = new_sheet_url

        # Create a document reference
        doc_ref = db.collection(collection_name).document(document_id)

        # Set the string data in the document
        doc_ref.set({'gsheet': string_data})
        #print(string_data)
        messagebox.showinfo("INFORMATION", "Sheet generated and shared successfully!'", icon=messagebox.INFO)
    def frame_4(self):
        self.hide_frame()
        self.frame4.place(x=200, y=-2)

        button = tk.Button(self.frame4,width=210, height=320,image=self.cast)
        #button4.config(width=8, height=9,font=("Arial", 20,'bold'))
        button.configure(relief="flat")
        button.place(x=80,y=35)
        lb=tk.Label(self.frame4,text="VIEW \nCASTING SHEET",font=("Helvetica", 19,"bold"),bg='white',fg='blue',width=14)
        lb.place(x=80,y=359)
    def view(self):

        db2 = firestore.client(app=firebase_admin.get_app(name='second-app'))

        det = db2.collection("gsheet").document("casting")

        pen = det.get()
        
        doc_data = pen.to_dict()
        e1 = doc_data.get('gsheet', '')
        #print(e1)
        webbrowser.open(e1)
        # Define the selected month as a string




    def hide_frame(self):
        self.dframe.place_forget()
        self.frame2.place_forget()
        self.frame1.place_forget()
        self.frame3.place_forget()
        self.frame4.place_forget()
        
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('950x600')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        '''self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        '''
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=25, width=350, height=50)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        global mystr
        mystr = StringVar()
        
        
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="blue",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame,textvariable=mystr, highlightthickness=0, relief=FLAT, bg="black", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        '''self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405',height=60)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=520, y=450)'''
        self.login = Button(self.window, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=log)
        self.login.place(x=570, y=460)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        '''self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)'''

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        global pystr
        pystr = StringVar()
        
        self.password_label = Label(self.lgn_frame,text="Password", bg="#040405", fg="blue",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame,textvariable=pystr, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
         ##
        font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=412, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

      #  self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
       #                           activebackground="white"
        #                          , borderwidth=0, background="white", cursor="hand2")
       # self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


def page():
    global window
    window = Tk()
    p1 = PhotoImage(file = 'images2/logo.png')
  
    window.iconphoto(True, p1)
    LoginPage(window)
    window.mainloop()
def log():
    pas=str(pystr.get())

    username=str(mystr.get())

    

    if username=="admin@gmail.com"and pas=="123456":
        messagebox.showinfo("Success", "Login successful!")
        window.destroy()
        obj=main()
        obj.new()
    else:
        messagebox.showerror("Error", "Invalid email or password")

    


if __name__ == '__main__':
    page()

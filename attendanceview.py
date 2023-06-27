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
import subprocess
import webbrowser
#import pyautogui


class main:
    def new(self):
        self.root = Tk()
        self.root.title("ATTENDANCE SYSTEM")
        self.root.state('zoomed')
        self.root.resizable(False, False)
        self.cred = credentials.Certificate('gateactivities.json')
        firebase_admin.initialize_app(self.cred)
        
        self.db = firestore.client()
        self.collection_ref = self.db.collection('EmployeeDetails')

        helv36 = tkFont.Font(family='Helvetica', size=9, weight=tkFont.BOLD)

        self.dframe = Frame(self.root, height=801, width=1456,bg='#FFFDD0',highlightthickness=7,highlightbackground="black")
        self.dframe.place(x=200, y=-2)
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

# Place the button in the window
        
        image = Image.open("user.png")
        image = image.resize((140, 160))  # Resize the image to fit the frame

# Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

# Create a label within the frame and set the image
        label = tk.Label(self.sidefr, image=photo,bd=0)
        label.place(x=30,y=20)
        lb=tk.Label(self.sidefr,text="Welcome Admin",font=("Helvetica", 19,"bold"),bg="#00047B",fg='white')
        lb.place(x=3,y=150)

        self.frame1 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="#CDCDC1")
        self.subframe=Frame(self.frame1, height=600, width=1330, bg="white",highlightthickness=5,highlightbackground="blue")

        self.frame2 = Frame(self.root, height=801, width=1456,highlightthickness=7,highlightbackground="black", bg="#CDCDC1")
        
        lb2=tk.Label(self.root,text="▇ BAJAJ ENGINEERING WORKS",font=("Helvetica", 19,"bold"),fg='RED')
        lb2.place(x=1100,y=802)
        phb= PhotoImage(file ="search.png")
  
        # Resizing image to fit on button
        self.photo2 = phb.subsample(6,7)
        self.root.mainloop()

    def set_frame_1(self):
        self.hide_frame()
        self.frame1.place(x=200, y=-2)
        self.subframe.place(x=0, y=190)
        v=Scrollbar(self.subframe, orient='vertical',width=30)
        v.place(x=1285, relheight=1)
        lbf1=tk.Label(self.frame1,text="*SELECT DATE :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf1.place(x=300,y=50)

        buttonf1 = tk.Button(self.frame1, text="SELECT")

# Configure the button's appearance
        buttonf1.config(width=19, height=2, font=("Arial", 12,'bold'),bg='blue',fg='white')
        buttonf1.place(x=300,y=100)
        custom_font = font.Font(weight="bold",size=20)
        lbf2=tk.Label(self.frame1,text="*ENTER NAME TO SEARCH :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf2.place(x=900,y=50)
        entry = tk.Entry(self.frame1,font=custom_font,fg='grey',bg='white',highlightthickness=2, highlightbackground="sky blue")
        #entry.config(width=19, height=2)
        
        entry.place(x=900,y=100,width=300,height=30)


        button2 = tk.Button(self.frame1, image=self.photo2,width=28, height=23)
        button2.place(x=1200,y=101)

        cal = Calendar(self.frame1, selectmode = 'day',date_pattern='dd-MM-yy')

        cal.place(x=20,y=5)
    def frame_2(self):
        self.hide_frame()
        self.frame2.place(x=200, y=-2)
        self.subframe2=Frame(self.frame2, height=687, width=1330, bg="black",highlightthickness=5,highlightbackground="blue")
        self.subframe2.place(x=0, y=100)

        custom_font = font.Font(weight="bold",size=20)
        lbf3=tk.Label(self.frame2,text="*ENTER NAME TO SEARCH :",font=("Helvetica", 19,"bold"),bg='#CDCDC1',fg='blue')
        lbf3.place(x=450,y=25)
        entry2 = tk.Entry(self.frame2,font=custom_font,fg='grey',bg='white',highlightthickness=2, highlightbackground="sky blue")
        #entry.config(width=19, height=2)
        
        entry2.place(x=450,y=65,width=300,height=30)


        button3 = tk.Button(self.frame2, image=self.photo2,width=28, height=22)
        button3.place(x=750,y=65)
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
        docs = sorted(pen, key=lambda doc: doc.get('num'))
 
                        
        for doc in docs:
                doc_data = doc.to_dict()
                #print(doc_data)
                #doc_id = int(doc.id)
                #name = doc_data.get('id', '')
                age = doc_data.get('name', '')
                #print(age)
                country = doc_data.get('contact', '')
                id=int(doc_data.get('id', ''))
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
        pic= PhotoImage(file ="refresh.png")
  
        # Resizing image to fit on button
        self.photo3 = pic.subsample(2,1)

        button4 = tk.Button(self.subframe2,bg='black',width=143, height=320,image=self.photo3,command=self.refresh)
        #button4.config(width=8, height=9,font=("Arial", 20,'bold'))
        button4.configure(relief="flat")
        button4.place(x=1170,y=15)


        #button5.config(width=8, height=9,font=("Arial", 20,'bold'))
        pic2= PhotoImage(file ="print.png")
  
        # Resizing image to fit on button
        self.photo4 = pic2.subsample(4,3)
        button5 = tk.Button(self.subframe2,width=143, height=320,image=self.photo4,bg='white',command=self.print)
        button5.place(x=1170,y=340)


    def handle_select(self,event):
        selected_item = self.tree.focus()
        item_text = self.tree.item(selected_item)["text"]
        print(f"Selected: {item_text}")

    def refresh(self):
        self.frame_2()

    def print(self):

        pdf = canvas.Canvas("treeview.pdf", pagesize=letter)

    # Get the data from the TreeView
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

    # Set the font and font size for the table
        pdf.setFont("Helvetica", 12)

        for i, column in enumerate(self.tree["columns"]):
            x = 30 + sum(column_widths[:i])
            y = 770
            pdf.drawString(x, y, column)
            pdf.line(x, y, x, y - (num_rows * row_height) - 20)

        # Draw the table rows and dividers
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                x = 30 + sum(column_widths[:j])
                y = 750 - (i * row_height)
                pdf.drawString(x, y, str(value))
                pdf.line(x, y, x + column_widths[j], y)
    # Save the PDF file
        pdf.save()
        print("TreeView converted to PDF successfully.")
        self.pdf_file_path = 'treeview.pdf'

        webbrowser.open_new(self.pdf_file_path)

        #subprocess.run(['xdg-open', self.pdf_file_path])








    def hide_frame(self):
        self.dframe.place_forget()
        self.frame2.place_forget()
        self.frame1.place_forget()
        

    
if __name__ == '__main__':
    obj = main()
    obj.new()
    

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
#import subprocess
import webbrowser
from io import BytesIO
import requests
#import pyautogui


class main:
    def new(self):
        self.root = Tk()
        self.root.title("ATTENDANCE SYSTEM")
        self.root.state('zoomed')
        #self.root.geometry("800x800")
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
        #print(selected_item)
        item_text = self.tree.item(selected_item)["text"]
        #print(str(item_text))
        
        det = self.db.collection("EmployeeDetails").document(str(item_text))

        pen = det.get()
        #print(pen)

        self.root2=tk.Toplevel()
        self.root2.geometry("700x600")
        self.root2.title("DETAILS")
        #self.root2.resizable(False, False)
                        
        
        doc_data = pen.to_dict()
        e1 = doc_data.get('name', '')
                                                                    
        e2= doc_data.get('contact', '')
        e3=int(doc_data.get('id', ''))
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
        #print (e16)

        firebase_image_url = e16
        print(firebase_image_url)
        #print(firebase_image_url)
        #print(type(firebase_image_url))

        response = requests.get(firebase_image_url)
        image_data = response.content


        # Create a label to display the image

        image = Image.open(BytesIO(image_data))
        image.resize((400,300),resample=Image.BILINEAR)
        photo= ImageTk.PhotoImage(image)
        
                

    # Resizing image to fit on button
        #photo= phb.subsample(6,7)

        image_label = tk.Button(self.root2, image=photo)
        image_label.image = photo  # Keep a reference to the image
        
        

        #image_label.pack()
        image_label.place(x=80, y=300, width=400, height=300)  


        data = [("Name", e1), ("ID", e3), ("DEPARTMENT", e4),("CONTACT", e2),("DATE OF JOINING", e5),("VEHICLE", e6),("ADDRESS", e7),("PERMANENT ADDRESS", e8),("DOB", e9),("OTHER CONTACT", e10),("FSI-CODE", e12),("BANK ACCOUNT", e14),("PAN NUMBER", e13),("AADHAAR NO:",e15)]

        num_columns = 2

        # Iterate over the data list and create labels and entries
        for idx, (label_text, entry_text) in enumerate(data):
            # Calculate the row and column indices
            row = idx // num_columns
            col = idx % num_columns

            # Create label
            label = tk.Label(self.root2, text=label_text)
            label.grid(row=row, column=col * 2, padx=5, pady=5, sticky="e")

            # Create entry
            entry = tk.Entry(self.root2)
            entry.insert(tk.END, entry_text)
            entry.grid(row=row, column=col * 2 + 1, padx=5, pady=5, sticky="w")

                

            


    


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
        
        
           
        






    def hide_frame(self):
        self.dframe.place_forget()
        self.frame2.place_forget()
        self.frame1.place_forget()
        

    
if __name__ == '__main__':
    obj = main()
    obj.new()
    

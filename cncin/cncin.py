from tkinter import font as tkFont
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkcalendar import Calendar
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as font
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import datetime
import babel.numbers
import pygsheets
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

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
    cred2 = credentials.Certificate('cred/gsheets.json')

    firebase_admin.initialize_app(cred2,name='second-app')
    

    if username=="admin@gmail.com"and pas=="123456":
        db2 = firestore.client(app=firebase_admin.get_app(name='second-app'))

        det = db2.collection("gsheet").document("in")

        pen = det.get()
        
        doc_data = pen.to_dict()
        e1 = doc_data.get('gsheet', '')
        
        
        messagebox.showinfo("Success", "Login successful!")
        window.destroy()
        webbrowser.open(e1)
    else:
        messagebox.showerror("Error", "Invalid email or password")


    


if __name__ == '__main__':
    page()

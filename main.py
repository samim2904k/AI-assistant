import customtkinter
from CTkMessagebox import CTkMessagebox
import tkinter
from PIL import Image, ImageTk
from PyQt5.QtWidgets import *
import sys
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

auth={}
auth['username'] = os.getenv("ai_username")
auth['password'] = os.getenv("ai_password")

app = customtkinter.CTk()
app.geometry("600x440")
app.resizable(width=False, height=False)
app.title("Log In")

def call_enzo():
    username = username_entry.get()
    password = password_entry.get()
    if auth["username"] == username and auth["password"] == password:
        app.destroy()
        import interface
        GuiApp = QApplication(sys.argv)
        jarvis_gui = interface.Gui_Start()
        jarvis_gui.show()
        exit(GuiApp.exec_())
    else:
        username_entry.delete(0,"end")
        password_entry.delete(0,"end")
        CTkMessagebox(title="Error",message="Invalid Username or Password !!",icon="cancel")

Img1 = ImageTk.PhotoImage(Image.open("C:\CODING\c cpp\python programs\AI assistant\Loginbackground.jpg"))
l1 = customtkinter.CTkLabel(master=app,image=Img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320 , height=360, corner_radius=20)
frame.place(relx=0.5 , rely=0.5, anchor=customtkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame , text="Log in Required" ,font=('Century Gothic', 20))
l2.place(x=55,y=45)

username_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=220)
username_entry.place(x=50,y=110)

password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", width=220)
password_entry.place(x=50,y=165)

l3 = customtkinter.CTkLabel(master=frame , text="Forget Password" ,font=('Century Gothic', 12),text_color="blue")
l3.place(x=165,y=195)

button1 = customtkinter.CTkButton(master=frame , width=220 , text="Login" , corner_radius=6,command=call_enzo)
button1.place(x=50,y=240)

app.mainloop()
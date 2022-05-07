from tkinter import *
import tkinter as tk
import Login.Login_Process as lgp

class Login_View:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1080x720+210+50")
        self.window.configure(bg="#ffffff")

        self.canvas = Canvas(self.window, bg="#ffffff", height=720, width=1080,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./Images/Login/background.png")
        self.background = self.canvas.create_image(660.0, 335.0,
                                                   image=self.background_img)

        self.login_image = PhotoImage(file=f"./Images/Login/login_image.png")
        self.login_button = Button(image=self.login_image, borderwidth=0,
                                   highlightthickness=0, relief="flat", bg="#ffffff", command=lambda: lgp.Login_Process.confirm_button_handle(self))
        self.login_button.place(x=215, y=553, width=150, height=50)

        self.signup_image = PhotoImage(file=f"./Images/Login/signup_image.png")
        self.signup_button = Button(image=self.signup_image, borderwidth=0,
                                    highlightthickness=0, relief="flat", bg="#5D5FEF", command=lambda: lgp.Login_Process.signup_button_handle(self))
        self.signup_button.place(x=765, y=430, width=150, height=50)

        self.entry_img = PhotoImage(file=f"./Images/Login/img_textBox0.png")
        self.entry_bg1 = self.canvas.create_image(290.0, 490.0, image=self.entry_img)
        self.entry_bg2 = self.canvas.create_image(290.0, 390.0, image=self.entry_img)

        self.name_entry = Entry(self.window,bd=0, bg="#c4c4c4", highlightthickness=0)
        self.name_entry.place(x=165.0, y=365, width=250.0, height=48)

        self.password_entry = Entry(self.window,show="*", bd=0, bg="#c4c4c4", highlightthickness=0)
        self.password_entry.place(x=165.0, y=465, width=250.0, height=48)

# app = Login_View()
# app.window.mainloop()
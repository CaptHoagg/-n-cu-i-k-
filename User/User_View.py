from tkinter import *

class User_View:

    def __init__(self):
        self.window = Tk()
        
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        
        self.window.title("User")
        self.window.configure(bg = "#E89DBC")
        self.window.iconphoto(False, PhotoImage(file = f"./Images/SignUp/AppIcon.png"))

        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 720, width = 1080, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./Images/User/Background.png")
        self.background = self.canvas.create_image(540, 360, image=self.background_img)
        
        self.logout_image = PhotoImage(file = f"./Images/User/Button_Logout.png")
        self.logout_button = Button(self.window, image = self.logout_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#F9B1CD")
        self.logout_button.place(x=940, y=15, width=125, height=45)

        self.items_image = PhotoImage(file = f"./Images/User/Button_Items.png")
        self.items_button = Button(self.window, image = self.items_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#49CFFC")
        self.items_button.place(x=335, y=585, width=160, height=55)

        self.shopnow_image = PhotoImage(file = f"./Images/User/Button_Shopnow.png")
        self.shopnow_button = Button(self.window, image = self.shopnow_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#C6B0D7")
        self.shopnow_button.place(x=580, y=585, width=160, height=55)



# app = User_View()
# app.window.mainloop()
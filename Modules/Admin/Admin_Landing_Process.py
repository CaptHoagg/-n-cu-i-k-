from tkinter import *
import Modules.Login.Login_View as lgv
import Modules.Admin.Component.Admin_Main_View as amv


class Admin_Process:
    @staticmethod
    def log_out_button_handle(obj):
        obj.window.destroy()
        app = lgv.Login_View()
        app.window.mainloop()

    @staticmethod
    def products_button_handle(obj):
        obj.window.destroy()

        app = amv.Admin_Main_View()
        app.click_button("products")
        app.window.mainloop()
        # app.click_button("products")

    @staticmethod
    def inventory_button_handle(obj):
        obj.window.destroy()
        app = amv.Admin_Main_View()
        app.click_button("inventory")
        app.window.mainloop()
        # app.click_button("inventory")


    # @staticmethod
    # def sales_button_handle(obj):
    #     obj.window.destroy()
    #     app = salesview.Sales_View()
    #     app.window.mainloop()

    # @staticmethod
    # def user_button_handle(obj):
    #     obj.window.destroy()
    #     app = userview.User_View()
    #     app.window.mainloop()

import tkinter as tk
from tkinter import messagebox
import AdminPostgreSql
import admin


class Login:
    def __init__(self):
        self.adminSql = AdminPostgreSql.Admin_Message()
        # tk对象以及调用
        self.root_window = tk.Tk()
        self.root_window.title('简洁新闻管理')
        self.root_window.geometry('500x300+700+300')
        self.root_window.minsize(500, 300)
        self.root_window.maxsize(500, 300)
        self.user = tk.Entry(self.root_window)
        self.password = tk.Entry(self.root_window, show='*')

        self.addLab()
        self.addEntry()
        self.addBut()
        self.root_window.mainloop()

    def addLab(self):
        user = tk.Label(self.root_window, text="账号  :", font=('Times', 16, ' italic'))
        password = tk.Label(self.root_window, text="密码  :", font=('Times', 16, ' italic'))
        user.place(x=120, y=70)
        password.place(x=120, y=120)

    def addEntry(self):
        self.user.place(x=200, y=73)
        self.password.place(x=200, y=123)

    def addBut(self):
        # 添加按钮
        but_L = tk.Button(self.root_window, text="确认登录", font=('宋体', 12),command=self.but_Login)
        but_W = tk.Button(self.root_window, text="忘记密码", font=('宋体', 12), command=self.but_Forget)
        but_R = tk.Button(self.root_window, text="添加管理员", font=('宋体', 12), command=self.but_Register)
        but_L.place(x=150, y=170)
        but_R.place(x=250, y=170)
        but_W.place(x=150, y=210)
        but_L.bind("<Return>", self.but_Login)

    def but_Login(self):

        name = self.user.get()
        password = self.password.get()
        if name == '' or password == '':
            pass
        else:
            mark_login = self.adminSql.select_AdminUser_OK(name=name, password=password)
            if mark_login:
                messagebox.showinfo("提示", "登录成功")
                self.root_window.destroy()
                main_windows = admin.Admin_Main()
            else:
                messagebox.showinfo("提示", "账号或密码有误！")

    def but_Register(self):
        self.root_window.destroy()
        register = Register()

    def but_Forget(self):
        self.root_window.destroy()
        register = Forget()


class Register:
    def __init__(self):
        self.adminSql = AdminPostgreSql.Admin_Message()
        self.root_window = tk.Tk()
        self.root_window.title('简洁新闻管理')
        self.root_window.geometry('500x500+700+300')
        self.root_window.minsize(500, 500)
        self.root_window.maxsize(500, 500)

        self.user = tk.Entry(self.root_window)
        self.password = tk.Entry(self.root_window, show='*')
        self.phone = tk.Entry(self.root_window)
        self.email = tk.Entry(self.root_window)
        self.reNum = tk.Entry(self.root_window)

        self.addLab()
        self.addEntry()
        self.addBut()

        self.root_window.mainloop()

    def addLab(self):
        user = tk.Label(self.root_window, text="账  号  :", font=('宋体', 16))
        password = tk.Label(self.root_window, text="密  码  :", font=('宋体', 16))
        phone = tk.Label(self.root_window, text="手机号  :", font=('宋体', 16))
        email = tk.Label(self.root_window, text="邮箱号  :", font=('宋体', 16))
        reNum = tk.Label(self.root_window, text="注册码  :", font=('宋体', 16))
        user.place(x=100, y=70)
        password.place(x=100, y=120)
        phone.place(x=100, y=170)
        email.place(x=100, y=220)
        reNum.place(x=100, y=270)

    def addEntry(self):
        self.user.place(x=220, y=73)
        self.password.place(x=220, y=123)
        self.phone.place(x=220, y=173)
        self.email.place(x=220, y=223)
        self.reNum.place(x=220, y=273)

    def addBut(self):
        # 添加按钮
        but_L = tk.Button(self.root_window, text="确认注册", font=('宋体', 12), command=self.register_OK)
        but_R = tk.Button(self.root_window, text="返回登录", font=('宋体', 12), command=self.returnLogin)
        but_L.place(x=120, y=330)
        but_R.place(x=270, y=330)

    def register_OK(self):
        name = self.user.get()
        password = self.password.get()
        phone = self.phone.get()
        email = self.email.get()
        reNum = self.reNum.get()
        if name == '' or password == '' or phone == '' or reNum == '':
            messagebox.showinfo("提示", "输入不能为空成功")
        else:
            self.adminSql.insert_AdminUser(name, password, phone, email, reNum)
            messagebox.showinfo("提示", "注册成功,跳转到登录界面")
            self.returnLogin()

    def returnLogin(self):
        self.root_window.destroy()
        win = Login()


class Forget:
    def __init__(self):
        self.adminSql = AdminPostgreSql.Admin_Message()
        self.root_window = tk.Tk()
        self.root_window.title('简洁新闻管理')
        self.root_window.geometry('500x500+700+300')
        self.root_window.minsize(500, 500)
        self.root_window.maxsize(500, 500)

        self.user = tk.Entry(self.root_window)
        self.phone = tk.Entry(self.root_window)
        self.password = tk.Entry(self.root_window, show='*')
        self.repassword = tk.Entry(self.root_window, show='*')

        self.addLab()
        self.addEntry()
        self.addBut()

        self.root_window.mainloop()

    def addLab(self):
        user = tk.Label(self.root_window, text="账    号  :", font=('宋体', 16))
        phone = tk.Label(self.root_window, text="手 机 号  :", font=('宋体', 16))
        password = tk.Label(self.root_window, text="密    码  :", font=('宋体', 16))
        repassword = tk.Label(self.root_window, text="确认密码  :", font=('宋体', 16))
        user.place(x=100, y=70)
        phone.place(x=100, y=120)
        password.place(x=100, y=170)
        repassword.place(x=100, y=220)

    def addEntry(self):
        self.user.place(x=230, y=73)
        self.phone.place(x=230, y=123)
        self.password.place(x=230, y=173)
        self.repassword.place(x=230, y=223)

    def addBut(self):
        # 添加按钮
        but_L = tk.Button(self.root_window, text="确认修改", font=('宋体', 12), command=self.updateAdmin)
        but_R = tk.Button(self.root_window, text="返回登录", font=('宋体', 12), command=self.returnLogin)
        but_L.place(x=120, y=330)
        but_R.place(x=270, y=330)

    def updateAdmin(self):
        name = self.user.get()
        phone = self.phone.get()
        password = self.password.get()
        repassword = self.repassword.get()

        message_OK = self.adminSql.select_AdminUser_update(name, phone)
        if message_OK:
            if password == repassword:
                self.adminSql.update_adminPassword(name, password)
                messagebox.showinfo("提示", "修改密码成功")
                self.root_window.destroy()
                win = Login()
            else:
                messagebox.showinfo("提示", "两次输入密码不一致！")
        else:
            messagebox.showinfo("提示", "用户名或手机号错误！")

    def returnLogin(self):
        self.root_window.destroy()
        win = Login()


if __name__ == '__main__':
    win_root = Login()

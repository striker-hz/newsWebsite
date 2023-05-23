import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import AdminPostgreSql
import datetime
import time


# 主窗口
class Admin_Main:
    def __init__(self):
        self.root_window = tk.Tk()
        self.adminsql = AdminPostgreSql.Admin_Message()
        self.root_window.title('简洁新闻管理')
        self.root_window.geometry('600x500+700+300')
        self.ybar = Scrollbar(self.root_window, orient='vertical')
        self.tree = ttk.Treeview(self.root_window, show="headings", yscrollcommand=self.ybar.set, height=10)
        self.show_User()
        self.but_index()
        self.add_but()
        self.root_window.mainloop()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '姓名': 100,
            '手机号': 130,
            '电子邮箱': 200,
            '注册码': 100,
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_user()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[3], user[4], user[5]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=30, y=200)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            # show_user_contribute(item_text[0], item_text[2], item_text[3])

    def but_index(self):
        but_1 = tk.Button(self.root_window, text="查看用户订阅", font=('宋体', 12), command=self.jump_subscribe)
        but_2 = tk.Button(self.root_window, text="查看投稿新闻", font=('宋体', 12), command=self.jump_contribute)
        but_3 = tk.Button(self.root_window, text="查看地区列表", font=('宋体', 12), command=self.jump_region_list)
        but_4 = tk.Button(self.root_window, text="查看新闻标题", font=('宋体', 12), command=self.jump_new_list)
        but_5 = tk.Button(self.root_window, text="查看国内新闻", font=('宋体', 12), command=self.jump_china_news)
        but_6 = tk.Button(self.root_window, text="管理员添加新闻", font=('宋体', 12), command=self.jump_adminAdd_news)
        but_Refresh = tk.Button(self.root_window, text="刷新页面", font=('宋体', 12), command=self.Refresh)
        but_1.place(x=50, y=50)
        but_2.place(x=50, y=100)
        but_3.place(x=250, y=50)
        but_4.place(x=250, y=100)
        but_5.place(x=450, y=50)
        but_6.place(x=450, y=100)
        but_Refresh.place(x=460, y=450)

    def add_but(self):
        pass

    # 跳转到订阅
    def jump_subscribe(self):
        self.root_window.destroy()
        win = user_subscribe()

    # 跳转到地区列表
    def jump_region_list(self):
        self.root_window.destroy()
        win = region_List()

    # 跳转到用户投稿
    def jump_contribute(self):
        self.root_window.destroy()
        win = user_contribute()

    # 跳转到新闻channel列表
    def jump_new_list(self):
        self.root_window.destroy()
        win = new_list()

    # 跳转到国内新闻界面
    def jump_china_news(self):
        self.root_window.destroy()
        win = china_new_list()

    # 管理员插入的新闻
    def jump_adminAdd_news(self):
        self.root_window.destroy()
        win = admin_add_news()

    def Refresh(self):
        self.root_window.destroy()
        win_Main = Admin_Main()


# 用户订阅
class user_subscribe(Admin_Main):
    def __init__(self):
        super().__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            'ID': 100,
            '电子邮箱': 400,
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_user_subscribe()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[0], user[1]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=30, y=200)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_user_subscribe(item_text[0], item_text[1])

    def Refresh(self):
        self.root_window.destroy()
        win_Main = user_subscribe()

    def show_user_subscribe(self, ID, Eamil):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('500x200+700+300')
        user = tk.Label(root_window, text="ID:", font=('宋体', 16))
        user_1 = tk.Label(root_window, text=ID, font=('宋体', 16))
        date = tk.Label(root_window, text="电子邮箱:", font=('宋体', 16))
        date_1 = tk.Label(root_window, text=Eamil, font=('宋体', 16))
        user.place(x=50, y=50)
        user_1.place(x=150, y=50)
        date.place(x=50, y=100)
        date_1.place(x=150, y=100)
        root_window.mainloop()


# 用户投稿
class user_contribute(Admin_Main):
    def __init__(self):
        super().__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '姓名': 50,
            '手机号': 100,
            '电子邮箱': 100,
            '投稿日期': 100,
            '投稿内容': 150,
            '显示状态': 50
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_user_contribute()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[2], user[3], user[4], user[5], user[6]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=30, y=200)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_user_contribute(item_text[0], item_text[3], item_text[4], item_text[1])

    def show_user_contribute(self, name, time, contentMessage, phone):
        root_window = tk.Tk()
        adminsql = AdminPostgreSql.Admin_Message()
        root_window.title('简洁新闻管理')
        root_window.geometry('600x500+700+300')
        user = tk.Label(root_window, text="投稿人:", font=('宋体', 16))
        user_1 = tk.Label(root_window, text=name, font=('宋体', 16))
        date = tk.Label(root_window, text="投稿时间:", font=('宋体', 16))
        date_1 = tk.Label(root_window, text=time, font=('宋体', 16))
        content = tk.Label(root_window, text="投稿内容", font=('宋体', 16))
        content_1 = Text(root_window, width=50, height=20)
        but_1 = tk.Button(root_window, text="显示", font=('宋体', 12),
                          command=lambda: self.show_state_OK(root_window, phone))
        but_2 = tk.Button(root_window, text="不显示", font=('宋体', 12),
                          command=lambda: self.show_state_NO(root_window, phone))

        content_1.insert(INSERT, contentMessage)
        user.place(x=50, y=50)
        user_1.place(x=150, y=50)
        date.place(x=50, y=100)
        date_1.place(x=150, y=100)
        content.place(x=50, y=150)
        content_1.place(x=150, y=150)
        but_1.place(x=150, y=450)
        but_2.place(x=350, y=450)
        root_window.mainloop()

    def show_state_OK(self, win, phone):
        adminsql = AdminPostgreSql.Admin_Message()
        adminsql.update_show_state_OK(phone)
        win.destroy()

    def show_state_NO(self, win, phone):
        adminsql = AdminPostgreSql.Admin_Message()
        adminsql.update_show_state_NO(phone)
        win.destroy()

    def Refresh(self):
        self.root_window.destroy()
        win_Main = user_contribute()


# 城市列表
class region_List(Admin_Main):
    def __init__(self):
        super().__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '地区名称': 100,
            '地区 ID': 400,
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_region_List()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[2]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=30, y=200)

    def add_but(self):
        but_add_city = tk.Button(self.root_window, text="添加城市", font=('宋体', 12), command=self.add_city)
        but_add_city.place(x=100, y=450)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_region_List(item_text[0], item_text[1])

    def add_city(self):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('500x300+700+300')
        city_name = tk.Label(root_window, text="地区名称:", font=('宋体', 15))
        city_name_Enter = tk.Entry(root_window)
        city_id = tk.Label(root_window, text="地区ID:", font=('宋体', 15))
        city_id_Entry = tk.Entry(root_window)
        but_update_city = tk.Button(root_window, text="确定添加", font=('宋体', 12))  # 添加的功能还没写
        but_delete_city = tk.Button(root_window, text="返回前页", font=('宋体', 12), command=lambda: return_(root_window))

        city_name.place(x=80, y=50)
        city_name_Enter.place(x=200, y=50)
        city_id.place(x=80, y=100)
        city_id_Entry.place(x=200, y=100)
        but_update_city.place(x=80, y=200)
        but_delete_city.place(x=250, y=200)
        root_window.mainloop()

    def show_region_List(self, name, region_id):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('500x300+700+300')
        user = tk.Label(root_window, text="地区名称:", font=('宋体', 16))
        user_1 = tk.Label(root_window, text=name, font=('宋体', 16))
        date = tk.Label(root_window, text="地区ID:", font=('宋体', 16))
        date_1 = tk.Label(root_window, text=region_id, font=('宋体', 16))
        but_update_city = tk.Button(root_window, text="修改信息", font=('宋体', 12))
        but_delete_city = tk.Button(root_window, text="删除信息", font=('宋体', 12))

        user.place(x=50, y=50)
        user_1.place(x=150, y=50)
        date.place(x=50, y=100)
        date_1.place(x=150, y=100)
        but_update_city.place(x=50, y=200)
        but_delete_city.place(x=250, y=200)
        root_window.mainloop()

    def Refresh(self):
        self.root_window.destroy()
        win_Main = region_List()


# 新闻标题
class new_list(Admin_Main):
    def __init__(self):
        super(new_list, self).__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '新闻名称': 100,
            'API-ID': 400,
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_news_List()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[2]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=30, y=200)

    def add_but(self):
        but_add_city = tk.Button(self.root_window, text="添加标题", font=('宋体', 12), command=self.add_news_channel)
        but_add_city.place(x=100, y=450)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_news_List(item_text[0], item_text[1])

    def show_news_List(self, name, CHANNEL_id):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('500x300+700+300')
        user = tk.Label(root_window, text="新闻标题:", font=('宋体', 16))
        user_1 = tk.Label(root_window, text=name, font=('宋体', 16))
        date = tk.Label(root_window, text="API-ID:", font=('宋体', 16))
        date_1 = tk.Label(root_window, text=CHANNEL_id, font=('宋体', 16))
        but_update_city = tk.Button(root_window, text="修改信息", font=('宋体', 12))
        but_delete_city = tk.Button(root_window, text="删除信息", font=('宋体', 12))

        user.place(x=50, y=50)
        user_1.place(x=150, y=50)
        date.place(x=50, y=100)
        date_1.place(x=150, y=100)
        but_update_city.place(x=50, y=200)
        but_delete_city.place(x=250, y=200)
        root_window.mainloop()

    def Refresh(self):
        self.root_window.destroy()
        win_Main = new_list()

    def add_news_channel(self):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('500x300+700+300')
        city_name = tk.Label(root_window, text="标题名称:", font=('宋体', 15))
        city_name_Enter = tk.Entry(root_window)
        city_id = tk.Label(root_window, text="API-ID:", font=('宋体', 15))
        city_id_Entry = tk.Entry(root_window)
        but_update_city = tk.Button(root_window, text="确定添加", font=('宋体', 12))  # 添加的功能还没写
        but_delete_city = tk.Button(root_window, text="返回前页", font=('宋体', 12), command=lambda: return_(root_window))

        city_name.place(x=80, y=50)
        city_name_Enter.place(x=200, y=50)
        city_id.place(x=80, y=100)
        city_id_Entry.place(x=200, y=100)
        but_update_city.place(x=80, y=200)
        but_delete_city.place(x=250, y=200)
        root_window.mainloop()


# 查看国内新闻
class china_new_list(Admin_Main):
    def __init__(self):
        super(china_new_list, self).__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '新闻标题': 80,
            '新闻链接': 90,
            '发布时间': 90,
            '新闻来源': 90,
            '新闻简介': 100,
            '新闻正文': 100,
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_ChinaNews_List()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[2], user[3], user[4], user[5], user[6]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=20, y=200)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_chinaNews(item_text[0], item_text[1], item_text[2], item_text[3], item_text[4], item_text[5])

    def show_chinaNews(self, title, link, pubdate, source, describe, contentMessage):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('800x600+700+300')
        title_ = tk.Label(root_window, text="新闻标题:", font=('宋体', 15))
        title_1 = tk.Label(root_window, text=title, font=('宋体', 12), wraplength=500)
        link_ = tk.Label(root_window, text="新闻链接:", font=('宋体', 15))
        link_1 = tk.Label(root_window, text=link, font=('宋体', 15))
        date_ = tk.Label(root_window, text="发布时间:", font=('宋体', 15))
        date_1 = tk.Label(root_window, text=pubdate, font=('宋体', 15))
        source_ = tk.Label(root_window, text="新闻来源:", font=('宋体', 15))
        source_1 = tk.Label(root_window, text=source, font=('宋体', 15))
        describe_ = tk.Label(root_window, text="新闻简介:", font=('宋体', 15))
        describe_1 = tk.Label(root_window, text=describe, font=('宋体', 12), wraplength=500)
        content = tk.Label(root_window, text="新闻正文：", font=('宋体', 15))
        content_1 = Text(root_window, width=80, height=20)
        content_1.insert(INSERT, contentMessage)
        title_.place(x=50, y=50)
        title_1.place(x=150, y=50)
        link_.place(x=50, y=100)
        link_1.place(x=150, y=100)
        date_.place(x=50, y=150)
        date_1.place(x=150, y=150)
        source_.place(x=50, y=200)
        source_1.place(x=150, y=200)
        describe_.place(x=50, y=250)
        describe_1.place(x=150, y=250)
        content.place(x=50, y=300)
        content_1.place(x=150, y=300)
        root_window.mainloop()

    def add_but(self):
        but_add_city = tk.Button(self.root_window, text="添加新闻", font=('宋体', 12), command=self.add_news_channel)
        but_add_city.place(x=100, y=450)

    def Refresh(self):
        self.root_window.destroy()
        win_Main = china_new_list()

    def add_news_channel(self):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('800x500+700+300')
        title_ = tk.Label(root_window, text="新闻标题 *:", font=('宋体', 15))
        self.title_Entry = tk.Entry(root_window, width=50, highlightcolor='red', highlightthickness=1)
        link_ = tk.Label(root_window, text="新闻链接 *:", font=('宋体', 15))
        self.link_Entry = tk.Entry(root_window, width=50, highlightcolor='red', highlightthickness=1)
        pubdate_ = tk.Label(root_window, text="发布时间:", font=('宋体', 15))
        curr_time = datetime.datetime.now()
        timestamp = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        self.pubdate_Entry = tk.Label(root_window, text=timestamp, font=('宋体', 15))
        source_ = tk.Label(root_window, text="新闻来源 *:", font=('宋体', 15))
        self.source_Entry = tk.Entry(root_window, width=50, highlightcolor='red', highlightthickness=1)
        describe_ = tk.Label(root_window, text="主题内容 *:", font=('宋体', 15))
        self.describe_Entry = tk.Entry(root_window, width=50, highlightcolor='red', highlightthickness=1)
        # 添加的功能还没写
        but_update_city = tk.Button(root_window, text="确定添加", font=('宋体', 12),
                                    command=lambda: self.addNews(root_window, timestamp))
        but_delete_city = tk.Button(root_window, text="返回前页", font=('宋体', 12), command=lambda: return_(root_window))

        title_.place(x=80, y=50)
        self.title_Entry.place(x=200, y=50)
        link_.place(x=80, y=100)
        self.link_Entry.place(x=200, y=100)
        pubdate_.place(x=80, y=150)
        self.pubdate_Entry.place(x=200, y=150)
        source_.place(x=80, y=200)
        self.source_Entry.place(x=200, y=200)
        describe_.place(x=80, y=250)
        self.describe_Entry.place(x=200, y=250, height=50)
        but_update_city.place(x=100, y=350)
        but_delete_city.place(x=250, y=350)
        root_window.mainloop()

    def addNews(self, win, pubdate):
        title = self.title_Entry.get()
        link = self.link_Entry.get()
        describe = self.describe_Entry.get()
        self.adminsql.insert_admin_Add_News(title, link, pubdate, describe)
        messagebox.showinfo("提示", "添加成功！")
        win.destroy()


# 管理员添加新闻
class admin_add_news(Admin_Main):
    def __init__(self):
        super(admin_add_news, self).__init__()

    def show_User(self):
        self.ybar['command'] = self.tree.yview
        columns = {
            '新闻标题': 120,
            '新闻链接': 120,
            '发布时间': 120,
            '新闻正文': 180
        }
        self.tree["columns"] = list(columns)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=columns[column], anchor='center')

        users_list = self.adminsql.select_admin_add_news()
        for user in users_list:
            self.tree.insert('', user[0], text='', values=(user[1], user[2], user[3], user[4]))

        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.place(x=20, y=200)

    def treeviewClick(self, event):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            self.show_chinaNews(item_text[0], item_text[1], item_text[2], item_text[3], )

    def show_chinaNews(self, title, link, pubdate, contentMessage):
        root_window = tk.Tk()
        root_window.title('简洁新闻管理')
        root_window.geometry('800x600+700+300')
        title_ = tk.Label(root_window, text="新闻标题:", font=('宋体', 15))
        title_1 = tk.Label(root_window, text=title, font=('宋体', 12), wraplength=500)
        link_ = tk.Label(root_window, text="新闻链接:", font=('宋体', 15))
        link_1 = tk.Label(root_window, text=link, font=('宋体', 15))
        date_ = tk.Label(root_window, text="发布时间:", font=('宋体', 15))
        date_1 = tk.Label(root_window, text=pubdate, font=('宋体', 15))
        content = tk.Label(root_window, text="新闻正文：", font=('宋体', 15))
        content_1 = Text(root_window, width=80, height=20)
        content_1.insert(INSERT, contentMessage)
        title_.place(x=50, y=50)
        title_1.place(x=150, y=50)
        link_.place(x=50, y=100)
        link_1.place(x=150, y=100)
        date_.place(x=50, y=150)
        date_1.place(x=150, y=150)
        content.place(x=50, y=200)
        content_1.place(x=150, y=200)
        root_window.mainloop()


# 关闭这个窗口
def return_(win):
    win.destroy()


if __name__ == '__main__':
    win_Main = admin_add_news()

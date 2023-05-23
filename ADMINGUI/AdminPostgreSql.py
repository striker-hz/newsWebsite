from tkinter import messagebox

import psycopg2
import admin

"""
    数据库建立连接
"""


class Admin_Message:
    """
    对用户的增删改查
    """

    def __init__(self):
        self.conn = psycopg2.connect(database='pro_user'
                                     , user='postgres'
                                     , password='990805'
                                     , host='localhost'
                                     , port='5432')
        # 创建指针（游标）对象
        self.cur = self.conn.cursor()

    def insert_AdminUser(self, name, password, phone, email, registermake):
        try:
            sql_insert = "INSERT INTO adminuser (name,password,phone,email,registermake) VALUES ('%s','%s','%s','%s','%s');" \
                         % (name, password, phone, email, registermake)
            self.cur.execute(sql_insert)
            self.conn.commit()
            print('入库成功')
        except Exception as e:
            print(e)

    def insert_admin_Add_News(self, title, link, pubdate, content):
        try:
            sql_insert = "INSERT INTO adminaddnews (title,link,pubdate,content) VALUES ('%s','%s','%s','%s');" \
                         % (title, link, pubdate, content)
            self.cur.execute(sql_insert)
            self.conn.commit()
            print('入库成功')
        except Exception as e:
            print(e)

    # 删
    def delete_user(self, id):
        try:
            sql_delete = "DELETE FROM users WHERE id = %d;" % (int(id))
            self.cur.execute(sql_delete)
            self.conn.commit()
            print("删除成功：id = %d" % (int(id)))
        except Exception as e:
            print(e)

    # 改
    def update_adminPassword(self, name, password):
        try:
            sql_update = "update adminuser set password = '%s' where name = '%s' ;" % (password, name)
            self.cur.execute(sql_update)
            self.conn.commit()
            print('更新成功')

        except Exception as e:
            print(e)

    def update_show_state_NO(self, phone):
        try:
            sql_update = "update users set state = '1' where phone = '%s' ;" % phone
            self.cur.execute(sql_update)
            self.conn.commit()
            messagebox.showinfo("提示", "操作成功！")

        except Exception as e:
            print(e)

    def update_show_state_OK(self, phone):
        try:
            sql_update = "update users set state = '0' where phone = '%s' ;" % phone
            self.cur.execute(sql_update)
            self.conn.commit()
            messagebox.showinfo("提示", "操作成功！")

        except Exception as e:
            print(e)

    # 查询所有的管理员
    def select_AdminUser(self):
        try:
            sql_select = "select * from adminuser"
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            for i in date:
                print(i[1])
        except Exception as e:
            print(e)

    def select_AdminUser_OK(self, name, password):
        try:
            sql_select = "select * from adminuser where name = '%s' ;" % name
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            if password == date[0][2]:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def select_AdminUser_update(self, name, phone):
        try:
            sql_select = "select * from adminuser where name = '%s' ;" % name
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            if phone == date[0][3]:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def select_user(self):
        try:
            sql_select = "select * from adminuser;"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_user_contribute(self):
        try:
            sql_select = "select * from users;"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_user_subscribe(self):
        try:
            sql_select = "select * from subscribe"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_region_List(self):
        try:
            sql_select = "select * from channel_region"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_news_List(self):
        try:
            sql_select = "select * from channel"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_ChinaNews_List(self):
        try:
            sql_select = "select * from chinanews;"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)

    def select_admin_add_news(self):
        try:
            sql_select = "select * from adminaddnews;"
            self.cur.execute(sql_select)
            message = self.cur.fetchall()
            return message
        except Exception as e:
            print(e)


if __name__ == '__main__':
    admin = Admin_Message()
    admin.select_ChinaNews_List()

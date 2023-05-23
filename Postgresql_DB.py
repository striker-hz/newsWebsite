import psycopg2

"""
    数据库建立连接
"""


class User_Message:
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

    # 增
    def insert_user(self, name, phone, email, time, text):
        """
        增加投稿用户信息
        :param name:
        :param phone:
        :param email:
        :param text:
        :param time:
        :return:
        """
        try:
            sql_insert = "INSERT INTO users (name,phone,email,date,news) VALUES ('%s', '%s', '%s', '%s', '%s');" % (
                name, phone, email, time, text)
            self.cur.execute(sql_insert)
            self.conn.commit()
            self.conn.close()


        except Exception as e:
            print(e)

    # 用户订阅
    def insert_subscribe(self, email):
        try:
            sql_insert = "INSERT INTO subscribe (email) VALUES ('%s');" % (email)
            self.cur.execute(sql_insert)
            self.conn.commit()
            print('入库成功')
        except Exception as e:
            print(e)

    def insert_channel(self, channelname, channelid):
        """
        增加新闻标题
        :param channelname:
        :param channelid:
        :return:
        """
        try:
            sql_insert = "INSERT INTO channel (channelname,channelid) VALUES ('%s', '%s');" % (
                channelname, channelid)
            self.cur.execute(sql_insert)
            self.conn.commit()
        except Exception as e:
            print(e)

    def insert_newsContent(self, title, link, pubdate, source, desc, content):
        """
        插入新闻正文
        :param title:
        :param link:
        :param pubdate:
        :param source:
        :param desc:
        :param content:
        :return:
        """
        try:
            sql_insert = "INSERT INTO chinanews (title, link, pubdate, source,describe1 ,content) VALUES ('%s', '%s','%s','%s','%s','%s');" % (
                title, link, pubdate, source, desc, content)
            self.cur.execute(sql_insert)
            self.conn.commit()
        except Exception as e:
            print(e)

    def insert_region_name(self, region_name, region_id):
        """
         插入地区名称和地区id
        :param region_name:
        :param region_id:
        :return:
        """
        try:
            sql_insert = "INSERT INTO channel_region (name_region,channel_id) VALUES ('%s', '%s');" % (
                region_name, region_id)
            self.cur.execute(sql_insert)
            self.conn.commit()
            print("数据入库成功")
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

    def delete(self, id):
        pass

    # 改
    def update(self):
        pass

    # 查询
    def select_user_message(self):
        try:
            sql_select = "select * from users"
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            user_message = {}
            for i in date:
                user_message.setdefault(i[0], i[4])
            # print(user_message.items())
            return user_message
        except Exception as e:
            print(e)

    def emptyNews(self):
        try:
            sql_delete = "TRUNCATE TABLE chinanews;"
            self.cur.execute(sql_delete)
            self.conn.commit()
        except Exception as e:
            print(e)

    def select_user_contribute(self):
        try:
            sql_select = "select * from users where state in (0)"
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            user_message = []
            for i in date:
                user_message.append(i)
            return user_message
        except Exception as e:
            print(e)

    def select_page_news(self, title):
        try:
            sql_select = "select * from chinanews where title = '%s';" % title
            self.cur.execute(sql_select)
            page_news = self.cur.fetchall()
            return page_news
        except Exception as e:
            print(e)

    def select_region(self):
        """

        :return:
        """
        try:
            sql_select = "select name_region from channel_region"
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            region_list = []
            for i in date:
                region_list.append(i[0])
            return region_list

        except Exception as e:
            print(e)

    def select_region_id(self, region_name):
        try:
            sql_select = "select channel_id from channel_region where name_region='%s' " % region_name
            self.cur.execute(sql_select)
            date = self.cur.fetchall()
            channel_region_id = date[0][0]
            return channel_region_id

        except Exception as e:
            print(e)


if __name__ == '__main__':
    user = User_Message()
    user.select_page_news('互联网巨头原有商业模式面临挑战')

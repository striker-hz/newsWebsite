import pymysql

"""
管理控制 Mysql 数据库
"""


class news:
    def __init__(self):
        self.conn = pymysql.connect(host='sh-cynosdbmysql-grp-gkgthkk0.sql.tencentcdb.com'
                                    , user='root'
                                    , password='990805Heng'
                                    , database='news_pro_Hz'
                                    , port=23615
                                    , charset='utf8')
        self.cur = self.conn.cursor()

    def _insert(self):
        pass

    def _delete(self):
        pass

    def _update(self):
        pass

    def _select(self):
        try:
            sql_select = "SELECT *  from subscribe;"
            self.cur.execute(sql_select)
            rows = self.cur.fetchall()
            for row in rows:
                print("ID = ", row[0])
                print("EMAIL = ", row[1])
            self.conn.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    user = news()
    user._select()

from flask import Flask, render_template, request
import datetime
import Postgresql_DB
from Send_Email import SEND

send_E = SEND()

"""
 contact 投稿新闻后台
"""


def getData():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    text = request.form.get('textMessage')
    if name is not None and phone is not None and email is not None:
        if len(str(name)) != 0 and len(str(phone)) != 0 and len(str(email)) != 0:
            try:
                curr_time = datetime.datetime.now()
                time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
                addUser_submit = Postgresql_DB .User_Message()
                addUser_submit.insert_user(name=name, phone=phone, email=email, time = time_str ,text=text)
                print('数据入库成功')
                user_ret = send_E.Send_Email_C(email)
                if user_ret:
                    return True
                else:
                    return False

            except Exception as e:
                print(e)
                print('数据入库失败')
                return False

        else:
            return False
    else:
        return False

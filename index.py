from flask import Flask, render_template, request, redirect, url_for
from setting import SECRET_KEY
from flask_bootstrap import Bootstrap
from recreation import Region
import contact
import about
import International
from Postgresql_DB import User_Message
import Get_indexData
from Send_Email import SEND

app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)
# 数据库实例
user = User_Message()
# 国内新闻实例
news_inland = about.inland()
# 地区新闻后台实例
region_news = Region()
# 邮件发送实例
send_E = SEND()

'''
用户首页
'''


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def Index():
    index = Get_indexData.index_data()
    list_1 = index.get_head_data1()
    list_2 = index.get_head_data2()
    list_3 = index.get_head_data3()
    list_4 = index.get_head_data4()
    list_5 = index.get_head_data5()
    list_6 = index.get_head_data6()
    list_7 = index.get_head_data7()
    list_8 = index.get_head_data8()
    list_9 = index.get_head_data9()
    desc_head, link_head = index.get_head()
    list_lab1 = index.get_lab1()
    list_lab2 = index.get_lab2()
    list_lab3 = index.get_lab3()
    title_bot, source_bot, link_bot, desc_bot = index.get_bot()
    if request.method == 'POST':
        emaildata = request.form.get('subscribe')
        if len(str(emaildata)) != 0:
            print(emaildata)
            user.insert_subscribe(emaildata)
            user_ret = send_E.Send_Email_U(emaildata)
            if user_ret:
                return redirect(url_for('subscribe_Success'))
            else:
                pass

    return render_template('index.html',
                           list_1=list_1, list_2=list_2, list_3=list_3,
                           list_4=list_4, list_5=list_5, list_6=list_6,
                           list_7=list_7, list_8=list_8, list_9=list_9,
                           title_head=desc_head, link_head=link_head,
                           list_lab1=list_lab1, list_lab2=list_lab2, list_lab3=list_lab3,
                           title_bot=title_bot, link_bot=link_bot, source_bot=source_bot, desc_bot=desc_bot)


'''
 国内页面
'''


@app.route('/InLand.html')
def inland():
    title, source, pubdate, desc, link = news_inland.news_content_china()
    return render_template('InLand.html', title=title, source=source, pubdate=pubdate, desc=desc, link=link)


@app.route('/InLand_1.html')
def inland_1():
    title, source, pubdate, desc, link = news_inland.news_content_one()
    return render_template('InLand_1.html', title=title, source=source, pubdate=pubdate, desc=desc, link=link)


@app.route('/InLand_2.html')
def inland_2():
    title, source, pubdate, desc, link = news_inland.news_content_two()
    return render_template('InLand_2.html', title=title, source=source, pubdate=pubdate, desc=desc, link=link)


"""
    提交成功
"""


@app.route('/SubmitSuccess.html')
def submit_Success():
    return render_template('SubmitSuccess.html')


@app.route('/SubscribeSuccess.html')
def subscribe_Success():
    return render_template('SubscribeSuccess.html')


'''
投稿页面
'''


@app.route('/Contribute.html', methods=['GET', 'POST'])
def Contact():
    # 获取 contact 页面表单数据
    if request.method == 'POST':
        ContactBoolean = contact.getData()
        if ContactBoolean:
            return redirect(url_for('submit_Success'))
        else:
            pass
            # return redirect(url_for('submit_Success'))

    return render_template('Contribute.html')


'''
地区新闻页面
'''


@app.route('/Recreation.html')
def Recreation():
    region_list = user.select_region()
    bj_list = region_news.Region_news_bj()
    sh_list = region_news.Region_news_sh()
    gd_list = region_news.Region_news_gz()
    tw_list = region_news.Region_news_tw()
    hb_list = region_news.Region_news_hb()
    sx_list = region_news.Region_news_sx()

    return render_template('Recreation.html', bj_list=bj_list, sh_list=sh_list, gd_list=gd_list,
                           tw_list=tw_list, sx_list=sx_list, hb_list=hb_list, region_list=region_list, )


@app.route('/<cityName>|CityNews.html')
def cityNews(cityName):
    region_list = user.select_region()
    city_id = user.select_region_id(cityName)
    news_list = region_news.get_region_news(cityName, city_id)
    news_list2 = region_news.get_region_news2(cityName)

    return render_template('CityNews.html', cityName=cityName, region_list=region_list, citynews_list=news_list,
                           citynews_list2=news_list2)


''' 
国际页面
'''


@app.route('/International.html')
def international():
    international_news = International.internation()
    title, link, pubdate = international_news.news_channel_world()
    return render_template('International.html', title=title, link=link)


@app.route('/International_1.html')
def international_one():
    international_news = International.internation()
    title, link, pubdate = international_news.news_channel_world_one()
    return render_template('International_1.html', title=title, link=link, pubdate=pubdate)


'''
用户投稿页面显示
'''


@app.route('/UserSubmit.html')
def userSubmit():
    user_message_SUBMIT = user.select_user_contribute()
    return render_template('UserSubmit.html', user_message=user_message_SUBMIT)


"""
新闻详情页面
"""


@app.route('/title=<deNews>|DetailPage.html')
def detailNews(deNews):
    page_news = user.select_page_news(deNews)
    return render_template('detailsPage.html', page_new=page_news[0])


'''
404
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


'''
500
'''


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/Admin', methods=['GET', 'POST'])
def admin():
    user_message = user.select_user_message()
    if request.method == 'POST':
        pass
        # state = request.form.get('user_id')
        # print(state)
    else:
        pass
    return render_template('Admin.html', user_Message=user_message, delete_user=delete_user)


def delete_user(user_id_list):
    print(user_id_list)


if __name__ == '__main__':
    app.run(debug=True)

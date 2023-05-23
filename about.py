from ShowapiRequest import ShowapiRequest
import json
import Postgresql_DB

"""
国内新闻（两会速递）  网页后台
"""


class inland:

    def news_content_china(self):
        """
        获取国内新闻信息
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001db")
            r.addBodyPara("channelName", "")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "10")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            source = []
            pubdate = []
            desc = []
            link = []
            for i in channel_content_list:
                title.append(i['title'])
                source.append(i['source'])
                pubdate.append(i['pubDate'])
                desc.append(i['desc'])
                link.append(i['link'])

            return title, source, pubdate, desc, link

        except Exception as e:
            print(e)

    def news_content_one(self):
        """
        获取国内新闻信息(两会速递)
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001db")
            r.addBodyPara("channelName", "")
            r.addBodyPara("title", "全国两会")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "10")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            source = []
            pubdate = []
            desc = []
            link = []
            for i in channel_content_list:
                title.append(i['title'])
                source.append(i['source'])
                pubdate.append(i['pubDate'])
                desc.append(i['desc'])
                link.append(i['link'])

            return title, source, pubdate, desc, link

        except Exception as e:
            print(e)

    def news_content_two(self):
        """
        获取国内新闻信息(两会速递)
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001db")
            r.addBodyPara("channelName", "")
            r.addBodyPara("title", "疫情")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "10")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            source = []
            pubdate = []
            desc = []
            link = []
            for i in channel_content_list:
                title.append(i['title'])
                source.append(i['source'])
                pubdate.append(i['pubDate'])
                desc.append(i['desc'])
                link.append(i['link'])

            return title, source, pubdate, desc, link

        except Exception as e:
            print(e)

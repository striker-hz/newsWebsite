from ShowapiRequest import ShowapiRequest
import json

"""
国际新闻  网页后台
"""


class internation:
    def news_channel_world(self):
        """
        获取国际新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001de")
            r.addBodyPara("channelName", "国际最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "45")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            link = []
            pubdate = []
            for i in channel_content_list:
                title.append(i['title'])
                link.append(i['link'])
                pubdate.append(i['pubDate'])
            return title, link, pubdate

        except Exception as e:
            print(e)

    def news_channel_world_one(self):
        """
        获取国际新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001de")
            r.addBodyPara("channelName", "国际最新")
            r.addBodyPara("title", "俄乌局势")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "45")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            link = []
            pubdate = []
            for i in channel_content_list:
                title.append(i['title'])
                link.append(i['link'])
                pubdate.append(i['pubDate'])
            return title, link, pubdate

        except Exception as e:
            print(e)


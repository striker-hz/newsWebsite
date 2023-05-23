from ShowapiRequest import ShowapiRequest
import json
from Postgresql_DB import User_Message

"""
 地区新闻网页后台
"""


class Region:
    def __init__(self):
        pass

    def Region_channel(self):
        """
        获取地区
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-48", "926147", "b461cf485c7b48a598064fe428b88ac5")
            res = r.post()
            # 处理json数据
            data_json_content = json.loads(res.text)
            recreation_news_list = data_json_content['showapi_res_body']['cityList']
            user = User_Message()
            for i in recreation_news_list:
                user.insert_region_name(i['areaName'], i['areaId'])
                print(i['areaId'], i['areaName'])
        except Exception as e:
            print(e)

    def Region_news_bj(self):
        """
        北京新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af5085b7bc0c73836b4")  # 地区ID
            r.addBodyPara("areaName", "北京")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def Region_news_sh(self):
        """
        上海新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af5085b7bc0c73836b5")  # 地区ID
            r.addBodyPara("areaName", "上海")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def Region_news_gz(self):
        """
        广州新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af5085b7bc0c73836b7")  # 地区ID
            r.addBodyPara("areaName", "重庆")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def Region_news_tw(self):
        """
        台湾新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af7085b7bc0c73836ce")  # 地区ID
            r.addBodyPara("areaName", "台湾")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def Region_news_hb(self):
        """
        湖北新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af6085b7bc0c73836c3")  # 地区ID
            r.addBodyPara("areaName", "湖北")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def Region_news_sx(self):
        """
        山西新闻
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", "55818af6085b7bc0c73836bd")  # 地区ID
            r.addBodyPara("areaName", "山西")  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def get_region_news(self, region_name, region_id):
        try:
            r = ShowapiRequest("http://route.showapi.com/170-47", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("areaId", " {} ".format(region_id))  # 地区ID
            r.addBodyPara("areaName", "{}".format(region_name))  # 地区名称
            r.addBodyPara("title", "")  # 新闻标题
            r.addBodyPara("page", "1")
            res = r.post()
            data_json_content = json.loads(res.text)
            news_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            news = {}
            for i in news_list:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)

    def get_region_news2(self,region_name):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001cd")# 国内焦点
            r.addBodyPara("channelName", "国内焦点")
            r.addBodyPara("title", "{}".format(region_name))
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "37")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']
            news = {}
            for i in channel_content_list['contentlist']:
                news.setdefault(i['title'], i['link'])
            return news
        except Exception as e:
            print(e)


if __name__ == '__main__':
    region = Region()
    region.get_region_news2('江西')

import Postgresql_DB
from ShowapiRequest import ShowapiRequest
import json


class index_data:
    def __init__(self):
        self.add_insert = Postgresql_DB.User_Message()

    def get_head_data1(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001d1")
            r.addBodyPara("channelName", "互联网焦点")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_1 = {}
            self.add_insert.emptyNews()
            for i in channel_content_list:
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
                list_1.setdefault(i['title'], i['link'])
            return list_1

        except Exception as e:
            print(e)

    def get_head_data2(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001d9")
            r.addBodyPara("channelName", "科技焦点")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_2 = {}
            for i in channel_content_list:
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
                list_2.setdefault(i['title'], i['link'])
            return list_2

        except Exception as e:
            print(e)

    def get_head_data3(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a10bb3cdc86cf39001f5")
            r.addBodyPara("channelName", "数码最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_3 = {}
            for i in channel_content_list:
                list_3.setdefault(i['title'], i['link'])
                content = str(i['content'])
                i['content'] = content.replace("'", "''")
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], ' ', i['content'])
            return list_3
        except Exception as e:
            pass

    def get_head_data4(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001e6")
            r.addBodyPara("channelName", "体育最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_4 = {}
            for i in channel_content_list:
                list_4.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_4

        except Exception as e:
            print(e)

    def get_head_data5(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a10ab3cdc86cf39001ea")
            r.addBodyPara("channelName", "综合体育最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_5 = {}
            for i in channel_content_list:
                list_5.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_5

        except Exception as e:
            print(e)

    def get_head_data6(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a10ab3cdc86cf39001e7")
            r.addBodyPara("channelName", "国际足球")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_6 = {}
            for i in channel_content_list:
                list_6.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_6

        except Exception as e:
            print(e)

    def get_head_data7(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a10bb3cdc86cf39001f8")
            r.addBodyPara("channelName", "社会最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_7 = {}
            for i in channel_content_list:
                list_7.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_7

        except Exception as e:
            print(e)

    def get_head_data8(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001e2")
            r.addBodyPara("channelName", "宏观经济最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_8 = {}
            for i in channel_content_list:
                list_8.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_8

        except Exception as e:
            print(e)

    def get_head_data9(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001e4")
            r.addBodyPara("channelName", "房产最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # print(res.text)
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_9 = {}
            for i in channel_content_list:
                list_9.setdefault(i['title'], i['link'])
                self.add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], '',
                                                   i['content'])
            return list_9

        except Exception as e:
            print(e)

    def get_head(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a109b3cdc86cf39001e0")
            r.addBodyPara("channelName", "财经最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "5")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            desc = []
            link = []
            for i in channel_content_list:
                desc.append(i['desc'])
                link.append(i['link'])
            return desc, link

        except Exception as e:
            print(e)

    def get_lab1(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001d5")
            r.addBodyPara("channelName", "娱乐焦点")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_lab = {}
            for i in channel_content_list:
                list_lab.setdefault(i['title'], i['link'])
            return list_lab

        except Exception as e:
            print(e)

    def get_lab2(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001d6")
            r.addBodyPara("channelName", "游戏焦点")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_lab = {}
            for i in channel_content_list:
                list_lab.setdefault(i['title'], i['link'])
            return list_lab

        except Exception as e:
            print(e)

    def get_lab3(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a10ab3cdc86cf39001ed")
            r.addBodyPara("channelName", "电影最新")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "15")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            list_lab = {}
            for i in channel_content_list:
                list_lab.setdefault(i['title'], i['link'])
            return list_lab

        except Exception as e:
            print(e)

    def get_bot(self):
        try:
            r = ShowapiRequest("http://route.showapi.com/109-35", "926147", "b461cf485c7b48a598064fe428b88ac5")
            r.addBodyPara("channelId", "5572a108b3cdc86cf39001ce")
            r.addBodyPara("channelName", "国际焦点")
            r.addBodyPara("title", "")
            r.addBodyPara("page", "")
            r.addBodyPara("needContent", "1")
            r.addBodyPara("needHtml", "0")
            r.addBodyPara("needAllList", "0")
            r.addBodyPara("maxResult", "3")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']['contentlist']
            title = []
            source = []
            link = []
            desc = []
            for i in channel_content_list:
                title.append(i['title'])
                source.append(i['source'])
                link.append(i['link'])
                desc.append(i['desc'])
                # print(i['title'],i['source'],i['link'])
            return title, source, link, desc

        except Exception as e:
            print(e)


if __name__ == '__main__':
    data = index_data()
    data.get_head_data3()

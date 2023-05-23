from ShowapiRequest import ShowapiRequest
import json
import Postgresql_DB


class get_news_Data:

    def news_channel(self):
        """
        获取新闻频道
        :return:
        """
        try:
            r = ShowapiRequest("http://route.showapi.com/109-34", "926147", "b461cf485c7b48a598064fe428b88ac5")
            res = r.post()
            data_json = json.loads(res.text)
            channelList = data_json['showapi_res_body']
            add_channelid = Postgresql_DB.User_Message()
            for i in channelList['channelList']:
                # add_channelid.insert_channel(i['name'], i['channelId'])
                print(i['channelId'])
                print(i['name'])
        except Exception as e:
            print(e)

    def news_content_china(self):
        """
        获取国内新闻信息入库
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
            r.addBodyPara("maxResult", "20")
            r.addBodyPara("id", "")
            res = r.post()
            # 处理json 数据格式
            data_json_content = json.loads(res.text)
            channel_content_list = data_json_content['showapi_res_body']['pagebean']
            add_insert = Postgresql_DB.User_Message()
            for i in channel_content_list['contentlist']:
                if len(i['imageurls']) == 0:
                    pass
                    # print(i['title'],i['link'],i['pubDate'],i['source'],i['desc'],i['content'])
                else:
                    print(i['imageurls'])

                # add_insert.insert_newsContent(i['title'], i['link'], i['pubDate'], i['source'], i['desc'], i['content'])
        except Exception as e:
            print(e)
            # pass


if __name__ == '__main__':
    getdata = get_news_Data()
    getdata.news_content_china()

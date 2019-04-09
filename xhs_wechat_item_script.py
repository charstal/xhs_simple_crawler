import json
import pymongo
from time import sleep
from config import *


def response(flow):
    global collection
    client = pymongo.MongoClient(MONGO_URL)
    db = client[WECHAT_XHS_MONGO_DB]
    collection = db[WECHAT_XHS_MONGO_COLLECTION]


    url = 'https://www.xiaohongshu.com/sapi/wx_mp_api/sns/v1/note/'
    if flow.request.url.startswith(url):
        # 数据的解析
        # print(flow.request.url)
        for item in json.loads(flow.response.text)["data"]:
            comment_list = []
            for comment in item["comment_list"]:
                content = comment["content"]
                user = comment["user"]["name"]
                comment_item = [user, content]
                comment_list.append(comment_item)

            for note in item["note_list"]:
                note_id = note["id"]
                comment_list.append(note_id)
                user = note["user"]["name"]
                collect_count = note["collected_count"]
                comment_count = note["comments_count"]
                like_count = note["liked_count"]
                share_count = note["shared_count"]
                description = note["desc"]
                img_ist = note["images_list"]
                date = note["time"]

                content = {
                    'note_id': note_id,
                    'user': user,
                    'description': description,
                    'collect_count': collect_count,
                    'comment_count': comment_count,
                    'like_count': like_count,
                    'share_count': share_count,
                    'img_list': img_ist,
                    'date': date,
                    'comment': comment_list
                }

                collection.insert(content)
                # print(content)
            # sleep(SCROLL_SLEEP_TIME)





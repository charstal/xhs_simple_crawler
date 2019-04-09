import json
import pymongo

from config import *


def response(flow):
    global collection
    client = pymongo.MongoClient(MONGO_URL)
    db = client[WECHAT_XHS_MONGO_DB]
    collection = db[WECHAT_XHS_NOTE_MONGO_COLLECTION]

    url1 = 'https://www.xiaohongshu.com/sapi/wx_mp_api/sns/v1/search/notes?'
    url2 = 'https://www.xiaohongshu.com/fe_api/burdock/v1/page/'
    if flow.request.url.startswith(url1):
        # 数据的解析
        print(flow.request.url)

        notes = json.loads(flow.response.text)["data"]["notes"]
        for note in notes:
            note_id = note["id"]
            img_list = note["images_list"]
            title = note["title"]
            user = note["user"]

            content = {
                "note_id": note_id,
                "img_list": img_list,
                "title": title,
                "user":user
            }

            collection.insert(content)

    elif flow.request.url.startswith(url2):
        print(flow.request.url)

        notes = json.loads(flow.response.text)["data"]
        for note in notes:
            note_id = note["id"]
            img_list = note["cover"]
            title = note["title"]
            user = note["user"]

            content = {
                "note_id": note_id,
                "img_list": img_list,
                "title": title,
                "user": user
            }

            collection.insert(content)

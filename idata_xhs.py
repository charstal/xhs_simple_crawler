import json
import re
import time

import pymongo

import requests

from config import *

API_KEY = ""
API_AREA = ""
url = "http://" + API_AREA + "/post/xiaohongshu_ids"


client = pymongo.MongoClient(MONGO_URL)
xhs_db = client[WECHAT_XHS_MONGO_DB]



headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
}

param = {
    'id' : '5a5f1ea9c8e55d32cbe96617',
    'apikey': API_KEY
}


def test():
    r = requests.get(url, headers=headers, params=param)
    json_obj = r.json()
    print(json_obj)


def note_id_read():
    note_id_list = []
    list = xhs_db[WECHAT_XHS_NOTE_MONGO_COLLECTION].find()
    for item in list:
        note_id_list.append(item['note_id'])

    # print(note_id_list)
    return note_id_list


def send_quest(node_id):
    param["id"] = node_id
    count = 0
    while True:
        try:
            r = requests.get(url, headers=headers, params=param)
            json_obj = r.json()
            # print(json_obj)
            if json_obj["retcode"] == "000000":
                save_to_mongo(json_obj)
            return
        except requests.exceptions.RequestException:
            continue
        except json.decoder.JSONDecodeError:
            if count == 3:
                print("note_id:", note_id)
                return
            continue


item_count = 0


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    time.sleep(1)
    f1 = open('log.txt', 'a', encoding="utf-8")
    try:
        if xhs_db[XHS_MONGO_ITEM_COLLECTION].insert(result):
            string = time.ctime() + '  ' + "#" + str(item_count) + ": " + '存储到MongoDB成功:' + result["data"][0]["id"]
            f1.writelines(string + '\n')
            print(string)

    except Exception:
        string = time.ctime() + '  ' + "#" + str(item_count) + ": " + '存储到MongoDB失败:' + result["data"][0]["id"]
        f1.writelines(string + '\n')
        print(string)

    f1.close()

def had_stored_note_id():
    with open('log.txt', 'r', encoding="utf-8") as f:
        text = f.readlines()
        list = []
        pattern = re.compile(r'成功:(\w+)')
        for line in text:
            key = pattern.findall(line)
            if len(key) != 0:
                list.append(key[0])
        return list

if __name__ == "__main__":
    # test()

    # 中断 避免重复项
    note_id_list = note_id_read()
    had_stored_note_id_list = had_stored_note_id()
    note_id_list = [item for item in note_id_list if item not in had_stored_note_id_list]

    # print(note_id_list)

    for note_id in note_id_list:
        send_quest(note_id)
        item_count = item_count + 1
# coding=utf-8
from datetime import datetime
import time
import random


import requests
import hashlib
import json

appKey = "704f1e422b60711902d044c6809ff871"
appSecret = "ba1e233e85e0"
nonce =  "%d"%random.randint(1, 10000)
curTime = "%d"%time.mktime(datetime.utcnow().timetuple())
checkSum = hashlib.sha1(appSecret+nonce+curTime).hexdigest()

headers = {
    "AppKey": appKey,
    "Nonce": nonce,
    "CurTime": curTime,
    "CheckSum": checkSum,

    "Content-Type": "application/json;charset=utf-8"
}

def channel_create(name, type):
    url = "https://vcloud.163.com/app/channel/create"
    data = {
        "name": name,
        "type": int(type)
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.text

def channel_update(name, cid, type):
    url = "https://vcloud.163.com/app/channel/update"
    data = {
        "name": name,
        "cid": cid,
        "type": int(type)
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.text

def channel_delete(cid):
    url = "https://vcloud.163.com/app/channel/delete"
    data = {
        "cid": cid,
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.text

def channel_list(records=10, pnum=1, ofield="ctime", sort=0):
    url = "https://vcloud.163.com/app/channellist"
    data = {
        "records": records,
        "pnum": pnum,
        "ofield": ofield,
        "sort": sort}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.text




if __name__ == '__main__':
    print channel_create("测试3", 0)
    # print(channel_delete("55438719cfa944e9be0ccf9f12758cc0"))
    # print channel_list()
    pass
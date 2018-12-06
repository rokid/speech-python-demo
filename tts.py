#!/usr/bin/python
# coding:utf-8

from websocket import create_connection
import sys
import time
import tts_pb2
import auth_pb2
import hashlib
import threading
import random


class Tts(object):
    def __init__(self, file):
        self.file = file
        self.isAuth = True    # 第一次接到的请求包是认证包
        self.ws = create_connection("wss://apigwws-daily.open.rokid.com/api", timeout=100)
        # 建一个线程，监听服务器发送给客户端的数据
        self.trecv = threading.Thread(target=self.recv)
        self.trecv.start()

    def getMd5(self, content):
        md = hashlib.md5()
        md.update(content)
        return md.hexdigest()

    def recv(self):
        try:
            f = open(self.file, 'wb')
            while self.ws.connected:
                if self.isAuth:
                    resp = auth_pb2.AuthResponse()
                    resp.ParseFromString(self.ws.recv())
                    # SUCCESS = 0  AUTH_FAILED = 1
                    if resp.result == 0:
                        print 'auth:\tsuccess'
                    else:
                        print 'auth:\tfailed'
                        break
                    self.isAuth = False
                else:
                    resp = tts_pb2.TtsResponse()
                    resp.ParseFromString(self.ws.recv())
                    print('result:\t%s' % resp.result)
                    print('text:\t%s' % resp.text)
                    print('voice:\t%d' % len(resp.voice))
                    print('finish:\t%d' % resp.finish)
                    f.write(resp.voice)
                    if resp.finish:
                        break
                print('------------------------------------------')
            f.close()
        except Exception, e:
            print(e)

    def auth(self, key, device_type_id, device_id, secret):
        req = auth_pb2.AuthRequest()
        req.key = key
        req.device_type_id = device_type_id
        req.device_id = device_id
        req.service = "tts"
        req.version = "1.0"
        currentime = str(str(time.time()).split('.')[0])
        req.timestamp = currentime
        src = 'key=' + key + '&device_type_id=' + device_type_id + '&device_id=' + device_id + '&service=' + req.service + '&version=' + req.version + '&time=' + currentime + '&secret=' + secret
        req.sign = self.getMd5(src)
        self.ws.send_binary(req.SerializeToString())

    def send(self, text):
        reqId = random.randint(1, 10000)

        req = tts_pb2.TtsRequest()
        req.id = reqId
        req.text = text
        req.declaimer = "zh"
        req.codec = "pcm"
        self.ws.send_binary(req.SerializeToString())

        print("")


if __name__ == '__main__':

    text = "今天天气怎么样"
    file = "tts.pcm"
    if len(sys.argv) > 2:
        text = sys.argv[1]
        file = sys.argv[2]

    tts = Tts(file)
    tts.auth('fill_your_key_here',
                    'file_your_device_type_here',
                    'file_your_device_id_here',
                    'file_your_secret_here')
    try:
        tts.send(text)
    except Exception, e:
        print(e)

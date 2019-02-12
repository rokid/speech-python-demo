#!/usr/bin/python
# coding:utf-8

from websocket import create_connection
import sys
import time
import speech_pb2   # 生成方法，参考 make.sh
import auth_pb2     # 生成方法，参考 make.sh
import hashlib
import threading
import random


class SpeechText(object):
    def __init__(self):
        self.isAuth = True    # 第一次接到的请求包是认证包
        self.ws = create_connection("wss://apigwws.open.rokid.com/api", timeout=1000)
        # 建一个线程，监听服务器发送给客户端的数据
        self.trecv = threading.Thread(target=self.recv)
        self.trecv.start()

    def getMd5(self, content):
        md = hashlib.md5()
        md.update(content)
        return md.hexdigest()

    def recv(self):
        try:
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
                    resp = speech_pb2.SpeechResponse()
                    resp.ParseFromString(self.ws.recv())
                    print('type:\t%s' % resp.type)
                    print('result:\t%s' % resp.result)
                    print('asr:\t%s' % resp.asr)
                    if resp.nlp:
                        print('nlp:\t%s' % resp.nlp)
                    if resp.action:
                        print('action:\t%s' % resp.action)
                    if resp.extra:
                        print('extra:\t%s' % resp.extra)
                    if resp.vpr:
                        print('vpr:\t%s' % resp.vpr)
                    if len(resp.asr_scores) > 0:
                        print('asr_scores:\t')
                        for i in resp.asr_scores:
                            print("\t%f" % i)
                    if resp.type == 2:
                        break
                print('------------------------------------------')
        except Exception, e:
            print(e)

    def auth(self, key, device_type_id, device_id, secret):
        req = auth_pb2.AuthRequest()
        req.key = key
        req.device_type_id = device_type_id
        req.device_id = device_id
        req.service = "speech"
        req.version = "2.0"
        currentime = str(str(time.time()).split('.')[0])
        req.timestamp = currentime
        src = 'key=' + key + '&device_type_id=' + device_type_id + '&device_id=' + device_id + '&service=' + req.service + '&version=' + req.version + '&time=' + currentime + '&secret=' + secret
        req.sign = self.getMd5(src)
        self.ws.send_binary(req.SerializeToString())

    def send(self, txt):
        reqId = random.randint(1, 10000)

        req = speech_pb2.SpeechRequest()
        req.id = reqId
        req.type = 3  # txt
        req.asr = txt
        self.ws.send_binary(req.SerializeToString())


if __name__ == '__main__':

    txt = u"今天杭州天气怎么样"
    if len(sys.argv) > 1:
        txt = sys.argv[1]

    speechText = SpeechText()
    speechText.auth('fill_your_key_here',
                    'file_your_device_type_here',
                    'file_your_device_id_here',
                    'file_your_secret_here')
    try:
        speechText.send(txt)
    except Exception, e:
        print(e)

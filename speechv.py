#!/usr/bin/python
# coding:utf-8

from websocket import create_connection
import sys
import time
import speech_pb2
import auth_pb2
import hashlib
import threading
import random


class SpeechVoice(object):
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
        reqAuth = auth_pb2.AuthRequest()
        reqAuth.key = key
        reqAuth.device_type_id = device_type_id
        reqAuth.device_id = device_id
        reqAuth.service = "speech"
        reqAuth.version = "2.0"
        currentime = str(str(time.time()).split('.')[0])
        reqAuth.timestamp = currentime
        src = 'key=' + key + '&device_type_id=' + device_type_id + '&device_id=' + device_id + '&service=speech&version=2.0&time=' + currentime + '&secret=' + secret
        reqAuth.sign = self.getMd5(src)
        self.ws.send_binary(reqAuth.SerializeToString())

    def send(self, file):
        reqId = random.randint(1, 10000)

        reqStart = speech_pb2.SpeechRequest()
        reqStart.id = reqId
        reqStart.type = 0  # voice start  发送一个语音发送开始包
        reqStart.options.no_nlp = 1
        reqStart.options.no_intermediate_asr = 1
        self.ws.send_binary(reqStart.SerializeToString())

        with open(file, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                reqVoice = speech_pb2.SpeechRequest()
                reqVoice.id = reqId
                reqVoice.type = 1  # send voice data
                reqVoice.voice = data
                self.ws.send_binary(reqVoice.SerializeToString())
                time.sleep(0.02)
                sys.stdout.write("." + str(len(data)))

        reqEnd = speech_pb2.SpeechRequest()
        reqEnd.id = reqId
        reqEnd.type = 2  # voice end 发送一个语音发送结束包
        self.ws.send_binary(reqEnd.SerializeToString())
        print("")


if __name__ == '__main__':

    file = "weather.pcm"
    if len(sys.argv) > 1:
        file = sys.argv[1]

    speechVoice = SpeechVoice()
    speechVoice.auth('fill_your_key_here',
                    'file_your_device_type_here',
                    'file_your_device_id_here',
                    'file_your_secret_here')
    try:
        speechVoice.send(file)
    except Exception, e:
        print(e)

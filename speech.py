#!/usr/bin/python
# coding:utf-8
from websocket import create_connection
import time
import speech_v1_pb2
import auth_pb2
import hashlib
import threading
import random


class Speech(object):
    def __init__(self):
        self.authFlag = 0    # 第一次接到的请求包是认证包，设置一个变量来标识是否是第一次认证请求
        self.speechRequest = speech_v1_pb2.SpeechRequest()
        self.speechResponse = speech_v1_pb2.SpeechResponse()
        self.authResponse = auth_pb2.AuthResponse()
        self.ws = create_connection("wss://apigwws.open.rokid.com/api", timeout=100)
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
                if self.authFlag == 1:
                    self.speechResponse.ParseFromString(self.ws.recv())
                    print('extra: %s' % self.speechResponse.extra)
                    print('nlp: %s' % self.speechResponse.nlp)
                    print('result: %s' % self.speechResponse.result)
                    print('asr: %s' % self.speechResponse.asr)
                    print('action: %s' % self.speechResponse.action)
                    print('finish: %s' % self.speechResponse.finish)  # self.speechResponse.finish 才表示speech真正的结束
                    print('------------------------------------------')
                else:
                    self.authResponse.ParseFromString(self.ws.recv())
                    # SUCCESS = 0  AUTH_FAILED = 1
                    if self.authResponse.result == 0:
                        print 'auth success'
                    else:
                        print 'auth failed'
        except Exception, e:
            print(e)

    def auth(self, key, device_type_id, device_id, secret):
        authRequest = auth_pb2.AuthRequest()
        authRequest.key = key
        authRequest.device_type_id = device_type_id
        authRequest.device_id = device_id
        authRequest.service = "speech"
        authRequest.version = "1.0"
        currentime = str(str(time.time()).split('.')[0])
        authRequest.timestamp = currentime
        src = 'key=' + key + '&device_type_id=' + device_type_id + '&device_id=' + device_id + '&service=speech&version=1.0&time=' + currentime + '&secret=' + secret
        authRequest.sign = self.getMd5(src)
        self.ws.send_binary(authRequest.SerializeToString())

    def sendVoice(self):
        self.authFlag = 1
        f = open('weather.pcm', 'rb')
        data = f.read()
        speechRequestStart = speech_v1_pb2.SpeechRequest()
        speechId = random.randint(1, 99999)
        speechRequestStart.id = speechId
        speechRequestStart.type = 0  # voice start  发送一个语音发送开始包
        speechRequestStart.lang = "zh"
        speechRequestStart.codec = "pcm"
        self.ws.send_binary(speechRequestStart.SerializeToString())

        speechRequestVoiceData = speech_v1_pb2.SpeechRequest()
        speechRequestVoiceData.id = speechId
        speechRequestVoiceData.type = 1  # send voice data
        speechRequestVoiceData.voice = data
        self.ws.send_binary(speechRequestVoiceData.SerializeToString())

        speechRequestEnd = speech_v1_pb2.SpeechRequest()
        speechRequestEnd.id = speechId
        speechRequestEnd.type = 2  # voice end 发送一个语音发送结束包
        self.ws.send_binary(speechRequestEnd.SerializeToString())


if __name__ == '__main__':
    speech = Speech()
    speech.auth('60659BA5F4D14875A600B8F425994438', '649DCB3204ED413B9838B5C871026681', '4281835E94284245BBFA07852DFA35FD',
                           'E46DD502D5D0407BA68C94F95941983E')
    speech.sendVoice()
    while True:
        try:
            speech.sendVoice()
            time.sleep(60)
        except Exception, e:
            print(e)
            break


    # if authFlag:
    #     speech.sendVoice()

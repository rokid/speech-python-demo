# speech-python-demo

python版本的speech调用demo

### 环境

1. python 版本 2.7
2. pip install websocket websocket-client
3. pip install protobuf

### 设备信息

1. 从 [开放平台](https://developer.rokid.com) 获取 key、sercret、device_type_id 及 device_id
2. 修改 speecht.py、speechv.py、tts.py 中的设备信息

### 运行

``` ./make.sh```

### proto 生成的文件

```auth_pb2.py  speech_pb2.py  speech_types_pb2.py  tts_pb2.py``` 为 ```ws_open``` 目录下 ```proto``` 文件生成的对应文件，以下命令需要依赖这些文件的生成，生成方法可参考 ```make.sh```

### 语音 speech

```python speechv.py file.pcm```

### 文本 speech

```python speecht.py text```

### tts

```python tts.py text file.pcm```




# speech-python-demo

python版本的speech调用demo

### 环境

1. python 版本 2.7
2. pip install websocket websocket-client
3. pip install protobuf
4. protoc

注：
如果不了解以上命令或工具，请放弃使用本项目，尝试 [java](https://github.com/Rokid/rokid-speech) 或其它

### 设备信息

1. 从 [开放平台](https://developer.rokid.com) 获取 key、sercret、device_type_id 及 device_id
2. 修改 speecht.py、speechv.py、tts.py 中的设备信息，请反复确认这些信息**填写的位置是否正确**

### 运行

``` ./make.sh```

注：
1. 如果提示 ```protoc：command not found```，请先视系统不同用系统工具安装 protoc，如 centos 中用 ```yum install protobuf-compiler``` 
2. 如果 import 出错，请先 ```pip uninstall websocket websocket-client```再 ```pip install websocket websocket-client```，再作尝试
3. 如果提示类似 ```python: command not found```，则安装python，或放弃使用本项目，尝试 [java](https://github.com/Rokid/rokid-speech) 或其它

### proto 生成的文件

```auth_pb2.py  speech_pb2.py  speech_types_pb2.py  tts_pb2.py``` 为 ```ws_open``` 目录下 ```proto``` 文件生成的对应文件，以下命令需要依赖这些文件的生成，生成方法可参考 ```make.sh```

### 语音 speech

```python speechv.py weather.pcm```

### 文本 speech

```python speecht.py text```

### tts

```python tts.py text tts.pcm```




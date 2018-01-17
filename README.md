# speech-python-demo
python版本的speech调用demo
###环境：
1）安装websocket模块
2）安装protobuf模块
3）python版本2.7，其它版本没有试验，应该都是可以的
4) 不用再跟进protobuf文件生成python文件了，项目中已经生成好了
###认证信息：
 获取key、sercret、deviceTypeId步骤，登录 https://developer.rokid.com/#/ ，选择语音接入tab页面，然后点击创建新设备按钮，设备创建的第二步中有一个认证文
 件创建，创建完后在你的技能里面把这个语音设备添加进去。这个虚拟的设备只能使用你自己的技能，线上的技能用不了。如果需要请用真实的设备，真实的设备都有这些信息


整个请求交互打印信息示列
extra: {"activation":"none"}
nlp: 
result: 0
asr:今天 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天天气 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天天气 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天天气 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天天气怎么样 
action: 
finish: False
------------------------------------------
extra: 
nlp: 
result: 0
asr:今天天气怎么样 
action: 
finish: False
------------------------------------------
extra: 
nlp: {"appId":"RD311D28837747059F938D3107FCB9F2","appName":"天气","asr":"今天天气怎么样","cloud":true,"intent":"query","pattern":"^($prefix)?($location)?这?($nowtime|$datetime$parttime?|$twoday|$period|$parttime)的?$weather是?$how?$ah?","slots":{"datetime":{"type":"datetime","value":"{\"RelDay\":\"0\",\"text\":\"今天\"}"},"how":{"type":"how","value":"怎么样"},"weather":{"type":"weather","value":"天气"}}}
result: 0
asr:今天天气怎么样 
action:{"appId":"RD311D28837747059F938D3107FCB9F2","response":{"action":{"directives":[{"action":"PLAY","disableEvent":true,"item":{"tts":"杭州市今天多云,气温4到14摄氏度。"},"type":"voice"}],"form":"cut","shouldEndSession":false,"type":"NORMAL","version":"2.0.0"},"card":{"content":"杭州市今天多云,气温4到14摄氏度。","type":"chat"},"resType":"INTENT","respId":"FDB93EED78E541DBBB609FAC257D85BE"},"session":{},"startWithActiveWord":false,"version":"2.0.0"} 
finish: True
------------------------------------------

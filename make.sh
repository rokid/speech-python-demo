#!/bin/bash

protoc --python_out=. -Iws_open/common    ws_open/common/auth.proto
protoc --python_out=. -Iws_open/common/v1 ws_open/common/v1/speech_types.proto
protoc --python_out=Mspeech_types.proto=gitlab.rokid-inc.com/open-platform/protobuf/ws_open/common/v1:. -Iws_open/common/v1:ws_open/speech/v2 ws_open/speech/v2/speech.proto
protoc --python_out=Mspeech_types.proto=gitlab.rokid-inc.com/open-platform/protobuf/ws_open/common/v1:. -Iws_open/common/v1:ws_open/tts/v1 ws_open/tts/v1/tts.proto

echo "=========================================="
echo "=                speechv demo            ="
echo "=========================================="
for pcm in *.pcm; do
	echo
	echo "asr $pcm:"
	python speechv.py $pcm
done

echo "=========================================="
echo "=                speecht demo            ="
echo "=========================================="
python speecht.py

echo "=========================================="
echo "=                    tts demo            ="
echo "=========================================="
python tts.py

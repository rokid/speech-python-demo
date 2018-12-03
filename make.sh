#!/bin/bash

protoc --python_out=ws_open/common    -Iws_open/common    ws_open/common/auth.proto
protoc --python_out=ws_open/common/v1 -Iws_open/common/v1 ws_open/common/v1/speech_types.proto
protoc --python_out=Mspeech_types.proto=gitlab.rokid-inc.com/open-platform/protobuf/ws_open/common/v1:ws_open/speech/v1 -Iws_open/common/v1:ws_open/speech/v1 ws_open/speech/v1/speech.proto
protoc --python_out=Mspeech_types.proto=gitlab.rokid-inc.com/open-platform/protobuf/ws_open/common/v1:ws_open/speech/v2 -Iws_open/common/v1:ws_open/speech/v2 ws_open/speech/v2/speech.proto

find ws_open/ -name '*.py' | xargs -i cp \{\} . -vf

for pcm in *.pcm; do
	echo
	echo "asr $pcm:"
	python speech.py $pcm
done

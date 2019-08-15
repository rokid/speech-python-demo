# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: speech_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='speech_types.proto',
  package='rokid.open.speech.v1',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12speech_types.proto\x12\x14rokid.open.speech.v1\"N\n\x0bPingPayload\x12\x0e\n\x06req_id\x18\x01 \x02(\x05\x12\x0e\n\x06now_tp\x18\x02 \x02(\x04\x12\x0e\n\x06req_tp\x18\x03 \x02(\x04\x12\x0f\n\x07resp_tp\x18\x04 \x02(\x04*\xd1\x01\n\x0fSpeechErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x13\n\x0fUNAUTHENTICATED\x10\x02\x12\x15\n\x11\x43ONNECTION_EXCEED\x10\x03\x12\x15\n\x11RESOURCE_EXHASTED\x10\x04\x12\x08\n\x04\x42USY\x10\x05\x12\x0c\n\x08INTERNAL\x10\x06\x12\x0f\n\x0bVAD_TIMEOUT\x10\x07\x12\r\n\tNLP_EMPTY\x10\x08\x12\x11\n\rUNINITIALIZED\x10\t\x12\x13\n\x0f\x44UP_INITIALIZED\x10\n\x12\x0e\n\nBADREQUEST\x10\x0b*?\n\x07ReqType\x12\t\n\x05START\x10\x00\x12\t\n\x05VOICE\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\x0b\n\x07ONESHOT\x10\x04*b\n\x05\x43odec\x12\x07\n\x03PCM\x10\x00\x12\x07\n\x03OPU\x10\x01\x12\x08\n\x04OPU2\x10\x02\x12\x08\n\x04OPUS\x10\x03\x12\t\n\x05\x41MRNB\x10\x04\x12\t\n\x05\x41MRWB\x10\x05\x12\t\n\x05PCM8K\x10\x06\x12\x07\n\x03WAV\x10\x07\x12\t\n\x05PCM32\x10\x08')
)

_SPEECHERRORCODE = _descriptor.EnumDescriptor(
  name='SpeechErrorCode',
  full_name='rokid.open.speech.v1.SpeechErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHENTICATED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTION_EXCEED', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_EXHASTED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSY', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VAD_TIMEOUT', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NLP_EMPTY', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNINITIALIZED', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUP_INITIALIZED', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADREQUEST', index=10, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=125,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_SPEECHERRORCODE)

SpeechErrorCode = enum_type_wrapper.EnumTypeWrapper(_SPEECHERRORCODE)
_REQTYPE = _descriptor.EnumDescriptor(
  name='ReqType',
  full_name='rokid.open.speech.v1.ReqType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOICE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONESHOT', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=336,
  serialized_end=399,
)
_sym_db.RegisterEnumDescriptor(_REQTYPE)

ReqType = enum_type_wrapper.EnumTypeWrapper(_REQTYPE)
_CODEC = _descriptor.EnumDescriptor(
  name='Codec',
  full_name='rokid.open.speech.v1.Codec',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PCM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPU2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPUS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMRNB', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMRWB', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PCM8K', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAV', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PCM32', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=401,
  serialized_end=499,
)
_sym_db.RegisterEnumDescriptor(_CODEC)

Codec = enum_type_wrapper.EnumTypeWrapper(_CODEC)
SUCCESS = 0
UNAUTHENTICATED = 2
CONNECTION_EXCEED = 3
RESOURCE_EXHASTED = 4
BUSY = 5
INTERNAL = 6
VAD_TIMEOUT = 7
NLP_EMPTY = 8
UNINITIALIZED = 9
DUP_INITIALIZED = 10
BADREQUEST = 11
START = 0
VOICE = 1
END = 2
TEXT = 3
ONESHOT = 4
PCM = 0
OPU = 1
OPU2 = 2
OPUS = 3
AMRNB = 4
AMRWB = 5
PCM8K = 6
WAV = 7
PCM32 = 8



_PINGPAYLOAD = _descriptor.Descriptor(
  name='PingPayload',
  full_name='rokid.open.speech.v1.PingPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req_id', full_name='rokid.open.speech.v1.PingPayload.req_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='now_tp', full_name='rokid.open.speech.v1.PingPayload.now_tp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_tp', full_name='rokid.open.speech.v1.PingPayload.req_tp', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resp_tp', full_name='rokid.open.speech.v1.PingPayload.resp_tp', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['PingPayload'] = _PINGPAYLOAD
DESCRIPTOR.enum_types_by_name['SpeechErrorCode'] = _SPEECHERRORCODE
DESCRIPTOR.enum_types_by_name['ReqType'] = _REQTYPE
DESCRIPTOR.enum_types_by_name['Codec'] = _CODEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingPayload = _reflection.GeneratedProtocolMessageType('PingPayload', (_message.Message,), {
  'DESCRIPTOR' : _PINGPAYLOAD,
  '__module__' : 'speech_types_pb2'
  # @@protoc_insertion_point(class_scope:rokid.open.speech.v1.PingPayload)
  })
_sym_db.RegisterMessage(PingPayload)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: incoming_data_push.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import record_batch_pb2 as record__batch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='incoming_data_push.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18incoming_data_push.proto\x12\x03sdk\x1a\x12record_batch.proto\"h\n\x10IncomingDataPush\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12&\n\x0crecord_batch\x18\x03 \x01(\x0b\x32\x10.sdk.RecordBatchb\x06proto3'
  ,
  dependencies=[record__batch__pb2.DESCRIPTOR,])




_INCOMINGDATAPUSH = _descriptor.Descriptor(
  name='IncomingDataPush',
  full_name='sdk.IncomingDataPush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.IncomingDataPush.anchor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_name', full_name='sdk.IncomingDataPush.connection_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record_batch', full_name='sdk.IncomingDataPush.record_batch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=157,
)

_INCOMINGDATAPUSH.fields_by_name['record_batch'].message_type = record__batch__pb2._RECORDBATCH
DESCRIPTOR.message_types_by_name['IncomingDataPush'] = _INCOMINGDATAPUSH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomingDataPush = _reflection.GeneratedProtocolMessageType('IncomingDataPush', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGDATAPUSH,
  '__module__' : 'incoming_data_push_pb2'
  # @@protoc_insertion_point(class_scope:sdk.IncomingDataPush)
  })
_sym_db.RegisterMessage(IncomingDataPush)


# @@protoc_insertion_point(module_scope)

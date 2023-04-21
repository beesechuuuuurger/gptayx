# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: incoming_record_packet_push.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import record_packet_pb2 as record__packet__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='incoming_record_packet_push.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!incoming_record_packet_push.proto\x12\x03sdk\x1a\x13record_packet.proto\"r\n\x18IncomingRecordPacketPush\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12(\n\rrecord_packet\x18\x03 \x01(\x0b\x32\x11.sdk.RecordPacketb\x06proto3'
  ,
  dependencies=[record__packet__pb2.DESCRIPTOR,])




_INCOMINGRECORDPACKETPUSH = _descriptor.Descriptor(
  name='IncomingRecordPacketPush',
  full_name='sdk.IncomingRecordPacketPush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.IncomingRecordPacketPush.anchor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_name', full_name='sdk.IncomingRecordPacketPush.connection_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record_packet', full_name='sdk.IncomingRecordPacketPush.record_packet', index=2,
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
  serialized_start=63,
  serialized_end=177,
)

_INCOMINGRECORDPACKETPUSH.fields_by_name['record_packet'].message_type = record__packet__pb2._RECORDPACKET
DESCRIPTOR.message_types_by_name['IncomingRecordPacketPush'] = _INCOMINGRECORDPACKETPUSH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomingRecordPacketPush = _reflection.GeneratedProtocolMessageType('IncomingRecordPacketPush', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGRECORDPACKETPUSH,
  '__module__' : 'incoming_record_packet_push_pb2'
  # @@protoc_insertion_point(class_scope:sdk.IncomingRecordPacketPush)
  })
_sym_db.RegisterMessage(IncomingRecordPacketPush)


# @@protoc_insertion_point(module_scope)
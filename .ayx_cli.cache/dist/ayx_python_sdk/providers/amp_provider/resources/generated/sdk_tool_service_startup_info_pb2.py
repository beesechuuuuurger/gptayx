# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk_tool_service_startup_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk_tool_service_startup_info.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#sdk_tool_service_startup_info.proto\x12\x03sdk\"^\n\x19SdkToolServiceStartupInfo\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1f\n\x17sdk_tool_server_address\x18\x03 \x01(\tb\x06proto3'
)




_SDKTOOLSERVICESTARTUPINFO = _descriptor.Descriptor(
  name='SdkToolServiceStartupInfo',
  full_name='sdk.SdkToolServiceStartupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='sdk.SdkToolServiceStartupInfo.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='sdk.SdkToolServiceStartupInfo.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdk_tool_server_address', full_name='sdk.SdkToolServiceStartupInfo.sdk_tool_server_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=44,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['SdkToolServiceStartupInfo'] = _SDKTOOLSERVICESTARTUPINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SdkToolServiceStartupInfo = _reflection.GeneratedProtocolMessageType('SdkToolServiceStartupInfo', (_message.Message,), {
  'DESCRIPTOR' : _SDKTOOLSERVICESTARTUPINFO,
  '__module__' : 'sdk_tool_service_startup_info_pb2'
  # @@protoc_insertion_point(class_scope:sdk.SdkToolServiceStartupInfo)
  })
_sym_db.RegisterMessage(SdkToolServiceStartupInfo)


# @@protoc_insertion_point(module_scope)

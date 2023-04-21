# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: output_message_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='output_message_data.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19output_message_data.proto\x12\x03sdk\"S\n\x11OutputMessageData\x12-\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x17.sdk.OutputMessageTypes\x12\x0f\n\x07message\x18\x02 \x01(\t*\x96\x01\n\x12OutputMessageTypes\x12\x0c\n\x08OMT_None\x10\x00\x12\x0c\n\x08OMT_Info\x10\x01\x12\x0f\n\x0bOMT_Warning\x10\x02\x12\r\n\tOMT_Error\x10\x03\x12\x11\n\rOMT_FileInput\x10\x08\x12\x12\n\x0eOMT_FileOutput\x10\t\x12\x1d\n\x19OMT_UpdateOutputConfigXml\x10\x0b\x62\x06proto3'
)

_OUTPUTMESSAGETYPES = _descriptor.EnumDescriptor(
  name='OutputMessageTypes',
  full_name='sdk.OutputMessageTypes',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OMT_None', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_Info', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_Warning', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_Error', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_FileInput', index=4, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_FileOutput', index=5, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OMT_UpdateOutputConfigXml', index=6, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=120,
  serialized_end=270,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTMESSAGETYPES)

OutputMessageTypes = enum_type_wrapper.EnumTypeWrapper(_OUTPUTMESSAGETYPES)
OMT_None = 0
OMT_Info = 1
OMT_Warning = 2
OMT_Error = 3
OMT_FileInput = 8
OMT_FileOutput = 9
OMT_UpdateOutputConfigXml = 11



_OUTPUTMESSAGEDATA = _descriptor.Descriptor(
  name='OutputMessageData',
  full_name='sdk.OutputMessageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='sdk.OutputMessageData.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='sdk.OutputMessageData.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=117,
)

_OUTPUTMESSAGEDATA.fields_by_name['message_type'].enum_type = _OUTPUTMESSAGETYPES
DESCRIPTOR.message_types_by_name['OutputMessageData'] = _OUTPUTMESSAGEDATA
DESCRIPTOR.enum_types_by_name['OutputMessageTypes'] = _OUTPUTMESSAGETYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutputMessageData = _reflection.GeneratedProtocolMessageType('OutputMessageData', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTMESSAGEDATA,
  '__module__' : 'output_message_data_pb2'
  # @@protoc_insertion_point(class_scope:sdk.OutputMessageData)
  })
_sym_db.RegisterMessage(OutputMessageData)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dcm_e.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dcm_e.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x64\x63m_e.proto\x12\x03sdk\x1a\x1cgoogle/protobuf/struct.proto\"\xe3\x05\n\x0b\x44\x63mERequest\x12!\n\x02v2\x18\x01 \x01(\x0b\x32\x13.sdk.DcmERequest.V2H\x00\x1a\xa5\x05\n\x02V2\x12;\n\x0eget_connection\x18\x01 \x01(\x0b\x32!.sdk.DcmERequest.V2.GetConnectionH\x00\x12\x35\n\x0block_secret\x18\x02 \x01(\x0b\x32\x1e.sdk.DcmERequest.V2.LockSecretH\x00\x12\x39\n\runlock_secret\x18\x03 \x01(\x0b\x32 .sdk.DcmERequest.V2.UnlockSecretH\x00\x12\x39\n\rupdate_secret\x18\x04 \x01(\x0b\x32 .sdk.DcmERequest.V2.UpdateSecretH\x00\x1a&\n\rGetConnection\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x1a\x65\n\nLockSecret\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x17\n\x0f\x63redential_role\x18\x02 \x01(\t\x12\x13\n\x0bsecret_type\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\t\x1a\x64\n\x0cUnlockSecret\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x17\n\x0f\x63redential_role\x18\x02 \x01(\t\x12\x13\n\x0bsecret_type\x18\x03 \x01(\t\x12\x0f\n\x07lock_id\x18\x04 \x01(\t\x1a\xb4\x01\n\x0cUpdateSecret\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x17\n\x0f\x63redential_role\x18\x02 \x01(\t\x12\x13\n\x0bsecret_type\x18\x03 \x01(\t\x12\x0f\n\x07lock_id\x18\x04 \x01(\t\x12\x12\n\nexpires_on\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t\x12+\n\nparameters\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructB\t\n\x07RequestB\t\n\x07Request\"J\n\x0c\x44\x63mEResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12)\n\x08response\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_DCMEREQUEST_V2_GETCONNECTION = _descriptor.Descriptor(
  name='GetConnection',
  full_name='sdk.DcmERequest.V2.GetConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='sdk.DcmERequest.V2.GetConnection.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=342,
  serialized_end=380,
)

_DCMEREQUEST_V2_LOCKSECRET = _descriptor.Descriptor(
  name='LockSecret',
  full_name='sdk.DcmERequest.V2.LockSecret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='sdk.DcmERequest.V2.LockSecret.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credential_role', full_name='sdk.DcmERequest.V2.LockSecret.credential_role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='sdk.DcmERequest.V2.LockSecret.secret_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires_in', full_name='sdk.DcmERequest.V2.LockSecret.expires_in', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=382,
  serialized_end=483,
)

_DCMEREQUEST_V2_UNLOCKSECRET = _descriptor.Descriptor(
  name='UnlockSecret',
  full_name='sdk.DcmERequest.V2.UnlockSecret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='sdk.DcmERequest.V2.UnlockSecret.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credential_role', full_name='sdk.DcmERequest.V2.UnlockSecret.credential_role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='sdk.DcmERequest.V2.UnlockSecret.secret_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lock_id', full_name='sdk.DcmERequest.V2.UnlockSecret.lock_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=485,
  serialized_end=585,
)

_DCMEREQUEST_V2_UPDATESECRET = _descriptor.Descriptor(
  name='UpdateSecret',
  full_name='sdk.DcmERequest.V2.UpdateSecret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='sdk.DcmERequest.V2.UpdateSecret.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credential_role', full_name='sdk.DcmERequest.V2.UpdateSecret.credential_role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='sdk.DcmERequest.V2.UpdateSecret.secret_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lock_id', full_name='sdk.DcmERequest.V2.UpdateSecret.lock_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires_on', full_name='sdk.DcmERequest.V2.UpdateSecret.expires_on', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='sdk.DcmERequest.V2.UpdateSecret.value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='sdk.DcmERequest.V2.UpdateSecret.parameters', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=588,
  serialized_end=768,
)

_DCMEREQUEST_V2 = _descriptor.Descriptor(
  name='V2',
  full_name='sdk.DcmERequest.V2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_connection', full_name='sdk.DcmERequest.V2.get_connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lock_secret', full_name='sdk.DcmERequest.V2.lock_secret', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unlock_secret', full_name='sdk.DcmERequest.V2.unlock_secret', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_secret', full_name='sdk.DcmERequest.V2.update_secret', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DCMEREQUEST_V2_GETCONNECTION, _DCMEREQUEST_V2_LOCKSECRET, _DCMEREQUEST_V2_UNLOCKSECRET, _DCMEREQUEST_V2_UPDATESECRET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Request', full_name='sdk.DcmERequest.V2.Request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=102,
  serialized_end=779,
)

_DCMEREQUEST = _descriptor.Descriptor(
  name='DcmERequest',
  full_name='sdk.DcmERequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v2', full_name='sdk.DcmERequest.v2', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DCMEREQUEST_V2, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Request', full_name='sdk.DcmERequest.Request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=51,
  serialized_end=790,
)


_DCMERESPONSE = _descriptor.Descriptor(
  name='DcmEResponse',
  full_name='sdk.DcmEResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='sdk.DcmEResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='sdk.DcmEResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=792,
  serialized_end=866,
)

_DCMEREQUEST_V2_GETCONNECTION.containing_type = _DCMEREQUEST_V2
_DCMEREQUEST_V2_LOCKSECRET.containing_type = _DCMEREQUEST_V2
_DCMEREQUEST_V2_UNLOCKSECRET.containing_type = _DCMEREQUEST_V2
_DCMEREQUEST_V2_UPDATESECRET.fields_by_name['parameters'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DCMEREQUEST_V2_UPDATESECRET.containing_type = _DCMEREQUEST_V2
_DCMEREQUEST_V2.fields_by_name['get_connection'].message_type = _DCMEREQUEST_V2_GETCONNECTION
_DCMEREQUEST_V2.fields_by_name['lock_secret'].message_type = _DCMEREQUEST_V2_LOCKSECRET
_DCMEREQUEST_V2.fields_by_name['unlock_secret'].message_type = _DCMEREQUEST_V2_UNLOCKSECRET
_DCMEREQUEST_V2.fields_by_name['update_secret'].message_type = _DCMEREQUEST_V2_UPDATESECRET
_DCMEREQUEST_V2.containing_type = _DCMEREQUEST
_DCMEREQUEST_V2.oneofs_by_name['Request'].fields.append(
  _DCMEREQUEST_V2.fields_by_name['get_connection'])
_DCMEREQUEST_V2.fields_by_name['get_connection'].containing_oneof = _DCMEREQUEST_V2.oneofs_by_name['Request']
_DCMEREQUEST_V2.oneofs_by_name['Request'].fields.append(
  _DCMEREQUEST_V2.fields_by_name['lock_secret'])
_DCMEREQUEST_V2.fields_by_name['lock_secret'].containing_oneof = _DCMEREQUEST_V2.oneofs_by_name['Request']
_DCMEREQUEST_V2.oneofs_by_name['Request'].fields.append(
  _DCMEREQUEST_V2.fields_by_name['unlock_secret'])
_DCMEREQUEST_V2.fields_by_name['unlock_secret'].containing_oneof = _DCMEREQUEST_V2.oneofs_by_name['Request']
_DCMEREQUEST_V2.oneofs_by_name['Request'].fields.append(
  _DCMEREQUEST_V2.fields_by_name['update_secret'])
_DCMEREQUEST_V2.fields_by_name['update_secret'].containing_oneof = _DCMEREQUEST_V2.oneofs_by_name['Request']
_DCMEREQUEST.fields_by_name['v2'].message_type = _DCMEREQUEST_V2
_DCMEREQUEST.oneofs_by_name['Request'].fields.append(
  _DCMEREQUEST.fields_by_name['v2'])
_DCMEREQUEST.fields_by_name['v2'].containing_oneof = _DCMEREQUEST.oneofs_by_name['Request']
_DCMERESPONSE.fields_by_name['response'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['DcmERequest'] = _DCMEREQUEST
DESCRIPTOR.message_types_by_name['DcmEResponse'] = _DCMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DcmERequest = _reflection.GeneratedProtocolMessageType('DcmERequest', (_message.Message,), {

  'V2' : _reflection.GeneratedProtocolMessageType('V2', (_message.Message,), {

    'GetConnection' : _reflection.GeneratedProtocolMessageType('GetConnection', (_message.Message,), {
      'DESCRIPTOR' : _DCMEREQUEST_V2_GETCONNECTION,
      '__module__' : 'dcm_e_pb2'
      # @@protoc_insertion_point(class_scope:sdk.DcmERequest.V2.GetConnection)
      })
    ,

    'LockSecret' : _reflection.GeneratedProtocolMessageType('LockSecret', (_message.Message,), {
      'DESCRIPTOR' : _DCMEREQUEST_V2_LOCKSECRET,
      '__module__' : 'dcm_e_pb2'
      # @@protoc_insertion_point(class_scope:sdk.DcmERequest.V2.LockSecret)
      })
    ,

    'UnlockSecret' : _reflection.GeneratedProtocolMessageType('UnlockSecret', (_message.Message,), {
      'DESCRIPTOR' : _DCMEREQUEST_V2_UNLOCKSECRET,
      '__module__' : 'dcm_e_pb2'
      # @@protoc_insertion_point(class_scope:sdk.DcmERequest.V2.UnlockSecret)
      })
    ,

    'UpdateSecret' : _reflection.GeneratedProtocolMessageType('UpdateSecret', (_message.Message,), {
      'DESCRIPTOR' : _DCMEREQUEST_V2_UPDATESECRET,
      '__module__' : 'dcm_e_pb2'
      # @@protoc_insertion_point(class_scope:sdk.DcmERequest.V2.UpdateSecret)
      })
    ,
    'DESCRIPTOR' : _DCMEREQUEST_V2,
    '__module__' : 'dcm_e_pb2'
    # @@protoc_insertion_point(class_scope:sdk.DcmERequest.V2)
    })
  ,
  'DESCRIPTOR' : _DCMEREQUEST,
  '__module__' : 'dcm_e_pb2'
  # @@protoc_insertion_point(class_scope:sdk.DcmERequest)
  })
_sym_db.RegisterMessage(DcmERequest)
_sym_db.RegisterMessage(DcmERequest.V2)
_sym_db.RegisterMessage(DcmERequest.V2.GetConnection)
_sym_db.RegisterMessage(DcmERequest.V2.LockSecret)
_sym_db.RegisterMessage(DcmERequest.V2.UnlockSecret)
_sym_db.RegisterMessage(DcmERequest.V2.UpdateSecret)

DcmEResponse = _reflection.GeneratedProtocolMessageType('DcmEResponse', (_message.Message,), {
  'DESCRIPTOR' : _DCMERESPONSE,
  '__module__' : 'dcm_e_pb2'
  # @@protoc_insertion_point(class_scope:sdk.DcmEResponse)
  })
_sym_db.RegisterMessage(DcmEResponse)


# @@protoc_insertion_point(module_scope)

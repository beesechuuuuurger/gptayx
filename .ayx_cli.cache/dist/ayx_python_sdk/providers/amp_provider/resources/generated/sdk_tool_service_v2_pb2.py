# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk_tool_service_v2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import close_outgoing_anchor_pb2 as close__outgoing__anchor__pb2
from . import incoming_connection_complete_pb2 as incoming__connection__complete__pb2
from . import translate_message_data_pb2 as translate__message__data__pb2
from . import outgoing_metadata_push_pb2 as outgoing__metadata__push__pb2
from . import output_message_data_pb2 as output__message__data__pb2
from . import password_data_pb2 as password__data__pb2
from . import plugin_initialization_data_pb2 as plugin__initialization__data__pb2
from . import dcm_e_pb2 as dcm__e__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sdk_tool_service_v2.proto',
  package='sdk',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19sdk_tool_service_v2.proto\x12\x03sdk\x1a\x1b\x63lose_outgoing_anchor.proto\x1a\"incoming_connection_complete.proto\x1a\x1ctranslate_message_data.proto\x1a\x1coutgoing_metadata_push.proto\x1a\x19output_message_data.proto\x1a\x13password_data.proto\x1a plugin_initialization_data.proto\x1a\x0b\x64\x63m_e.proto\"\x94\x03\n\tControlIn\x12\x43\n\x1aplugin_initialization_data\x18\x01 \x01(\x0b\x32\x1d.sdk.PluginInitializationDataH\x00\x12\x34\n\x12translated_message\x18\x02 \x01(\x0b\x32\x16.sdk.TranslatedMessageH\x00\x12/\n\x12\x64\x65\x63rypted_password\x18\x03 \x01(\x0b\x32\x11.sdk.PasswordDataH\x00\x12\x38\n\x0fnotify_complete\x18\x04 \x01(\x0b\x32\x1d.sdk.ControlIn.NotifyCompleteH\x00\x12+\n\x0e\x64\x63m_e_response\x18\x05 \x01(\x0b\x32\x11.sdk.DcmEResponseH\x00\x12G\n\x1cincoming_connection_complete\x18\x06 \x01(\x0b\x32\x1f.sdk.IncomingConnectionCompleteH\x00\x12\x0e\n\x06msg_id\x18\x07 \x01(\t\x1a\x10\n\x0eNotifyCompleteB\t\n\x07payload\"\xf3\x02\n\nControlOut\x12\x36\n\x11outgoing_metadata\x18\x01 \x01(\x0b\x32\x19.sdk.OutgoingMetadataPushH\x00\x12\x30\n\x0eoutput_message\x18\x02 \x01(\x0b\x32\x16.sdk.OutputMessageDataH\x00\x12\x36\n\x11translate_message\x18\x03 \x01(\x0b\x32\x19.sdk.TranslateMessageDataH\x00\x12-\n\x10\x64\x65\x63rypt_password\x18\x04 \x01(\x0b\x32\x11.sdk.PasswordDataH\x00\x12;\n\x10\x63onfirm_complete\x18\x05 \x01(\x0b\x32\x1f.sdk.ControlOut.ConfirmCompleteH\x00\x12)\n\rdcm_e_request\x18\x06 \x01(\x0b\x32\x10.sdk.DcmERequestH\x00\x12\x0e\n\x06msg_id\x18\x07 \x01(\t\x1a\x11\n\x0f\x43onfirmCompleteB\t\n\x07payload\"\xf3\x02\n\x10RecordTransferIn\x12\x41\n\x10incoming_records\x18\x01 \x01(\x0b\x32%.sdk.RecordTransferIn.IncomingRecordsH\x00\x12=\n\x0erecord_request\x18\x02 \x01(\x0b\x32#.sdk.RecordTransferIn.RecordRequestH\x00\x12G\n\x1cincoming_connection_complete\x18\x03 \x01(\x0b\x32\x1f.sdk.IncomingConnectionCompleteH\x00\x1a\x63\n\x0fIncomingRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x14\n\x0c\x65nd_of_chunk\x18\x04 \x01(\x08\x1a$\n\rRecordRequest\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\tB\t\n\x07payload\"\"\n\x0bWantRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\"c\n\x0fOutgoingRecords\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63onnection_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x14\n\x0c\x65nd_of_chunk\x18\x04 \x01(\x08\"\xb5\x01\n\x11RecordTransferOut\x12(\n\x0cwant_records\x18\x01 \x01(\x0b\x32\x10.sdk.WantRecordsH\x00\x12\x30\n\x10outgoing_records\x18\x02 \x01(\x0b\x32\x14.sdk.OutgoingRecordsH\x00\x12\x39\n\x15\x63lose_outgoing_anchor\x18\x03 \x01(\x0b\x32\x18.sdk.CloseOutgoingAnchorH\x00\x42\t\n\x07payload2\x80\x01\n\tSdkToolV2\x12.\n\x07\x43ontrol\x12\x0e.sdk.ControlIn\x1a\x0f.sdk.ControlOut(\x01\x30\x01\x12\x43\n\x0eRecordTransfer\x12\x15.sdk.RecordTransferIn\x1a\x16.sdk.RecordTransferOut(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[close__outgoing__anchor__pb2.DESCRIPTOR,incoming__connection__complete__pb2.DESCRIPTOR,translate__message__data__pb2.DESCRIPTOR,outgoing__metadata__push__pb2.DESCRIPTOR,output__message__data__pb2.DESCRIPTOR,password__data__pb2.DESCRIPTOR,plugin__initialization__data__pb2.DESCRIPTOR,dcm__e__pb2.DESCRIPTOR,])




_CONTROLIN_NOTIFYCOMPLETE = _descriptor.Descriptor(
  name='NotifyComplete',
  full_name='sdk.ControlIn.NotifyComplete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=632,
  serialized_end=648,
)

_CONTROLIN = _descriptor.Descriptor(
  name='ControlIn',
  full_name='sdk.ControlIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_initialization_data', full_name='sdk.ControlIn.plugin_initialization_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='translated_message', full_name='sdk.ControlIn.translated_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decrypted_password', full_name='sdk.ControlIn.decrypted_password', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_complete', full_name='sdk.ControlIn.notify_complete', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dcm_e_response', full_name='sdk.ControlIn.dcm_e_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incoming_connection_complete', full_name='sdk.ControlIn.incoming_connection_complete', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='sdk.ControlIn.msg_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTROLIN_NOTIFYCOMPLETE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='sdk.ControlIn.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=255,
  serialized_end=659,
)


_CONTROLOUT_CONFIRMCOMPLETE = _descriptor.Descriptor(
  name='ConfirmComplete',
  full_name='sdk.ControlOut.ConfirmComplete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1005,
  serialized_end=1022,
)

_CONTROLOUT = _descriptor.Descriptor(
  name='ControlOut',
  full_name='sdk.ControlOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='outgoing_metadata', full_name='sdk.ControlOut.outgoing_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_message', full_name='sdk.ControlOut.output_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='translate_message', full_name='sdk.ControlOut.translate_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decrypt_password', full_name='sdk.ControlOut.decrypt_password', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confirm_complete', full_name='sdk.ControlOut.confirm_complete', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dcm_e_request', full_name='sdk.ControlOut.dcm_e_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='sdk.ControlOut.msg_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTROLOUT_CONFIRMCOMPLETE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='sdk.ControlOut.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=662,
  serialized_end=1033,
)


_RECORDTRANSFERIN_INCOMINGRECORDS = _descriptor.Descriptor(
  name='IncomingRecords',
  full_name='sdk.RecordTransferIn.IncomingRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.RecordTransferIn.IncomingRecords.anchor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_name', full_name='sdk.RecordTransferIn.IncomingRecords.connection_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='sdk.RecordTransferIn.IncomingRecords.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_of_chunk', full_name='sdk.RecordTransferIn.IncomingRecords.end_of_chunk', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1259,
  serialized_end=1358,
)

_RECORDTRANSFERIN_RECORDREQUEST = _descriptor.Descriptor(
  name='RecordRequest',
  full_name='sdk.RecordTransferIn.RecordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.RecordTransferIn.RecordRequest.anchor_name', index=0,
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
  serialized_start=1360,
  serialized_end=1396,
)

_RECORDTRANSFERIN = _descriptor.Descriptor(
  name='RecordTransferIn',
  full_name='sdk.RecordTransferIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='incoming_records', full_name='sdk.RecordTransferIn.incoming_records', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record_request', full_name='sdk.RecordTransferIn.record_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incoming_connection_complete', full_name='sdk.RecordTransferIn.incoming_connection_complete', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RECORDTRANSFERIN_INCOMINGRECORDS, _RECORDTRANSFERIN_RECORDREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='sdk.RecordTransferIn.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1036,
  serialized_end=1407,
)


_WANTRECORDS = _descriptor.Descriptor(
  name='WantRecords',
  full_name='sdk.WantRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.WantRecords.anchor_name', index=0,
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
  serialized_start=1409,
  serialized_end=1443,
)


_OUTGOINGRECORDS = _descriptor.Descriptor(
  name='OutgoingRecords',
  full_name='sdk.OutgoingRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_name', full_name='sdk.OutgoingRecords.anchor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_name', full_name='sdk.OutgoingRecords.connection_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='sdk.OutgoingRecords.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_of_chunk', full_name='sdk.OutgoingRecords.end_of_chunk', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1445,
  serialized_end=1544,
)


_RECORDTRANSFEROUT = _descriptor.Descriptor(
  name='RecordTransferOut',
  full_name='sdk.RecordTransferOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='want_records', full_name='sdk.RecordTransferOut.want_records', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outgoing_records', full_name='sdk.RecordTransferOut.outgoing_records', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close_outgoing_anchor', full_name='sdk.RecordTransferOut.close_outgoing_anchor', index=2,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='sdk.RecordTransferOut.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1547,
  serialized_end=1728,
)

_CONTROLIN_NOTIFYCOMPLETE.containing_type = _CONTROLIN
_CONTROLIN.fields_by_name['plugin_initialization_data'].message_type = plugin__initialization__data__pb2._PLUGININITIALIZATIONDATA
_CONTROLIN.fields_by_name['translated_message'].message_type = translate__message__data__pb2._TRANSLATEDMESSAGE
_CONTROLIN.fields_by_name['decrypted_password'].message_type = password__data__pb2._PASSWORDDATA
_CONTROLIN.fields_by_name['notify_complete'].message_type = _CONTROLIN_NOTIFYCOMPLETE
_CONTROLIN.fields_by_name['dcm_e_response'].message_type = dcm__e__pb2._DCMERESPONSE
_CONTROLIN.fields_by_name['incoming_connection_complete'].message_type = incoming__connection__complete__pb2._INCOMINGCONNECTIONCOMPLETE
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['plugin_initialization_data'])
_CONTROLIN.fields_by_name['plugin_initialization_data'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['translated_message'])
_CONTROLIN.fields_by_name['translated_message'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['decrypted_password'])
_CONTROLIN.fields_by_name['decrypted_password'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['notify_complete'])
_CONTROLIN.fields_by_name['notify_complete'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['dcm_e_response'])
_CONTROLIN.fields_by_name['dcm_e_response'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLIN.oneofs_by_name['payload'].fields.append(
  _CONTROLIN.fields_by_name['incoming_connection_complete'])
_CONTROLIN.fields_by_name['incoming_connection_complete'].containing_oneof = _CONTROLIN.oneofs_by_name['payload']
_CONTROLOUT_CONFIRMCOMPLETE.containing_type = _CONTROLOUT
_CONTROLOUT.fields_by_name['outgoing_metadata'].message_type = outgoing__metadata__push__pb2._OUTGOINGMETADATAPUSH
_CONTROLOUT.fields_by_name['output_message'].message_type = output__message__data__pb2._OUTPUTMESSAGEDATA
_CONTROLOUT.fields_by_name['translate_message'].message_type = translate__message__data__pb2._TRANSLATEMESSAGEDATA
_CONTROLOUT.fields_by_name['decrypt_password'].message_type = password__data__pb2._PASSWORDDATA
_CONTROLOUT.fields_by_name['confirm_complete'].message_type = _CONTROLOUT_CONFIRMCOMPLETE
_CONTROLOUT.fields_by_name['dcm_e_request'].message_type = dcm__e__pb2._DCMEREQUEST
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['outgoing_metadata'])
_CONTROLOUT.fields_by_name['outgoing_metadata'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['output_message'])
_CONTROLOUT.fields_by_name['output_message'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['translate_message'])
_CONTROLOUT.fields_by_name['translate_message'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['decrypt_password'])
_CONTROLOUT.fields_by_name['decrypt_password'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['confirm_complete'])
_CONTROLOUT.fields_by_name['confirm_complete'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_CONTROLOUT.oneofs_by_name['payload'].fields.append(
  _CONTROLOUT.fields_by_name['dcm_e_request'])
_CONTROLOUT.fields_by_name['dcm_e_request'].containing_oneof = _CONTROLOUT.oneofs_by_name['payload']
_RECORDTRANSFERIN_INCOMINGRECORDS.containing_type = _RECORDTRANSFERIN
_RECORDTRANSFERIN_RECORDREQUEST.containing_type = _RECORDTRANSFERIN
_RECORDTRANSFERIN.fields_by_name['incoming_records'].message_type = _RECORDTRANSFERIN_INCOMINGRECORDS
_RECORDTRANSFERIN.fields_by_name['record_request'].message_type = _RECORDTRANSFERIN_RECORDREQUEST
_RECORDTRANSFERIN.fields_by_name['incoming_connection_complete'].message_type = incoming__connection__complete__pb2._INCOMINGCONNECTIONCOMPLETE
_RECORDTRANSFERIN.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFERIN.fields_by_name['incoming_records'])
_RECORDTRANSFERIN.fields_by_name['incoming_records'].containing_oneof = _RECORDTRANSFERIN.oneofs_by_name['payload']
_RECORDTRANSFERIN.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFERIN.fields_by_name['record_request'])
_RECORDTRANSFERIN.fields_by_name['record_request'].containing_oneof = _RECORDTRANSFERIN.oneofs_by_name['payload']
_RECORDTRANSFERIN.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFERIN.fields_by_name['incoming_connection_complete'])
_RECORDTRANSFERIN.fields_by_name['incoming_connection_complete'].containing_oneof = _RECORDTRANSFERIN.oneofs_by_name['payload']
_RECORDTRANSFEROUT.fields_by_name['want_records'].message_type = _WANTRECORDS
_RECORDTRANSFEROUT.fields_by_name['outgoing_records'].message_type = _OUTGOINGRECORDS
_RECORDTRANSFEROUT.fields_by_name['close_outgoing_anchor'].message_type = close__outgoing__anchor__pb2._CLOSEOUTGOINGANCHOR
_RECORDTRANSFEROUT.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFEROUT.fields_by_name['want_records'])
_RECORDTRANSFEROUT.fields_by_name['want_records'].containing_oneof = _RECORDTRANSFEROUT.oneofs_by_name['payload']
_RECORDTRANSFEROUT.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFEROUT.fields_by_name['outgoing_records'])
_RECORDTRANSFEROUT.fields_by_name['outgoing_records'].containing_oneof = _RECORDTRANSFEROUT.oneofs_by_name['payload']
_RECORDTRANSFEROUT.oneofs_by_name['payload'].fields.append(
  _RECORDTRANSFEROUT.fields_by_name['close_outgoing_anchor'])
_RECORDTRANSFEROUT.fields_by_name['close_outgoing_anchor'].containing_oneof = _RECORDTRANSFEROUT.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['ControlIn'] = _CONTROLIN
DESCRIPTOR.message_types_by_name['ControlOut'] = _CONTROLOUT
DESCRIPTOR.message_types_by_name['RecordTransferIn'] = _RECORDTRANSFERIN
DESCRIPTOR.message_types_by_name['WantRecords'] = _WANTRECORDS
DESCRIPTOR.message_types_by_name['OutgoingRecords'] = _OUTGOINGRECORDS
DESCRIPTOR.message_types_by_name['RecordTransferOut'] = _RECORDTRANSFEROUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlIn = _reflection.GeneratedProtocolMessageType('ControlIn', (_message.Message,), {

  'NotifyComplete' : _reflection.GeneratedProtocolMessageType('NotifyComplete', (_message.Message,), {
    'DESCRIPTOR' : _CONTROLIN_NOTIFYCOMPLETE,
    '__module__' : 'sdk_tool_service_v2_pb2'
    # @@protoc_insertion_point(class_scope:sdk.ControlIn.NotifyComplete)
    })
  ,
  'DESCRIPTOR' : _CONTROLIN,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.ControlIn)
  })
_sym_db.RegisterMessage(ControlIn)
_sym_db.RegisterMessage(ControlIn.NotifyComplete)

ControlOut = _reflection.GeneratedProtocolMessageType('ControlOut', (_message.Message,), {

  'ConfirmComplete' : _reflection.GeneratedProtocolMessageType('ConfirmComplete', (_message.Message,), {
    'DESCRIPTOR' : _CONTROLOUT_CONFIRMCOMPLETE,
    '__module__' : 'sdk_tool_service_v2_pb2'
    # @@protoc_insertion_point(class_scope:sdk.ControlOut.ConfirmComplete)
    })
  ,
  'DESCRIPTOR' : _CONTROLOUT,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.ControlOut)
  })
_sym_db.RegisterMessage(ControlOut)
_sym_db.RegisterMessage(ControlOut.ConfirmComplete)

RecordTransferIn = _reflection.GeneratedProtocolMessageType('RecordTransferIn', (_message.Message,), {

  'IncomingRecords' : _reflection.GeneratedProtocolMessageType('IncomingRecords', (_message.Message,), {
    'DESCRIPTOR' : _RECORDTRANSFERIN_INCOMINGRECORDS,
    '__module__' : 'sdk_tool_service_v2_pb2'
    # @@protoc_insertion_point(class_scope:sdk.RecordTransferIn.IncomingRecords)
    })
  ,

  'RecordRequest' : _reflection.GeneratedProtocolMessageType('RecordRequest', (_message.Message,), {
    'DESCRIPTOR' : _RECORDTRANSFERIN_RECORDREQUEST,
    '__module__' : 'sdk_tool_service_v2_pb2'
    # @@protoc_insertion_point(class_scope:sdk.RecordTransferIn.RecordRequest)
    })
  ,
  'DESCRIPTOR' : _RECORDTRANSFERIN,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.RecordTransferIn)
  })
_sym_db.RegisterMessage(RecordTransferIn)
_sym_db.RegisterMessage(RecordTransferIn.IncomingRecords)
_sym_db.RegisterMessage(RecordTransferIn.RecordRequest)

WantRecords = _reflection.GeneratedProtocolMessageType('WantRecords', (_message.Message,), {
  'DESCRIPTOR' : _WANTRECORDS,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.WantRecords)
  })
_sym_db.RegisterMessage(WantRecords)

OutgoingRecords = _reflection.GeneratedProtocolMessageType('OutgoingRecords', (_message.Message,), {
  'DESCRIPTOR' : _OUTGOINGRECORDS,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.OutgoingRecords)
  })
_sym_db.RegisterMessage(OutgoingRecords)

RecordTransferOut = _reflection.GeneratedProtocolMessageType('RecordTransferOut', (_message.Message,), {
  'DESCRIPTOR' : _RECORDTRANSFEROUT,
  '__module__' : 'sdk_tool_service_v2_pb2'
  # @@protoc_insertion_point(class_scope:sdk.RecordTransferOut)
  })
_sym_db.RegisterMessage(RecordTransferOut)



_SDKTOOLV2 = _descriptor.ServiceDescriptor(
  name='SdkToolV2',
  full_name='sdk.SdkToolV2',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1731,
  serialized_end=1859,
  methods=[
  _descriptor.MethodDescriptor(
    name='Control',
    full_name='sdk.SdkToolV2.Control',
    index=0,
    containing_service=None,
    input_type=_CONTROLIN,
    output_type=_CONTROLOUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RecordTransfer',
    full_name='sdk.SdkToolV2.RecordTransfer',
    index=1,
    containing_service=None,
    input_type=_RECORDTRANSFERIN,
    output_type=_RECORDTRANSFEROUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SDKTOOLV2)

DESCRIPTOR.services_by_name['SdkToolV2'] = _SDKTOOLV2

# @@protoc_insertion_point(module_scope)

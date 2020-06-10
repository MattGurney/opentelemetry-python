# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/resource/v1/resource.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='opentelemetry/proto/resource/v1/resource.proto',
  package='opentelemetry.proto.resource.v1',
  syntax='proto3',
  serialized_options=b'\n\"io.opentelemetry.proto.resource.v1B\rResourceProtoP\001Z@github.com/open-telemetry/opentelemetry-proto/gen/go/resource/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.opentelemetry/proto/resource/v1/resource.proto\x12\x1fopentelemetry.proto.resource.v1\x1a*opentelemetry/proto/common/v1/common.proto\"r\n\x08Resource\x12\x44\n\nattributes\x18\x01 \x03(\x0b\x32\x30.opentelemetry.proto.common.v1.AttributeKeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x02 \x01(\rBw\n\"io.opentelemetry.proto.resource.v1B\rResourceProtoP\x01Z@github.com/open-telemetry/opentelemetry-proto/gen/go/resource/v1b\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,])




_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='opentelemetry.proto.resource.v1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='opentelemetry.proto.resource.v1.Resource.attributes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_attributes_count', full_name='opentelemetry.proto.resource.v1.Resource.dropped_attributes_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=127,
  serialized_end=241,
)

_RESOURCE.fields_by_name['attributes'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._ATTRIBUTEKEYVALUE
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'opentelemetry.proto.resource.v1.resource_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.resource.v1.Resource)
  })
_sym_db.RegisterMessage(Resource)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

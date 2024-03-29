# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\" \n\x0eOperationReply\x12\x0e\n\x06result\x18\x01 \x01(\x01\x32:\n\x11\x43\x61lculatorService\x12%\n\x03Sum\x12\x0b.SumRequest\x1a\x0f.OperationReply\"\x00\x62\x06proto3'
)




_SUMREQUEST = _descriptor.Descriptor(
  name='SumRequest',
  full_name='SumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SumRequest.a', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='SumRequest.b', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=20,
  serialized_end=54,
)


_OPERATIONREPLY = _descriptor.Descriptor(
  name='OperationReply',
  full_name='OperationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='OperationReply.result', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=56,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['SumRequest'] = _SUMREQUEST
DESCRIPTOR.message_types_by_name['OperationReply'] = _OPERATIONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SumRequest = _reflection.GeneratedProtocolMessageType('SumRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUMREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:SumRequest)
  })
_sym_db.RegisterMessage(SumRequest)

OperationReply = _reflection.GeneratedProtocolMessageType('OperationReply', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONREPLY,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:OperationReply)
  })
_sym_db.RegisterMessage(OperationReply)



_CALCULATORSERVICE = _descriptor.ServiceDescriptor(
  name='CalculatorService',
  full_name='CalculatorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=90,
  serialized_end=148,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='CalculatorService.Sum',
    index=0,
    containing_service=None,
    input_type=_SUMREQUEST,
    output_type=_OPERATIONREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATORSERVICE)

DESCRIPTOR.services_by_name['CalculatorService'] = _CALCULATORSERVICE

# @@protoc_insertion_point(module_scope)

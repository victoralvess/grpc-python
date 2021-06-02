# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sum = channel.unary_unary(
                '/CalculatorService/Sum',
                request_serializer=calculator__pb2.SumRequest.SerializeToString,
                response_deserializer=calculator__pb2.OperationReply.FromString,
                )


class CalculatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=calculator__pb2.SumRequest.FromString,
                    response_serializer=calculator__pb2.OperationReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CalculatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CalculatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CalculatorService/Sum',
            calculator__pb2.SumRequest.SerializeToString,
            calculator__pb2.OperationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

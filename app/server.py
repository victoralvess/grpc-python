from concurrent import futures
import logging

import grpc

import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServiceServicer):
    def Sum(self, request, context):
        return calculator_pb2.OperationReply(result=request.a + request.b)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server is running on port 50051.')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    main()
import sys
import logging

import grpc

import calculator_pb2
import calculator_pb2_grpc

def main(argv):
    if 3 > len(sys.argv) < 4:
        print('Usage: python client.py <operation> <a> <b>')
        return
    
    if sys.argv[1] not in ['sum']:
        print('%s is not a valid operation.' % (sys.argv[1]))
        return
    
    with grpc.insecure_channel('localhost:50051') as channel:
        a = float(sys.argv[2])
        b = float(sys.argv[3])

        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
        response = stub.Sum(calculator_pb2.SumRequest(a=a, b=b))
        print('%f + %f = %f' % (a, b, response.result))

if __name__ == '__main__':
    logging.basicConfig()
    main(sys.argv)

import greet_pb2_grpc
import greet_pb2
import time
import grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. Unary\n2. Server Streaming\n3. Client Streaming\n 4. Both Streaming")
        rpc_call = input('Which rpc would you call: ')

        if rpc_call == '1':
            hello_request = greet_pb2.HelloRequest(greeting = 'Hello', name = 'StudyApp')
            hello_reply = stub.SayHello(hello_request)
            print('SayHello Response received: ')
            print(hello_reply)

        elif rpc_call == '2':
            print('Not')
            # hello_request = greet_pb2.HelloRequest(greeting = 'Hello', name = 'StudyApp')
            # hello_replies = stub.ParrotSaysHello(hello_request)

            # for hello_reply in hello_replies:
            #     print('ParrotSaysHello Response received: ')
            #     print(hello_reply)

        elif rpc_call == '3':
            print('Not ')
        elif rpc_call == '4':
            print('Not ')


if __name__ == '__main__':
    run()
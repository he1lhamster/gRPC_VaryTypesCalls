import greet_pb2_grpc
import greet_pb2
import time
import grpc


def get_client_stream_requests():
    while True:
        name = input('Please enter name (or nothing to stop): ')

        if name == '':
            break

        hello_request = greet_pb2.HelloRequest(greeting = 'Privet', name = name)
        yield hello_request
        time.sleep(2)

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
            hello_request = greet_pb2.HelloRequest(greeting = 'Bonjour', name = 'StudyApp')
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print('ParrotSaysHello Response received: ')
                print(hello_reply)

        elif rpc_call == '3':
            delayed_reply = stub.ChattyClientSayHello(get_client_stream_requests())
            print('ChattyClientSaysHello Response received: ')
            print(delayed_reply)

        elif rpc_call == '4':
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print('InteractingHello Response received: ')
                print(response)


if __name__ == '__main__':
    run()
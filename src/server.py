"""
from concurrent.futures import ThreadPoolExecutor
import grpc

from proto.helloworld_pb2 import HelloRequest, HelloReply
from proto import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    
    # .proto에서 지정한 메서드를 구현하는데, request, context를 인자로 받는다.
    # 요청하는 데이터를 활용하기 이ㅜ해서는 request.{메시지 형식 이름}으로 호출한다.
    # 응답시에는 메서드 return에 proto buffer 형태로 메시지 형식에 내용을 적어서 반환한다.
    def SayHello(self, request, context):
        return HelloReply(message="Hello, %s!" % request.name)


def serve():
    print("Server start...")
    
    # 서버를 정의할 때, future의 멀티 스레딩을 이용하여 서버 가동
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    
    # 위에서 정의한 서버를 지정
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    # 불안정한 포트 50051로 연결한다.
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()
    
"""
import asyncio
from grpc import aio

from proto.helloworld_pb2 import HelloRequest, HelloReply
from proto import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    
    # .proto에서 지정한 메서드를 구현하는데, request, context를 인자로 받는다.
    # 요청하는 데이터를 활용하기 이ㅜ해서는 request.{메시지 형식 이름}으로 호출한다.
    # 응답시에는 메서드 return에 proto buffer 형태로 메시지 형식에 내용을 적어서 반환한다.
    async def SayHello(self, request, context):
        return HelloReply(message="Hello, %s!" % request.name)


async def serve():
    print("Server start...")
    
    # 서버를 정의할 때, future의 멀티 스레딩을 이용하여 서버 가동
    server = aio.server()
    
    # 위에서 정의한 서버를 지정
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    listen_addr = '[::]:50051'
    
    # 불안정한 포트 50051로 연결한다.
    server.add_insecure_port(listen_addr)
    await server.start()
    await server.wait_for_termination()
    
if __name__ == '__main__':
    asyncio.run(serve())
    
    
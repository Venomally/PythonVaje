from concurrent import futures
import grpc
import pozdrav_pb2 as ts 
import pozdrav_pb2_grpc as rpc

class Server(rpc.ServeServicer):
    def __init__(self):
        self.points = []

    def GetInfo(self, request, context):
        return ts.InfoResponse(message="Hello from the server!")
    def GetAll(self, request, context):
        return ts.AllResponse(points=self.points)
    def sendMore(self,request, context):
        self.points.append(request.point)
        return ts.SendResponse(message="Point received!")

port = 3000
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
rpc.add_ServeServicer_to_server(Server(), server)
server.add_insecure_port(f'[::]:{port}')
server.start()
print(f'Server is running on port {port}...')
print('Press Ctrl+C to stop the server.')
server.wait_for_termination()

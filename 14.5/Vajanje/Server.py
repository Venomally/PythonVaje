from concurrent import futures
import time
import grpc
import pozdrav_pb2
import pozdrav_pb2_grpc

class PozdravService(pozdrav_pb2_grpc.PozdravServisServicer):
    def __init__(self,*arg,**kwargs):
        pass
    def VrniSporocilo(self,request,context):
        print("Prejeto ime: ", request.ime)
        return pozdrav_pb2.Sporocilo(odgovor=f"Pozdravljen, {request.ime}!")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pozdrav_pb2_grpc.add_PozdravServisServicer_to_server(PozdravService(),server)
server.add_insecure_port('[::]:50051')
server.start()
print("Strežnik je zagnan na portu 50051")
server.wait_for_termination()

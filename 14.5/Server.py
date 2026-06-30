import grpc
from concurrent import futures
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class Service(pb2_grpc.Naloga1Servicer): 

    def __init__(self, *args, **kwargs):
        pass

    def NekajDrugega(self, request, context):
        message = request.text
        result = {'text': message.upper()}

        return pb2.Sporocilo(text=message.upper())


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pb2_grpc.add_Naloga1Servicer_to_server(Service(), server)
server.add_insecure_port('[::]:10024')
server.start()
print('Started!')
server.wait_for_termination()

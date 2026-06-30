import grpc
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = pb2_grpc.GreeterStub(channel)
 
asd = pb2.Sporocilo()
asd.text = "Hello, gRPC!"
asd.text


response = stub.NekajDrugega(asd)
print(response)

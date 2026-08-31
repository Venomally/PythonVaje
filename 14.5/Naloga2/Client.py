import threading

import grpc

import ts_pb2 as ts
import ts_pb2_grpc as rpc

address = 'localhost'
port = 30000


class Client:

    def __init__(self):
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.Serve(channel)

    def put_point(self, value):
        p = ts.Point()
        p.value = value
        self.conn.SendOne(p)

    def get_point(self, index):
        point = self.conn.GetOne(ts.PointIndex(index=index))
        print(point.value)
    
    def get_all_points(self):
        all_points = self.conn.GetAll(ts.Empty())
        for point in all_points:
            print(point.value)

    def iterator(self, point_objects):
        for point in point_objects:
            yield point
    def put_stream_point(self, values):
        point_objects = [ts.Point(value = val) for val in values]
        self.conn.SendMore(self.iterator(point_objects))


c = Client()
c.put_point(1.2)
c.put_point(1.2)
c.put_point(2.2)

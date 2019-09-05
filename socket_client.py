import json
import pickle
import socket

class SocketClient:

    def __init__(self):
        self.HOST = None
        self.PORT = None
        self.socket = None

    def start(self, host, port):
        if not host or not port:
            return
        self.HOST = host
        self.PORT = port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            while True:
                array = input()
                data = list(map(int, array.split(' ')))
                data_array = json.dumps({"array": data})
                s.send(data_array.encode())


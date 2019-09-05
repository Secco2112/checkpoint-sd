import json
import socket
import pickle

class CheckpointMaster:
    def __init__(self):
        self.host = None
        self.port = None
        self.unordered_array = None

    def config(self, server_config):
        self.host = server_config['host']
        self.port = server_config['port']
        return self

    def validate(self):
        if not self.host or not self.port:
            raise Exception("Host and port are required")

    def start(self):
        self.validate()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        data = json.loads(data.decode())
                        self.unordered_array = data
                        print(self.unordered_array)
                conn.close()

from socket_master import CheckpointMaster

checkpoint_master = CheckpointMaster()
checkpoint_master.config({
    "host": "192.168.0.15",
    "port": 65432
}).start()

import socket
import time
import asyncio
import websockets
import socketio

class NetworkTester:
    def __init__(self, host='localhost', tcp_port=10001, ws_port=10002, sio_port=10003):
        self.host = host
        self.tcp_port = tcp_port
        self.ws_port = ws_port
        self.sio_port = sio_port

    async def tcp_test(self, data_size, message_count):
        """ Test TCP socket performance. """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.host, self.tcp_port))
            data = b'x' * data_size
            start_time = time.time()
            for _ in range(message_count):
                client.sendall(data)
                response = client.recv(data_size)
            end_time = time.time()
            print(f"TCP Test: {message_count} messages of {data_size} bytes took {end_time - start_time} seconds")

    async def websocket_test(self, data_size, message_count):
        """ Test WebSocket performance. """
        uri = f"ws://{self.host}:{self.ws_port}"
        async with websockets.connect(uri) as websocket:
            data = b'x' * data_size
            start_time = time.time()
            for _ in range(message_count):
                await websocket.send(data)
                response = await websocket.recv()
            end_time = time.time()
            print(f"WebSocket Test: {message_count} messages of {data_size} bytes took {end_time - start_time} seconds")

    async def socketio_test(self, data_size, message_count):
        """ Test Socket.IO performance. """
        sio = socketio.AsyncClient()
        await sio.connect(f"http://{self.host}:{self.sio_port}")
        data = b'x' * data_size
        start_time = time.time()
        for _ in range(message_count):
            await sio.emit('message', data)
            await sio.call('message', data)
        end_time = time.time()
        print(f"Socket.IO Test: {message_count} messages of {data_size} bytes took {end_time - start_time} seconds")
        await sio.disconnect()

    async def run_all_tests(self):
        """ Run all tests. """
        data_size = 1024  # Size of each message (1 KB)
        message_count = 1000  # Number of messages
        await asyncio.gather(
            self.tcp_test(data_size, message_count),
            self.websocket_test(data_size, message_count),
            self.socketio_test(data_size, message_count)
        )

# Example of using the class
if __name__ == "__main__":
    tester = NetworkTester()
    asyncio.run(tester.run_all_tests())

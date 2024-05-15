import asyncio
import time
import socket
import websockets
import socketio

async def tcp_latency_test(host, port, data_size, message_count):
    total_time = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        data = b'x' * data_size
        for _ in range(message_count):
            start_time = time.time()
            client.sendall(data)
            response = client.recv(data_size)
            total_time += time.time() - start_time
    print(f"TCP Latency Test: {total_time} seconds")

async def websocket_latency_test(host, port, data_size, message_count):
    total_time = 0
    uri = f"ws://{host}:{port}"
    async with websockets.connect(uri) as websocket:
        data = b'x' * data_size
        for _ in range(message_count):
            start_time = time.time()
            await websocket.send(data)
            response = await websocket.recv()
            total_time += time.time() - start_time
    print(f"WebSocket Latency Test: {total_time} seconds")

async def socketio_latency_test(host, port, data_size, message_count):
    total_time = 0
    sio = socketio.AsyncClient()
    await sio.connect(f"http://{host}:{port}")
    data = b'x' * data_size
    for _ in range(message_count):
        start_time = time.time()
        await sio.emit('message', data)
        await sio.call('message', data)
        total_time += time.time() - start_time
    await sio.disconnect()
    print(f"Socket.IO Latency Test: {total_time} seconds")

async def run_tests(host='85.0.76.241'):
    data_size = 1024  # Size of each message (1 KB)
    message_count = 10000  # Number of messages
    await asyncio.gather(
        tcp_latency_test(host, 10001, data_size, message_count),
        websocket_latency_test(host, 10002, data_size, message_count),
        socketio_latency_test(host, 10003, data_size, message_count)
    )

if __name__ == "__main__":
    import sys
    host = sys.argv[1] if len(sys.argv) > 1 else '85.0.76.241'
    asyncio.run(run_tests(host))

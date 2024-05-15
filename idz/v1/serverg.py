import asyncio
import socket
import websockets
import socketio
from uvicorn import Config, Server

class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        server_socket.setblocking(False)
        print(f'Socket server listening on {self.host}:{self.port}')

        while True:
            conn, addr = await asyncio.get_event_loop().sock_accept(server_socket)
            asyncio.get_event_loop().create_task(self.handle_client(conn, addr))

    async def handle_client(self, conn, addr):
        with conn:
            while True:
                data = await asyncio.get_event_loop().sock_recv(conn, 1024)
                if not data:
                    break
                await asyncio.sleep(0.01)
                await asyncio.get_event_loop().sock_sendall(conn, data)

class WebSocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def start(self):
        async def echo(websocket, path):
            async for message in websocket:
                await asyncio.sleep(0.01)
                await websocket.send(message)

        server = await websockets.serve(echo, self.host, self.port)
        print(f'WebSocket server listening on {self.host}:{self.port}')
        await server.wait_closed()

class SocketIOServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sio = socketio.AsyncServer(async_mode='asgi')
        self.app = socketio.ASGIApp(self.sio)

        @self.sio.event
        async def connect(sid, environ):
            print(f'{sid} connected')

        @self.sio.event
        async def disconnect(sid):
            print(f'{sid} disconnected')

        @self.sio.event
        async def message(sid, data):
            await asyncio.sleep(0.01)
            await self.sio.emit('response', data, to=sid)

    async def start(self):
        config = Config(self.app, host=self.host, port=self.port, loop="asyncio")
        server = Server(config)
        print(f'Socket.IO server listening on {self.host}:{self.port}')
        await server.serve()

async def main(host='localhost'):
    socket_server = SocketServer(host, 10001)
    websocket_server = WebSocketServer(host, 10002)
    socketio_server = SocketIOServer(host, 10003)

    await asyncio.gather(
        socket_server.start(),
        websocket_server.start(),
        socketio_server.start(),
    )

if __name__ == "__main__":
    asyncio.run(main())

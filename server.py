import asyncio
import websockets
import threading

# Data handling
command_queue = []

def getMovements():

    temp_commands = []

    for commands in command_queue:
        temp_commands.extend([i for i in commands.split(";") if i])

    command_queue.clear()

    return temp_commands

# Server
portnum = 5555

def websocket_thread():
    print("Websocket listening on: " + str(portnum))
    async def reciever(websocket, path):
        print("Websocket connected on: " + str(portnum))
        data = await websocket.recv()
        command_queue.append(data)
        print(f"< {data} total queue {command_queue}")

    start_server = websockets.serve(reciever, port=portnum)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    ws = threading.Thread(target=websocket_thread)
    ws.start()
import asyncio
import websockets

# Data handling
command_queue = ["rotatehead(forward);turn(left);move(forward);turn(left);", "rotatehead(forward);turn(left);move(forward);turn(left);"]

def getMovements():

    temp_commands = []

    for commands in command_queue:
        temp_commands.extend([i for i in commands.split(";") if i])

    return temp_commands

print(getMovements())

# Server
portnum = 5555

print("Websocket listening on: " + str(portnum))

async def reciever(websocket, path):
    print("Websocket connected on: " + str(portnum))
    data = await websocket.recv()
    command_queue.append(data)
    print(f"< {data} total queue {command_queue}")

# start_server = websockets.serve(reciever, port=portnum)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
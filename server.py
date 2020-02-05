import asyncio
import websockets

portnum = 5555

print("Websocket listening on: " + str(portnum))

async def reciever(websocket, path):
    print("Websocket connected on: " + str(portnum))
    data = await websocket.recv()
    print(f"< {data}")

start_server = websockets.serve(reciever, port=portnum)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
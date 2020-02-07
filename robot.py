import servocontrols
import server, threading, time

# robot clock

# relay commands from server to servocontroller
def relay_commands():
    moves = server.getMovements()

    if (len(moves) > 0):
        print("[robot]: got new commands")
        servocontrols.add_commands(moves)

# robot loop

def robot_clock():
    print("[robot_clock]: starting...")
    while(1):
        time.sleep(10)
        relay_commands()


rl = threading.Thread(target=robot_clock)
rl.start()

# start server. this locks up execution.
server.websocket_thread()
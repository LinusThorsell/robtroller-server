# Initialize servos
import threading, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def angle_to_pwm(angle):
    # Figure out how 'wide' each range is
    leftSpan = 180 - 0
    rightSpan = 10.5 - 3

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(angle - 0) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return 3 + (valueScaled * rightSpan)

class Servo:
    "Class used to keep track of the servos"

    def __init__(self, name, pin, init_value):
        self.name = name
        self.pin = pin
        self.position = init_value

        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(7.5)

    def __repr__(self):
        return "[NAME]: " + self.name + " [PIN]: " + str(self.pin) + " [POSITION]: " + str(self.position)

    def __str__(self):
        return "[NAME]: " + self.name + " [PIN]: " + str(self.pin) + " [POSITION]: " + str(self.position)

    def setPos(self, pos):
        self.position = pos

    def addAngle(self, angle):
        self.position += angle
    def delAngle(self, angle):
        self.position -= angle

    def update_location(self):
        self.pwm.ChangeDutyCycle(angle_to_pwm(self.position))

    def stop_pwm(self):
        self.pwm.ChangeDutyCycle(0)

    pass


servos = [
    Servo("LEFT_LEG_1", 3, 100),
    Servo("LEFT_LEG_2", 5, 100),
    Servo("LEFT_LEG_3", 7, 90),
    Servo("LEFT_LEG_4", 11, 90),
    Servo("RIGHT_LEG_1", 13, 100),
    Servo("RIGHT_LEG_2", 15, 100),
    Servo("RIGHT_LEG_3", 19, 90),
    Servo("RIGHT_LEG_4", 21, 90),
]

print(servos[0])

def update_servos():
    for servo in servos:
        servo.update_location()

def sleep_servos():
    for servo in servos:
        servo.stop_pwm()

update_servos()


command_queue = ["move(forward)"]

def add_commands(commands):
    command_queue.extend(commands)

def command_worker():

    def run_next():
        print(command_queue[0])
        do_command(command_queue[0])
        command_queue.pop(0)

    print("[command_worker]: starting...")
    while(1):
        time.sleep(5)
        if (len(command_queue) > 0):
            print("[command_worker]: running next command...")
            run_next()

t = threading.Thread(target=command_worker)
t.start()


def move_forward():
    print("moving forward now")
    # move forward
    servos[0].setPos(30)
    servos[1].setPos(30)
    servos[2].setPos(150)
    servos[3].setPos(150)

    servos[4].setPos(80)
    servos[4].setPos(80)
    servos[4].setPos(90)
    servos[4].setPos(90)

    update_servos()
    time.sleep(0.5)
    sleep_servos()

    servos[0].setPos(30)
    servos[1].setPos(30)
    servos[2].setPos(150)
    servos[3].setPos(150)

    servos[4].setPos(60)
    servos[4].setPos(60)
    servos[4].setPos(90)
    servos[4].setPos(90)

    update_servos()
    time.sleep(0.5)
    sleep_servos()

    
    servos[0].setPos(80)
    servos[1].setPos(80)
    servos[2].setPos(90)
    servos[3].setPos(90)

    servos[4].setPos(80)
    servos[4].setPos(80)
    servos[4].setPos(90)
    servos[4].setPos(90)

    update_servos()
    time.sleep(0.5)
    sleep_servos()


def do_command(command):
    command = command.lower()
    if "move" in command:
        if "forward" in command:
            print("move forward")
            move_forward()
        if "backwards" in command:
            print("move backwards")
    if "run" in command:
        if "forward" in command:
            print("run forward")
        if "backwards" in command:
            print("run backwards")
    if "spin" in command:
        if "left" in command:
            print("spin left")
        if "right" in command:
            print("spin right")
    if "head" in command:
        if "right" in command:
            print("head look right")
        if "left" in command:
            print("head look left")
        if "center" in command:
            print("head look straight")
    if "debug" in command:
        print("debug command received")
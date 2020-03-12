# Initialize servos
import threading, time
import RPi.GPIO as GPIO

servoPIN1 = 3
servoPIN2 = 5
servoPIN3 = 7

servoPIN4 = 11
servoPIN5 = 13
servoPIN6 = 15

servoPIN7 = 19
servoPIN8 = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(servoPIN3, GPIO.OUT)

GPIO.setup(servoPIN4, GPIO.OUT)
GPIO.setup(servoPIN5, GPIO.OUT)
GPIO.setup(servoPIN6, GPIO.OUT)

GPIO.setup(servoPIN7, GPIO.OUT)
GPIO.setup(servoPIN8, GPIO.OUT)

p1 = GPIO.PWM(servoPIN1, 50)
p1.start(0)
p2 = GPIO.PWM(servoPIN2, 50)
p2.start(0)
p3 = GPIO.PWM(servoPIN3, 50)
p3.start(0)

p4 = GPIO.PWM(servoPIN4, 50)
p4.start(0)
p5 = GPIO.PWM(servoPIN5, 50)
p5.start(0)
p6 = GPIO.PWM(servoPIN6, 50)
p6.start(0)

p7 = GPIO.PWM(servoPIN7, 50)
p7.start(0)
p8 = GPIO.PWM(servoPIN8, 50)
p8.start(0)


# setup inital positions
p1.ChangeDutyCycle(8.5)
p2.ChangeDutyCycle(8.5)
p3.ChangeDutyCycle(6.75)
p4.ChangeDutyCycle(6.75)
    
p5.ChangeDutyCycle(8.5)
p6.ChangeDutyCycle(8.5)
p7.ChangeDutyCycle(6.75)
p8.ChangeDutyCycle(6.75)

time.sleep(1)



def servos_sleep():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    p3.ChangeDutyCycle(0)
    p4.ChangeDutyCycle(0)
    
    p5.ChangeDutyCycle(0)
    p6.ChangeDutyCycle(0)
    p7.ChangeDutyCycle(0)
    p8.ChangeDutyCycle(0)

servos_sleep()


command_queue = []

def add_commands(commands):
    command_queue.extend(commands)

def command_worker():

    def run_next():
        print(command_queue[0])
        do_command(command_queue[0])
        command_queue.pop(0)

    print("[command_worker]: starting...")
    while(1):
        time.sleep(1)
        if (len(command_queue) > 0):
            print("[command_worker]: running next command...")
            run_next()

t = threading.Thread(target=command_worker)
t.start()


walkstage = 0.15
def walk_forward():
    # move forward
    p1.ChangeDutyCycle(8.5)
    p2.ChangeDutyCycle(8.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)
    
    p5.ChangeDutyCycle(8.5)
    p6.ChangeDutyCycle(8.5)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(3)
    p2.ChangeDutyCycle(3)
    p3.ChangeDutyCycle(10)
    p4.ChangeDutyCycle(10)

    p5.ChangeDutyCycle(6)
    p6.ChangeDutyCycle(6)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(3)
    p2.ChangeDutyCycle(3)
    p3.ChangeDutyCycle(10)
    p4.ChangeDutyCycle(10)

    p5.ChangeDutyCycle(4)
    p6.ChangeDutyCycle(4)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(5)
    p2.ChangeDutyCycle(5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(5)
    p6.ChangeDutyCycle(5)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)



    p1.ChangeDutyCycle(7.5)
    p2.ChangeDutyCycle(7.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(10.5)
    p6.ChangeDutyCycle(10.5)
    p7.ChangeDutyCycle(3.5)
    p8.ChangeDutyCycle(3.5)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(9.5)
    p2.ChangeDutyCycle(9.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(10.5)
    p6.ChangeDutyCycle(10.5)
    p7.ChangeDutyCycle(3.5)
    p8.ChangeDutyCycle(3.5)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(8.5)
    p2.ChangeDutyCycle(8.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(8.5)
    p6.ChangeDutyCycle(8.5)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)

    servos_sleep()

def walk_backwards():
    # move backward
    p1.ChangeDutyCycle(9.5)
    p2.ChangeDutyCycle(9.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(10.5)
    p6.ChangeDutyCycle(10.5)
    p7.ChangeDutyCycle(3.5)
    p8.ChangeDutyCycle(3.5)

    time.sleep(walkstage)

    
    p1.ChangeDutyCycle(7.5)
    p2.ChangeDutyCycle(7.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(10.5)
    p6.ChangeDutyCycle(10.5)
    p7.ChangeDutyCycle(3.5)
    p8.ChangeDutyCycle(3.5)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(5)
    p2.ChangeDutyCycle(5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)

    p5.ChangeDutyCycle(5)
    p6.ChangeDutyCycle(5)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(3)
    p2.ChangeDutyCycle(3)
    p3.ChangeDutyCycle(10)
    p4.ChangeDutyCycle(10)

    p5.ChangeDutyCycle(4)
    p6.ChangeDutyCycle(4)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)

    
    p1.ChangeDutyCycle(3)
    p2.ChangeDutyCycle(3)
    p3.ChangeDutyCycle(10)
    p4.ChangeDutyCycle(10)

    p5.ChangeDutyCycle(6)
    p6.ChangeDutyCycle(6)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    p1.ChangeDutyCycle(8.5)
    p2.ChangeDutyCycle(8.5)
    p3.ChangeDutyCycle(6.75)
    p4.ChangeDutyCycle(6.75)
    
    p5.ChangeDutyCycle(8.5)
    p6.ChangeDutyCycle(8.5)
    p7.ChangeDutyCycle(6.75)
    p8.ChangeDutyCycle(6.75)

    time.sleep(walkstage)


    servos_sleep()


def do_command(command):
    command = command.lower()
    if "walk" in command:
        if "forward" in command:
            print("walk forward")
            walk_forward()
        if "backwards" in command:
            print("move backwards")
            walk_backwards()
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
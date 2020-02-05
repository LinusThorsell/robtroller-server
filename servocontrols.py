# Initialize servos

class Servo:
    "Class used to keep track of the servos"

    def __init__(self, name, pin, init_value):
        self.name = name
        self.pin = pin
        self.position = init_value

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

    pass


servos = [
    Servo("HEAD", 1, 90),
    Servo("LEFT_UPPER_ARM", 2, 90),
    Servo("LEFT_LOWER_ARM", 3, 60),
    Servo("LEFT_HAND", 4, 60),
]

print(servos[0])
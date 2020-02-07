# this is a hack to allow development on windows machine
BOARD = 1
OUT = 1
IN = 1

def setmode(a):
   pass
def setup(a, b):
   pass
def output(a, b):
   pass
def cleanup():
   pass
def setwarnings(flag):
   pass
def PWM(flag1, flag2):
    class hack(object):
        def start(self):
            pass
        def ChangeDutyCycle(self):
            pass
        pass
    return hack
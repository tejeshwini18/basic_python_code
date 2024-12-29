import time
from gpiozero import Motor
from gpiozero import DistanceSensor
from adafruit_servokit import ServoKit

# Constants
TRIG_PIN = "A0"
ECHO_PIN = "A1"
MAX_DISTANCE = 200
MAX_SPEED = 1.0  # Speed in range [0, 1]
SPEED_STEP = 0.1

# Initialize motors
motor1 = Motor(forward=17, backward=18)  # Replace with your GPIO pins
motor2 = Motor(forward=22, backward=23)
motor3 = Motor(forward=24, backward=25)
motor4 = Motor(forward=5, backward=6)

# Initialize ultrasonic sensor
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN, max_distance=MAX_DISTANCE)

# Initialize servo
kit = ServoKit(channels=16)
servo = kit.servo[0]
servo.angle = 115  # Neutral position
time.sleep(2)

# Global variables
goes_forward = False
distance = 100


def read_ping():
    """Reads the distance from the ultrasonic sensor."""
    time.sleep(0.07)
    cm = sensor.distance * 100  # Convert to cm
    return cm if cm > 0 else 250


def move_stop():
    """Stops all motors."""
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()


def move_forward():
    """Moves all motors forward."""
    global goes_forward
    if not goes_forward:
        goes_forward = True
        motor1.forward()
        motor2.forward()
        motor3.forward()
        motor4.forward()

        for speed in range(0, int(MAX_SPEED * 100), int(SPEED_STEP * 100)):
            motor1.forward(speed / 100)
            motor2.forward(speed / 100)
            motor3.forward(speed / 100)
            motor4.forward(speed / 100)
            time.sleep(0.05)


def move_backward():
    """Moves all motors backward."""
    global goes_forward
    goes_forward = False
    motor1.backward()
    motor2.backward()
    motor3.backward()
    motor4.backward()

    for speed in range(0, int(MAX_SPEED * 100), int(SPEED_STEP * 100)):
        motor1.backward(speed / 100)
        motor2.backward(speed / 100)
        motor3.backward(speed / 100)
        motor4.backward(speed / 100)
        time.sleep(0.05)


def turn_right():
    """Turns the robot to the right."""
    motor1.forward()
    motor2.forward()
    motor3.backward()
    motor4.backward()
    time.sleep(0.5)
    move_stop()


def turn_left():
    """Turns the robot to the left."""
    motor1.backward()
    motor2.backward()
    motor3.forward()
    motor4.forward()
    time.sleep(0.5)
    move_stop()


def look_right():
    """Moves the servo to look right and returns the distance."""
    servo.angle = 50
    time.sleep(0.5)
    distance = read_ping()
    time.sleep(0.1)
    servo.angle = 115
    return distance


def look_left():
    """Moves the servo to look left and returns the distance."""
    servo.angle = 170
    time.sleep(0.5)
    distance = read_ping()
    time.sleep(0.1)
    servo.angle = 115
    return distance


# Setup routine
distance = read_ping()
time.sleep(0.1)

# Main loop
try:
    while True:
        time.sleep(0.04)
        if distance <= 15:
            move_stop()
            time.sleep(0.1)
            move_backward()
            time.sleep(0.3)
            move_stop()
            time.sleep(0.2)
            distance_right = look_right()
            time.sleep(0.2)
            distance_left = look_left()
            time.sleep(0.2)

            if distance_right >= distance_left:
                turn_right()
            else:
                turn_left()

            move_stop()
        else:
            move_forward()

        distance = read_ping()

except KeyboardInterrupt:
    move_stop()
    print("Program stopped.")

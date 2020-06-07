from gpiozero import Button
import math

wind_speed_sensor = Button(5)
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin" + str(wind_count))

wind_speed_sensor.when_pressed = spin

radius_cm = 9.0
wind_interval = 5
wind_count = 17

circumference_cm = (2 * math.pi) * radius_cm
rotations = count / 2.0
dist_cm = circumference_cm * rotations
speed = dist_cm / wind_interval

print(speed)

def reset_wind():
    global wind_count
    wind_count = 0
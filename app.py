from sense_hat import SenseHat
import time, threading

sense = SenseHat()
sense.set_imu_config(True, True, True)

THRESHOLD = 1.0

def leds_green():
    green = [0, 255, 0]
    all_green = []
    for i in range(64):
        all_green.append(green)
    sense.set_pixels(all_green)


def leds_red():
    red = [255, 0, 0]
    all_red = []
    for i in range(64):
        all_green.append(red)
    sense.set_pixels(all_red)


def set_in_use():
    leds_green()


def set_not_in_use():
    timer_started = False
    leds_red()


tof_in_use = Timer(30.0, set_not_in_use)
timer_started = False


new_orientation = sense.get_orientation_degrees()
dp = new_orientation['pitch'] - old_orientaion['pitch']
dr = new_orientation['roll'] - old_orientaion['roll']
dy = new_orientation['yaw'] - old_orientaion['yaw']
new_sum_d = dp + dr + dy

old_orientation = new_orientation
old_sum_d = new_sum_d


while True:
    new_orientation = sense.get_orientation_degrees()
    dp = new_orientation['pitch'] - old_orientaion['pitch']
    dr = new_orientation['roll'] - old_orientaion['roll']
    dy = new_orientation['yaw'] - old_orientaion['yaw']
    new_sum_d = dp + dr + dy

    pos_diff = new_sum_d - old_sum_d

    old_orientation = new_orientation
    old_sum_d = new_sum_d

    if pos_diff > TRESHOLD:
        tof_in_use.cancel()
        set_in_use()
    else:
        if timer_started = False:
            tof_in_use.start()
            timer_started = True


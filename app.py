from sense_hat import SenseHat
import time 

sense = SenseHat()
sense.set_imu_config(True, True, True)
pause = 0.2
counter_wait = 5            # wartezeit bevor auf grün gestellt wird
counter_threshold = counter_wait / pause
movement_threshold = 5      # empfindlichkeit des sensors

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
        all_red.append(red)
    sense.set_pixels(all_red)


old_orientation = {'pitch':0, 'roll':0, 'yaw':0}
old_sum_d = 0
in_motion = False
counter_value = 0

while True:
    new_orientation = sense.get_orientation_degrees()
    dp = new_orientation['pitch'] - old_orientation['pitch']
    dr = new_orientation['roll'] - old_orientation['roll']
    dy = new_orientation['yaw'] - old_orientation['yaw']
    old_orientation = new_orientation

    new_sum_d = abs(dp) + abs(dr) + abs(dy)

    pos_diff = new_sum_d - old_sum_d
    old_sum_d = new_sum_d

    if abs(pos_diff) > movement_threshold:                    # In Bewegung
        counter_value = 0
        if in_motion == False:                  # und vorher nicht in bewegung
            in_motion = True                      # auf in_bewegung setzen
    else:                                     # nicht in bewegung
        counter_value += 1                  
        if counter_value > counter_threshold:
            in_motion = False
            counter_value = 0
     
    
    print('pos_diff ' + str(pos_diff) + '\t\tnew_sum_d' + str(new_sum_d) + '\t\t\tin_motion ' + str(in_motion) + '\t\tcounter ' + str(counter_value))
    # \t\t\tnot_in_use_counter' + str(not_in_use_counter) +
    
    if in_motion == True:
        leds_red()
    else:
        leds_green()
        
    time.sleep(0.2)
   



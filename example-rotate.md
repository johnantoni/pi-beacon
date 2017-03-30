# servo control

controlling the servo is done by the pigpiod daemon, instructions in the setup.md file

# how to wire

for the example we're going to use gpio pin 2

the servo we have has three pins

red / orange / brown

red = dc 5v
orange = gpio digital pin 2
brown = earth

also check the photos in photos/wiring

## rotate.py

here is an example which turns the servo left, then right

    import time
    import pigpio

    # set which digital pin will send the turn signal to the servo
    LED_PIN = 2

    # connect to pigpiod daemon
    pi = pigpio.pi()

    # setup pin as an output
    pi.set_mode(LED_PIN, pigpio.OUTPUT)

    # turn left by 90 degrees
    pi.set_servo_pulsewidth(LED_PIN, 500)

    # stop
    time.sleep(1)

    # turn right 180 degrees
    pi.set_servo_pulsewidth(LED_PIN, 2500)

    # stop
    time.sleep(1)

    # cleanup
    pi.set_mode(LED_PIN, pigpio.INPUT)
    # disconnect
    pi.stop()

you'll find the code in rotate.py

## run

you can run the code by:

    sudo python rotate.py

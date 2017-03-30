# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import bluetooth._bluetooth as bluez

# setup servo
import time
import pigpio
LED_PIN = 2
#connect to pigpiod daemon
pi = pigpio.pi()
# setup pin as an output
pi.set_mode(LED_PIN, pigpio.OUTPUT)


def moveservo():
	# use a flag so we only move the servo left/right once
	pi.set_servo_pulsewidth(LED_PIN, 500)
	time.sleep(1)
	pi.set_servo_pulsewidth(LED_PIN, 2500)
	time.sleep(1)
	#cleanup
	pi.set_mode(LED_PIN, pigpio.INPUT)
	#disconnect
	pi.stop()


dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

# listen for beacons, returning if we see the beacon
# interference is how far or near the beacon is, -62 = near, -90 = far
# here if interference is greater than or equal to -62 (near the pi) the servo will move
# were using the flag variable, so once we find the beacon we move the servo and set the
# flag to true, making sure we won't turn the servo again

flag = False

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
        if '0112233445566778899aabbccddeeff0' in beacon:
            print "found feather beacon"
			interference = beacon[-3:]
            print "interference " + interference
				if flag == False and int(interference)>=-62:
					flag = True
					moveservo()

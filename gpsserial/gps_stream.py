"""Pulls live Serial Stream"""

import serial

ser = serial.Serial('/dev/tty.Qstarz818XT-SPPslave', 19200, timeout=1)
for i in range(1,10):
    line = (ser.readline())  # read a '\n' terminated line
    data = line.split(',')
    if len(data) == 15:
        lat = data[2]
        lat_dir = data[3]
        long = data[4]
        long_dir = data[5]
        print "lat: {0} {1} long: {2} {3}".format(lat, lat_dir, long, long_dir)
ser.close()
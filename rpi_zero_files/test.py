#!/usr/bin/python
# -*- coding: utf-8 -*-
# this file is executed automatically at startup
import smbus  
import math
import os
import time
import socket
import sys
from datetime import datetime

clear = lambda: os.system('clear')
# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
def read_byte(adr):
      return bus.read_byte_data(address, adr)
 
def read_word(adr):
      high = bus.read_byte_data(address, adr)
      low = bus.read_byte_data(address, adr+1)
      val = (high << 8) + low
      return val
 
def read_word_2c(adr):
      val = read_word(adr)
      if (val >= 0x8000):
          return -((65535 - val) + 1)
      else:
          return val
 
def dist(a,b):
      return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
      radians = math.atan2(x, dist(y,z))
      return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
      radians = math.atan2(y, dist(x,z))
      return math.degrees(radians)

bus = smbus.SMBus(1)
#bus = smbus.SMBus(0) A SECONDA DELLA SCHEDA
address = 0x68       # A seconda dell'indirizzo trovato precedentamente
 
# Avviamo il chip MPU6050, in questo punto si può avviare un loop 

filename = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
while 1==1:
      bus.write_byte_data(address, power_mgmt_1, 0)
      clear()
      print "gyro data"
      print "---------"
      
      gyro_xout = read_word_2c(0x43)
      gyro_yout = read_word_2c(0x45)
      gyro_zout = read_word_2c(0x47)
      
      print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
      print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
      print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
      
      print ""
      print "accelerometer data"
      print "------------------"
      
      accel_xout = read_word_2c(0x3b)
      accel_yout = read_word_2c(0x3d)
      accel_zout = read_word_2c(0x3f)
      accel_xout_scaled = accel_xout / 16384.0
      accel_yout_scaled = accel_yout / 16384.0
      accel_zout_scaled = accel_zout / 16384.0
      
      print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
      print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
      print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

      xRot = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
      yRot = get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
      print "x rotation: " , xRot
      print "y rotation: " , yRot
      
      f = open("/home/pi/rilevazioni/"+filename+".txt", "a")
      f.write(str(xRot)+";"+str(yRot)+";"+str(time.time())+";\n")
      f.close()
      time.sleep(0.2)

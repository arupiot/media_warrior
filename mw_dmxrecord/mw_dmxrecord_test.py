#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "127.0.0.1"
PORT = 4223

debug = True
verbose = True
reading_interval = 1.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dmx import BrickletDMX

from time import sleep
from os.path import join, splitext
from os import listdir
import math, time, datetime
from numpy import array, zeros, array_equal

tfIDs = [
]

tfConnect = True

prevFrame = zeros(512)

if tfConnect:
    tfIDs = []

deviceIdentifiersList = [
[11, "DC Brick",""],
[13, "Master Brick",""],
[14, "Servo Brick",""],
[15, "Stepper Brick",""],
[16, "IMU Brick","sensor",["get_all_data"],[""]],
[17, "RED Brick",""],
[18, "IMU Brick 2.0","sensor",["get_all_data"],[""]],
[19, "Silent Stepper Brick",""],
[21, "Ambient Light Bricklet","sensor",["get_illuminance"],["lux"]],
[23, "Current12 Bricklet","sensor"],
[24, "Current25 Bricklet","sensor"],
[25, "Distance IR Bricklet","sensor"],
[26, "Dual Relay Bricklet","actuator"],
[27, "Humidity Bricklet","sensor",["get_humidity"],["%RH"]],
[28, "IO-16 Bricklet","sensor"],
[29, "IO-4 Bricklet","sensor"],
[210, "Joystick Bricklet","sensor"],
[211, "LCD 16x2 Bricklet","actuator"],
[212, "LCD 20x4 Bricklet","actuator"],
[213, "Linear Poti Bricklet","sensor"],
[214, "Piezo Buzzer Bricklet","actuator"],
[215, "Rotary Poti Bricklet","sensor"],
[216, "Temperature Bricklet","sensor",["get_temperature"],["ºC"]],
[217, "Temperature IR Bricklet","sensor"],
[218, "Voltage Bricklet","sensor"],
[219, "Analog In Bricklet","sensor"],
[220, "Analog Out Bricklet","actuator"],
[221, "Barometer Bricklet","sensor"],
[222, "GPS Bricklet","sensor"],
[223, "Industrial Digital In 4 Bricklet","sensor"],
[224, "Industrial Digital Out 4 Bricklet","actuator"],
[225, "Industrial Quad Relay Bricklet","actuator"],
[226, "PTC Bricklet","sensor"],
[227, "Voltage/Current Bricklet","sensor"],
[228, "Industrial Dual 0-20mA Bricklet",""],
[229, "Distance US Bricklet","sensor"],
[230, "Dual Button Bricklet","sensor"],
[231, "LED Strip Bricklet","actuator"],
[232, "Moisture Bricklet","sensor"],
[233, "Motion Detector Bricklet","sensor"],
[234, "Multi Touch Bricklet","sensor"],
[235, "Remote Switch Bricklet","sensor"],
[236, "Rotary Encoder Bricklet","sensor"],
[237, "Segment Display 4x7 Bricklet","actuator"],
[238, "Sound Intensity Bricklet","sensor", ["get_intensity"],["dB"]],
[239, "Tilt Bricklet","sensor"],
[240, "Hall Effect Bricklet","sensor"],
[241, "Line Bricklet","sensor"],
[242, "Piezo Speaker Bricklet","actuator"],
[243, "Color Bricklet","sensor"],
[244, "Solid State Relay Bricklet","actuator"],
[245, "Heart Rate Bricklet","sensor"],
[246, "NFC/RFID Bricklet","sensor"],
[249, "Industrial Dual Analog In Bricklet","sensor"],
[250, "Accelerometer Bricklet","sensor"],
[251, "Analog In Bricklet 2.0","sensor"],
[252, "Gas Detector Bricklet","sensor"],
[253, "Load Cell Bricklet","sensor"],
[254, "RS232 Bricklet",""],
[255, "Laser Range Finder Bricklet","sensor"],
[256, "Analog Out Bricklet 2.0","actuator"],
[257, "AC Current Bricklet",""],
[258, "Industrial Analog Out Bricklet",""],
[259, "Ambient Light Bricklet 2.0","",["get_illuminance"],["lux"]],
[260, "Dust Detector Bricklet","sensor"],
[261, "Ozone Bricklet","sensor"],
[262, "CO2 Bricklet","sensor"],
[263, "OLED 128x64 Bricklet","actuator"],
[264, "OLED 64x48 Bricklet","actuator"],
[265, "UV Light Bricklet","sensor"],
[266, "Thermocouple Bricklet","sensor"],
[267, "Motorized Linear Poti Bricklet","sensor"],
[268, "Real-Time Clock Bricklet",""],
[269, "Pressure Bricklet","sensor"],
[270, "CAN Bricklet",""],
[271, "RGB LED Bricklet","actuator"],
[272, "RGB LED Matrix Bricklet","actuator"],
[276, "GPS Bricklet 2.0","sensor"],
[277, "RS485 Bricklet",""],
[278, "Thermal Imaging Bricklet",""],
[282, "RGB LED Button Bricklet","sensor"],
[283, "Humidity Bricklet 2.0","sensor"],
[284, "Dual Relay Bricklet 2.0","actuator"],
[285, "DMX Bricklet","actuator"],
[286, "NFC Bricklet","sensor"],
[287, "Moisture Bricklet 2.0","sensor"],
[288, "Outdoor Weather Bricklet","sensor"],
[289, "Remote Switch Bricklet 2.0","actuator"],
[291, "Temperature IR Bricklet 2.0","sensor"],
[292, "Motion Detector Bricklet 2.0","sensor"],
[294, "Rotary Encoder Bricklet 2.0","sensor"],
[295, "Analog In Bricklet 3.0","sensor"],
[296, "Solid State Relay Bricklet 2.0","actuator"],
[21111, "Stream Test Bricklet",""],
]

deviceIDs = [i[0] for i in deviceIdentifiersList]

if debug:
    print(deviceIDs)
    for i in range(len(deviceIDs)):
        print(deviceIdentifiersList[i])

def getIdentifier(ID):
    deviceType = ""

    for t in range(len(deviceIDs)):
        if ID[1]==deviceIdentifiersList[t][0]:
            deviceType = deviceIdentifiersList[t][1]
    return(deviceType)

# Tinkerforge sensors enumeration
def cb_enumerate(uid, connected_uid, position, hardware_version, firmware_version,
                 device_identifier, enumeration_type):
    tfIDs.append([uid, device_identifier])


def dmxread_callback(frame, frame_no):
    global prevFrame
    # if prevFrame. == 0:
    #     prevFrame = array(frame)
    frameArray = array(frame)
    if not array_equal(prevFrame,frameArray):
        if frame != None:
            print(frame)
    prevFrame = array(frame)
    # if prevframe-frame:
    #     print(frame, frame_no)
    # prev
    # print("callback called")

if __name__ == "__main__":
    # Create connection and connect to brickd
    ipcon = IPConnection()
    ipcon.connect(HOST, PORT)

    # Register Enumerate Callback
    ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, cb_enumerate)

    # Trigger Enumerate
    ipcon.enumerate()

    sleep(2)

    if verbose:
        print(tfIDs)

    dmxcount = 0
    for tf in tfIDs:
        # try:
        if True:
            # print(len(tf[0]))

            if len(tf[0])<=3: # if the device UID is 3 characters it is a bricklet
                if tf[1] in deviceIDs:
                    print(tf[0],tf[1], getIdentifier(tf))
                if tf[1] == 285: # DMX Bricklet
                    if dmxcount == 0:
                        print("Registering %s as slave DMX device for capturing DMX frames" % tf[0])
                        dmx = BrickletDMX(tf[0], ipcon)
                        dmx.set_dmx_mode(BrickletDMX.DMX_MODE_SLAVE)
                        dmx.register_callback(BrickletDMX.CALLBACK_FRAME, dmxread_callback)
                        dmx.set_frame_callback_config(False, False, True, False)

                    dmxcount += 1

    while True:
        pass

    if tfConnect:
        ipcon.disconnect()

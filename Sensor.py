# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:20:13 2015

@author: JMB
"""

def ReadLine(port):
    '''Reads a line of pixels. In the Arduino file distance_sensor.ino
    you can find how many pixels are red per line (tipically 64)
    '''
    port.flushInput() #- Empty the buffer
    port.write(' '.encode()) #- Send a space character
    aux = port.readline()
    line = aux.decode().split(';')[0:64]

    return line
    
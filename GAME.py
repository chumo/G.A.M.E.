def initiate_ports():
    global printerUSB, detectorUSB

    import serial
    printer = serial.Serial(printerUSB, 256000, timeout=5)
    detector = serial.Serial(detectorUSB, 9600, timeout=5)
    
    return printer, detector

    
if __name__ == '__main__':
    printerUSB = "COM3" # 3D printer 
    detectorUSB = "COM4" # Arduino controlling IR detector
    
    Zscan = 6.4
    Zmanip = 1.25
    LiftLM = 1.75

    xini = 10.
    yini = 30.

    printer, detector = initiate_ports()
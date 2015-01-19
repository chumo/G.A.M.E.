# -*- coding: utf-8 -*-

def SendGCODE(port, cmd):
    cmd += '\n'
    port.write(cmd.encode())

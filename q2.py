#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:Write a program that prints the IP address of the computer that it is being run on. 
            If the computer is not connected to the internet, it should print "not connected"
"""

import socket
import os

if __name__ == '__main__':
    # try:
    #     baidu = socket.gethostbyname("baidu.com")
    # except:
    #
    re = os.system('ping www.baidu.com')
    if re:
        print 'not connected'
    else:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print ip

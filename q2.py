#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:Write a program that prints the IP address of the computer that it is being run on. 
            If the computer is not connected to the internet, it should print "not connected"
"""


import os
import urllib
import re

def get_out_ip():
    
    url = "http://checkip.dyndns.org"
    request = urllib.urlopen(url).read()
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request).group(0)
    return ip

if __name__ == '__main__':
    reStr = os.system('ping www.google.com')
    if reStr:
        print 'not connected'
    else:
        ip = get_out_ip()
        print "your IP Address is: ", ip

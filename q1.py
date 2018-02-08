#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:Write a program that prints numbers from 1 to 1000 on each line. 
            1.But for numbers that are multiples of 7 print "Docket" instead of the number. 
            2.For multiples of 6 print "Alarm" instead of the number. 
            3.For numbers that are multiples of both 6 and 7 print "Docket Alarm"
"""
if __name__ == '__main__':
    for i in range(1,1001):
        if i%6 ==0 and i%7==0:
            print 'Docket Alarm'
        elif i%7==0:
            print 'Docket'
        elif i%6==0:
            print 'Alarm'
        else:
            print i
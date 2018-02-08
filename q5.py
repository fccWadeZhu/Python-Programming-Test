#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:a.Create a program that downloads the page located here and saves it to the file q5-1.html.
            b.Then have the program click the checkbox, and select continue, download the resulting case search page and save it into a file named q5-2.html
"""

import urllib
import urllib2


if __name__ == '__main__':

    values = {"disclaimer": "Y", "action": "Continue"}
    data = urllib.urlencode(values)
    url = "http://casesearch.courts.state.md.us/casesearch/processDisclaimer.jis"
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    downloadPath ="c:/q5-2.html"
    urllib.urlretrieve(url, downloadPath,None,data)
    print 'download complete!'

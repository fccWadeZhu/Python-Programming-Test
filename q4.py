#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:
            a.Build on top of the previous answer to create a program that downloads 50 cases sequentially. 
              Note the form of the URL, to scan through caseids 23800 to 23850.
            b.Output the result into a JSON format into a file named q4.json. 
              The JSON format should be a list, where each list item is in the same form of the JSON object you created in question 3.
"""

import urllib
import urllib2
from bs4 import BeautifulSoup
import json
from q3 import crawleappsByCaseId

if __name__ == '__main__':
    resultList = []
    for caseId in range(23800, 23851):
        result = crawleappsByCaseId(str(caseId), False)
        resultList.append(result)
    jsonResult = json.dumps(resultList)
    f = open("./q4.json", "w")
    f.write(jsonResult)
    f.close()
    print 'complete!'

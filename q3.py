#!/usr/bin/env python

# -*- coding: utf-8 -*-

__title__ = ''

__author__ = 'Wade'

__mtime__ = '2018/2/8'
"""
Description:a.Write a scraper which can download and parse the page here
            b.The program should output the Appellant name, Appellee name, CAV record number, and date recieved. 
            The format should be in JSON and saved to a filename q3.json. The exact format of the JSON file is not important.
"""

import urllib
import urllib2
from bs4 import BeautifulSoup
import json
if __name__ == '__main__':
    result = {}
    try:
        url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId=23811'
        values = {"caseId": "23811"}
        headers = {'Cookie':'JSESSIONID=0000ZRWCvFtTH5Kz2JlSKksfY3v:1962kbr3k','Host':'eapps.courts.state.va.us','User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data,headers)
        response = urllib2.urlopen(request)
        webpage = response.read().decode('utf-8')
        soup = BeautifulSoup(webpage, 'html.parser')
        # get Appellant name
        appellantTable = soup.find('table',id='listofPartiesAPL')
        appellantTds = appellantTable.find('tr',class_='alternaterow2').find_all('td')
        appellantName = appellantTds[0].get_text().strip()
        result['Appellant name'] = appellantName
        # get Appellee name
        appelleeTable = soup.find('table', id='listofPartiesAPE')
        appelleeTds = appelleeTable.find('tr', class_='alternaterow2').find_all('td')
        appelleeName = appelleeTds[0].get_text().strip()
        result['Appellee name'] = appelleeName
        # get CAV record number
        cavRecordDiv = soup.find('div',class_='customtab')
        cavBtag =cavRecordDiv.find('b')
        cavRecordNumber = cavBtag.get_text().replace('CAV Record #','').strip()
        result['CAV record number'] = cavRecordNumber
        # get date recieved
        cavReceiveDiv = soup.find('div',id='noticeOfAppealSlider')
        cavReceiveTds = cavReceiveDiv.find('table').find_all('td')
        cavReceivedDate = cavReceiveTds[1].find('input')['value']
        result['CAV date recieved'] = cavReceivedDate
        jsonResult = json.dumps(result)
        f = open("./q3.json", "w")
        f.write(jsonResult)
        f.close()
    except Exception as e:
        print e

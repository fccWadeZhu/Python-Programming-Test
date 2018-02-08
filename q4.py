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
if __name__ == '__main__':
    resultList = []
    for caseId in range(23800, 23851):
        result = {}
        url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry'
        values = {"caseId": caseId}
        headers = {'Cookie': 'JSESSIONID=0000ZRWCvFtTH5Kz2JlSKksfY3v:1962kbr3k', 'Host': 'eapps.courts.state.va.us', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        try:
            webpage = response.read().decode('utf-8')
            soup = BeautifulSoup(webpage, 'html.parser')
            # get Appellant name
            appellantTable = soup.find('table', id='listofPartiesAPL')
            appellantTds = appellantTable.find('tr', class_='alternaterow2').find_all('td')
            appellantName = appellantTds[0].get_text().strip()
            result['Appellant name'] = appellantName
            # get Appellee name
            appelleeTable = soup.find('table', id='listofPartiesAPE')
            appelleeTds = appelleeTable.find('tr', class_='alternaterow2').find_all('td')
            appelleeName = appelleeTds[0].get_text().strip()
            result['Appellee name'] = appelleeName
            #get CAV record number
            cavRecordDiv = soup.find('div', class_='customtab')
            cavBtag =cavRecordDiv.find('b')
            cavRecordNumber = cavBtag.get_text().replace('CAV Record #','').strip()
            result['CAV record number'] = cavRecordNumber
            #get date recieved
            cavReceiveDiv = soup.find('div', id='noticeOfAppealSlider')
            cavReceiveTds = cavReceiveDiv.find('table').find_all('td')
            cavReceivedDate = cavReceiveTds[1].find('input')['value']
            result['CAV date recieved'] = cavReceivedDate
            resultList.append(result)
        except Exception as e:
            print e
    jsonResult = json.dumps(resultList)
    f = open("c:/q4.json", "w")
    f.write(jsonResult)
    f.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CCStockAnalyse.py
#  
#  Created by CC on 2017/10/28.
#  Copyright 2017 youhua deng (deng you hua | CC) <ccworld1000@gmail.com>
#  https://github.com/ccworld1000/CCStockAnalyse
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
import os
import time
import json
import requests

def getTimestamp () :
	ts = time.time()
	ts1000 =  str(long (float(ts) * 1000))
	print str(ts1000)
		
	return ts1000
		
class CCParam (object) :
	def __init__ (self, stock_code, step, start, count, timestamp) :
		self.stock_code = stock_code
		self.step = step;
		self.start = start
		self.count = count
		self.timestamp = timestamp;
		
		self.os_ver=1
		self.cuid='xxx'
		self.vv=100
		self.fq_type='no'

	def convertParam(self) :
		index = 1;
		strings = []
		for k, v in self.__dict__.items() :
			paris = "{}={}".format(k, v)
			print "[CC " + str(index) + "] " + paris

			strings.append(paris)

			index = index + 1
		
		strings.append("from=pc")
		strings.append("format=json")
		
		retString = "&".join (strings)
			
		print retString
		
		return retString
		

	def genHeaders (self, url) :
		host = url
		if url :
			match = re.compile (':\/\/(.*?com)')
			res = match.search(url)
			if res :
				host = res.group(1)
			
		headers = {
			'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'en-US,en;q=0.8',
			'Connection':'keep-alive',
			'Cookie':'IDUPSID=9A83A4241A43A21C91557E6DE8AA8709; PSTM=1508161587; BAIDUID=300644275A35780F55B642CE762700A7:FG=1; PSINO=6; H_PS_PSSID=24875_1454_24886_21099_18559_23384_22159; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_35d1e71f4c913c126b8703586f1d2307=1509225661,1509226500,1509302137,1509307401; Hm_lpvt_35d1e71f4c913c126b8703586f1d2307=1509307413',
			'Host': host,
			#'Referer':url,
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		}
		
		return headers
	
	def getSite (self, url, param) :
		headers = self.genHeaders(url)
		requests.Session()
		address = "{}?{}".format(url, param)
		print address
		r = requests.get (address, headers = headers)
		r.encoding = r.apparent_encoding
		html = r.text
		
		print html



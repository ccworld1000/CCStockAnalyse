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
import json
import requests



class CCParm (object) :
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


	def genHeaders (url) :
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
			'Cookie':'UM_distinctid=15f437b4b97121-042a2340cadd34-31607c03-fa000-15f437b4b98a8; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1508665672; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1508706346',
			'Host': host,
			'Referer':url,
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		}
		
		return headers
	
	def getSite (url, rootdir) :
		headers = genHeaders(url)
		requests.Session()
		r = requests.get (url, headers = headers)
		r.encoding = r.apparent_encoding
		html = r.text



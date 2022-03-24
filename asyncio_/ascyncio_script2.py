



:q
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import os

import timeit



async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(what)

async def main2(num):
	task1 = asyncio.create_task(say_after(num+1, 'task1'))
	task2 = asyncio.create_task(say_after(num, 'task2'))
	
	await task1
	await task2


user_agent = ''' 
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) 
              AppleWebKit/537.36 (KHTML, like Gecko) 
              Chrome/61.0.3163.100 Safari/537.36'
             '''

async def async_scraper(url):
	content = asyncio.create_task(Request(url, headers={
          	'authority': 'https://dockets.justia.com/',
          	'scheme': 'https',
          	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}))
	# Create HTML object
	html = asyncio.create_task(urlopen(content))
        # Create Beautiful Soup Object  
	bsObj = asyncio.create_task(BeautifulSoup(html.read(), 'lxml'))

	await content
	await html
	await bsObj


List_urls = ["https://dockets.justia.com/docket/california/casdce/3:2013cv01037/413395",  
	     "https://dockets.justia.com/docket/new-hampshire/nhdce/1:2013cv00213/39165", 
	     "https://dockets.justia.com/docket/circuit-courts/ca4/13-6689",  
	     "https://dockets.justia.com/docket/circuit-courts/ca8/13-1987",  
	     "https://dockets.justia.com/docket/circuit-courts/ca9/13-55730",  
             "https://dockets.justia.com/docket/multi-district/jpml/ILS/3:13-cv-50340/837566"] 

async def get_page():
	for i in List_urls:
		start = timeit.timeit() 
		async_scraper(i)
		await async_scraper
		end = timeit.timeit()
		print('''Start => {}   
		         End   => {}'''.format(start, end))
		

asyncio.run(get_page())



		





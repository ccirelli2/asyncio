'''Documentation / Notes
Reference	https://aiohttp.readthedocs.io/en/stable/client_quickstart.html


'''


# aiohttp client API
import aiohttp


# Exampl1 - Request
session = aiohttp.ClientSession()

async with session.get('http://httpbin.org/get') as resp:
	print(resp.status)
	print(await resp.text())





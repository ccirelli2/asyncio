# LEARN ASYNCIO

'''
Coroutines:  	Coroutines look like a normal function, but in their 
		behaviour they are stateful objects with resume() and pause() — 		like methods.
Pause:		The way a coroutine pauses itself is by using the 'await' 
		keyword.  When you 'await' another coroutine, you 'step off'
		the event loop and schedule the awaited coroutine to run
		immediately. 
Application:	it could be anything in a real world scenario like a network 
		request, db query etc.

aiohttp		apparently is a library specifically for http requests


defining	rather than def something, you async def something, which notifies 
                that you want to coroutine something. 


'''


import asyncio
import timeit


# We need to insert functions into that loop
# loop.create_task(function_here)

async def counter2(num_start, num_end):
	list_num = []
	start = timeit.timeit()

	for i in range(num_start, num_end):
		if i == 5000:
			print('equals 5000')
			await asyncio.sleep(0.0001)
			list_num.append(i)
			pass
		else:
			pass        
	end = timeit.timeit()
	start = round(start, 6)
	end =   round(end, 6)
	print('Start => {}    End => {}'.format(start, end))

	return None

async def main2():
	test1 = loop.create_task(counter2(0,100000000))
	test2 = loop.create_task(counter2(0,1000000))	
	test3 = loop.create_task(counter2(0,10000))
	await asyncio.wait([test1, test2, test3])



if __name__ == "__main2__":
        loop = asyncio.get_event_loop()    # establish loop
        loop.run_until_complete(main2())
        loop.close()                       # always want to close loop

	


counter2(0,10000)

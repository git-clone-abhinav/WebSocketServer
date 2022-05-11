import asyncio
import websockets
import time

async def my_connect():
	async with websockets.connect("ws://localhost:3000") as websocket:
		for i in range(1,10,1):
			await websocket.send("Hi server. kese hoe" );
			data_rcv = await websocket.recv();
			print("data received from server : " + data_rcv)
			time.sleep(1)
# connect to server
asyncio.get_event_loop().run_until_complete(my_connect());

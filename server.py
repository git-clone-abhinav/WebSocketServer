import asyncio 
import websockets

# call back for websockets.serve(xx,
async def my_accept(websocket, path): 
    while True:
        data_rcv = await websocket.recv(); # receiving the data from client. 
        print("received data = " + data_rcv); 
        await websocket.send("websock_svr send data = " + data_rcv); # send received data

# websocket server creation
websoc_svr = websockets.serve(my_accept,"localhost",3000);

print("This is WebSocket Server: Waiting for client Access");

# waiting 
asyncio.get_event_loop().run_until_complete(websoc_svr); 
asyncio.get_event_loop().run_forever(); 

#!/usr/bin/env python

import asyncio
import json
import websockets

code = 'WWSU'

async def accept_clients(websocket, path):
    # name = await websocket.recv()
    # print(f"< {name}")

    # greeting = f"Hello {name}!"

    # await websocket.send(greeting)
    # print(f"> {greeting}")
    await websocket.send(json.dumps({'message': 'Enter 4 digit key', 'message_id': 0}))
    client_code = json.loads(await websocket.recv())

    if 'code' in client_code.keys() and client_code['code'] == code:
        await websocket.send(json.dumps({'message': 'Connection accepted', 'code': 1}))

        while True:
            await websocket.send(json.dumps({'message': 'ping', 'message_id': 2}))
            await asyncio.sleep(1)
    else:
        await websocket.send(json.dumps({'message': 'nope, get outta here', 'message_id': -1}))

start_server = websockets.serve(hello, 'localhost', 1337)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
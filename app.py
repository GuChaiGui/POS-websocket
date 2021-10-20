import asyncio
import websockets
from win32printing import Printer

async def server(websocket, path):
    async for message in websocket:    
        await websocket.send(f'We are going to print: {message}')    
    
        with Printer(linegap=1) as printer:
            printer.text(message)

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
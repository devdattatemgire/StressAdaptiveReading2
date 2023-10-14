# myapp/consumers.py

import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data['action'] == 'start_sensor':
            await self.send(text_data=json.dumps({'status': 'Sensor Started'}))
            # Logic to start the sensor and send data periodically
            await asyncio.sleep(5)  # Example: wait for 5 seconds
            await self.send(text_data=json.dumps({'reading': 42}))  # Example: send a reading
            # You can continue sending readings periodically

        elif data['action'] == 'stop_sensor':
            # Logic to stop the sensor
            await self.send(text_data=json.dumps({'status': 'Sensor Stopped'}))

        elif data['action'] == 'connect':
            # Logic to connect/disconnect to/from Raspberry Pi
            await self.send(text_data=json.dumps({'status': 'Connection Established/Disconnected'}))

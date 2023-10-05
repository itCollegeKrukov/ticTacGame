from channels.consumer import AsyncConsumer
clients = []
rooms = []


class YourConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        clients.append(self)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        print(text_data)

        if text_data['text'].startswith('create'):
            text_data
        for i in clients:
            if i != self:
                await i.send({"type": "websocket.send", "text": text_data['text']})

    async def websocket_disconnect(self, event):
        pass


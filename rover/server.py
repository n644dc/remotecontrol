from tornado import websocket, web, ioloop
import json

cl = []

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)
        self.sendMsg("Client Connected")

    def on_close(self):
        if self in cl:
            cl.remove(self)

    def on_message(self, message):
        messageObject = json.loads(message)
        print(messageObject['type'] + " - " + messageObject['value'])
        

    def sendMsg(self, message):
         data = {"type": "server", "value" : message}
         self.write_message(data)
         
        

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler)
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()

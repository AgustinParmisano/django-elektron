from tornado_websockets.websocket import WebSocket

tws = WebSocket('/echo')

# Listen the « message » event
@tws.on
def message(socket, data):
    socket.emit('new_message', {
        'message': data.get('message')
})

"""
import tornado
import tornado.websocket
from tornado import gen
import datetime, sys, time
import ast
import json
import random
from datetime import timedelta



#Websockets clients
clients = []

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    tt = datetime.datetime.now()

    def check_origin(self, origin):
        #print "origin: " + origin
        return True

    # the client connected
    def open(self):
        print ("New client connected")
        self.write_message("You are connected")
        clients.append(self)
        tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=1), self.test)

    @gen.coroutine
    def test(self):
        try:
            n = random.randint(0,100)
            message = {"data": n}
            try:
                time.sleep(1)
                self.write_message(message)
            except Exception as e:
                print "Exception in test write message: "
                print e
                #raise(e)
        except Exception as e:
            print "Exception in test write message 2: "
            print e
            self.write_message("Es un write message exeption:" + str(e))
            #raise(e)
        else:
            tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=0.1), self.test)

    # the client sent the message
    def on_message(self, message):
        print ("Message: " + message)
        try:
           msg = json.loads(message.payload)
           data_json = {}
           print "MESSAGE FROM WEB SOCKET"
           print "MSG TYPE"
           print type(msg)
           print "MSG DATA"
           print  msg
           #message = ast.literal_eval(message)
           #print("AST Message: " + str(message))

        except Exception as e:
            print ("Exception in on_message:")
            print e
        #self.write_message(message)

    # client disconnected
    def on_close(self):
        print ("Client disconnected")
        clients.remove(self)

socket = tornado.web.Application([(r"/websocket", WebSocketHandler),])

print("Starting WebSocket")
print("Opening port 8888")
socket.listen(8888)

tornado.ioloop.IOLoop.instance().start()
"""

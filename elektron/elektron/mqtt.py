import paho.mqtt.client as mqtt
import time
import json
import requests

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("sensors/new_sensor")
   client.subscribe("sensors/new_data")


def on_message(client, userdata, msg):
   print("msg.topic: " + msg.topic+" msg.payload "+str(msg.payload))

   list = json.loads(msg.payload)
   data_json = {}

   for key,value in list.iteritems():
       data_json[key] = value
       print ("")
       print key, value
       print "data_json"
       print data_json

def on_subscribe(client, userdata,mid, granted_qos):
   print "userdata : " +str(userdata)

def on_publish(mosq, obj, mid):
   print("mid: " + str(mid))


def on_message_device(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))

   list = json.loads(msg.payload)
   data_json = {}
   print list
   r = requests.post("http://localhost:8000/devices/", data={'device_ip': "12524", 'label': 'issue', 'state': 'on', 'measure':'100'})
   print("REQUEST (POST): ")
   print r
   print(r.status_code, r.reason)
   print("RESPUESTA AL REQUEST:")
   print(r.text[:255] + '...')

class MqttClient(object):
    """docstring for MqttClient."""
    def __init__(self, client=mqtt.Client()):
        super(MqttClient, self).__init__()
        self.client = client
        self.client.on_connect = on_connect
        self.client.on_message = on_message_device
        self.client.connect("localhost", 1883, 60)

    def get_client(self):
        return self.client

    def set_on_connect(self, func):
        self.on_connect = func

    def publish(message, topic):
         print("Sending %s " % (message))
         publish.single(str(topic), message, hostname="localhost")
         return "Sending msg: %d " % (message)

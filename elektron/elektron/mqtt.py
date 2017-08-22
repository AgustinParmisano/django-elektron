import paho.mqtt.client as mqtt
import time
import datetime
import json
import ast
import requests

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   #client.subscribe("sensors/new_sensor")
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

   llist = json.loads(msg.payload)
   data_json = {}
   print "LLLLLLLLLLLLLLLLLL"
   print type(llist)

   devices_request = requests.get("http://localhost:8000/devices/?format=json")

   print("REQUEST (POST): ")
   print devices_request
   print(devices_request.status_code, devices_request.reason)

   devices_json = json.loads(devices_request.text)


   print("RESPUESTA AL REQUEST (JSON):")
   print(devices_json)

   #print(ast.parse(devices_json, mode='eval'))
   #print ast.literal_eval(str(devices_json))
   print "total_devices"
   total_devices = devices_json["count"]

   devices = devices_json["results"]
   for device in devices:
       print device
       print "device mac"
       print device["device_mac"]
       #if


   #r = requests.get("http://localhost:8000/data/", data={'device': "3"})
   #r = requests.post("http://localhost:8000/data/", data={'device': "3", 'date': datetime.datetime.now(), 'data_value':'150'})



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

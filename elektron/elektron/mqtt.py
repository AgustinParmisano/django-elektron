import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import datetime
import json
import ast
import requests

def msg_ws(msg):
   resp = publish.single("data_to_web", msg, hostname="localhost")
   return resp

def check_device(device_mqtt):
    device_ok = False
    devices_request = requests.get("http://localhost:8000/devices/?format=json")

    devices_json = json.loads(devices_request.text)

    #print("RESPUESTA AL REQUEST (JSON):")
    #print(devices_json)

    #print "total_devices"
    total_devices = devices_json["count"]

    devices = devices_json["results"]

    for device in devices:
        #print device
        #print "device mac"
        #print device["device_mac"]
        if (device["device_mac"] == device_mqtt["mac"]):
            device_ok = device_mqtt

    return device_ok


def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   #client.subscribe("sensors/new_sensor")
   client.subscribe("sensors/new_data")


def on_message_device(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))

   mqtt_data = json.loads(msg.payload)
   print "mqtt_data"
   print mqtt_data

   device_ok = check_device(mqtt_data)

   if device_ok != False:
        mqtt_data = ast.literal_eval(json.dumps(mqtt_data))
        message = str(mqtt_data)
        msg_ws(message)

   #r = requests.get("http://localhost:8000/data/", data={'device': "3"})
   #r = requests.post("http://localhost:8000/data/", data={'device': "3", 'date': datetime.datetime.now(), 'data_value':'150'})


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

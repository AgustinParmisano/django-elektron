import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import datetime
import json
import ast
import requests
import Queue

qmsg = Queue.Queue()

def remove_duplicated_msg(mqtt_data):
    print  "mqtt_data"
    print  mqtt_data

    if qmsg.qsize() > 10:
        qmsg.get()

    if mqtt_data != None and mqtt_data != "" and mqtt_data not in qmsg.queue:
        qmsg.put(mqtt_data)
        qmsg.get()
        del mqtt_data["data_id"]

        return mqtt_data

def msg_ws(msg):
   resp = publish.single("data_to_web", msg, hostname="localhost")
   return resp

def create_new_device(device_mqtt):
    print("Creating new device in server")

    #print device_mqtt

    device_data = device_mqtt #{'device_ip': '10.0.0.3', 'device_mac': '22:22:22:22', 'devicestate': 1, 'label': 'horno'}

    r = requests.post("http://localhost:8000/devices/", data=device_data)

def check_data(mqtt_data):
    result = requests.post("http://localhost:8000/data/create", data=mqtt_data)
    return result

def check_device(device_mqtt):
    result = requests.post("http://localhost:8000/devices/create", data=device_mqtt)
    return result

def on_connect(client, userdata, flags, rc):
   print("MQTT Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   #client.subscribe("sensors/new_sensor")
   client.subscribe("sensors/new_data")


data_list = []
def on_message_device(client, userdata, msg):
   #print(msg.topic+" "+str(msg.payload))

   mqtt_data = ast.literal_eval(str(msg.payload)) #json.loads(str(msg.payload))
   #print "mqtt_data"
   #print mqtt_data
   #print type(mqtt_data)

   mqtt_data # = remove_duplicated_msg(mqtt_data)

   device_ok = check_device(mqtt_data)

   if device_ok != False:
        mqtt_data = ast.literal_eval(json.dumps(mqtt_data))
        message = str(mqtt_data)
        msg_ws(message)
        mqtt_data = check_data(mqtt_data)



"""
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
"""

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

if __name__ == "__main__":
    print "Starting MQTT"
    mqtt = MqttClient()
    #mqtt.client.loop_start()
    mqtt.client.loop_forever()

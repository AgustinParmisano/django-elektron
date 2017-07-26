from elektron.mqtt import MqttClient

def on_message_device(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))

   list = json.loads(msg.payload)
   data_json = {}

   for key,value in list.iteritems():
       data_json[key] = value
       print ("")
       print key, value
       print "data_jsonaaaaaaa"
       print data_json
       get_device_message(data_json)

def get_device_message(data_json):
    dev_ip = data_json["device_ip"]

    queryset = Device.objects.get(device_ip=dev_ip)

    print "queryset"
    print queryset


mqtt = MqttClient()
mqtt.on_message = on_message_device
mqtt.client.loop_start()

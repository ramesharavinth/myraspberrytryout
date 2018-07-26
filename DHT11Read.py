import json
import paho.mqtt.client as mqtt
#import Adafruit_DHT as adafrt
import random, time

def on_connect():  
    data = dict()
    while True:
        humidity = random.randint(1,100)
        temperature = random.randint(1,50)  # GPIO27 (BCM notation)
        #humidity, temperature = adafrt.read_retry(11, 27)  # GPIO27 (BCM notation)
        print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
        data["humidity"] = humidity
        data["temperature"] = temperature
        data_out = json.dumps(data) #create json object
        print (data_out)
        time.sleep(10)
        client.publish("kwf/demo/dht",data_out)

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.on_connect = on_connect


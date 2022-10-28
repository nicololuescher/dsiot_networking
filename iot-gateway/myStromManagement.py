import paho.mqtt.client as mqtt
import time
import requests
from scanner import Scanner

class myStromManagement:

    mainTopic="myStrom"

    def __init__(self, clients):
        self.clients = clients
        
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.username_pw_set("guest", "gibbiX12345")
        client.connect("mqtt.nicolo.info", 1883,60)

        client.loop_forever()

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(f"{self.mainTopic}/#")



    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        
        if(msg.topic == f"{self.mainTopic}/toggle/all"):
            for client in self.clients:
                requests.get(f"http://{client}/toggle")


if __name__ =="__main__":
    scanner = Scanner()
    time.sleep(10)
    test = myStromManagement(scanner.get_device_hostnames())
    
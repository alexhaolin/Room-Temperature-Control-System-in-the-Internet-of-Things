'''
Created on 2018��12��7��

@author: Alex
'''
import paho.mqtt.client as mqttClient
from app.common import ActuatorData
from app.module import TempActuatorEmulator

def on_connect(clientConn, data, flags, resultCode):
    print("Client connected to server. Result: " + str(resultCode))
    clientConn.subscribe("ActuatorData")
    
def on_message(clientConn, data, msg):
    print("Received PUBLISH on topic {0}. Payload: {1}".format(str(msg.topic), str(msg.payload)))
    tempactuator = int(msg.payload)
    actuatordata = ActuatorData.ActuatorData()
    if(tempactuator == 21):
        actuatordata.setValue(tempactuator)
        actuatordata.setCommand("raise")      
    if(tempactuator == 22):
        actuatordata.setValue(tempactuator)
        actuatordata.setCommand("lower")
    actuatoremulator = TempActuatorEmulator()
    actuatoremulator.processMessage(actuatordata)                 

mc = mqttClient.Client()
mc.on_connect = on_connect
mc.on_message = on_message

mc.connect("test.mosquitto.com", 1883, 60)

mc.loop_forever()
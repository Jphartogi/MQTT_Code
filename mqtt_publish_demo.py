
import paho.mqtt.client as mqtt

broker = "192.168.101.146"
port = 1883
timeout = 60

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
   

def on_publish(client,userdata,result):
	print("data published \n")
	pass


#this example reads and prints CO2 equiv. measurement, TVOC measurement, and temp every 2 seconds

from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

ccs =  Adafruit_CCS811()

while not ccs.available():
	pass
temp = ccs.calculateTemperature()
ccs.tempOffset = temp - 25.0

client1 = mqtt.Client("device1")
client1.username_pw_set(username="username",password="Jps040697")
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port)



while(1):
	if ccs.available():
	    temp = ccs.calculateTemperature()
	    if not ccs.readData():
	        message = "CO2:"+ str(ccs.geteCO2())+ "ppm, TVOC: " +str(ccs.getTVOC())+ " temp: "+ str(temp)
	        ret = client1.publish("Test",message)
	        print("CO2:", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp)

	    else:
	      print("ERROR!")
	      
	sleep(0.5)





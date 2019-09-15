
import paho.mqtt.client as mqtt

broker = "192.168.1.29"
port = 1883
timeout = 60

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
   

def on_publish(client,userdata,result):
	print("data published \n")
	pass


client1 = mqtt.Client("device1")
client1.username_pw_set(username="username",password="Jps040697")
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port)
ret = client1.publish("Test","World!")

print('Done!')


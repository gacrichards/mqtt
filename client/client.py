import paho.mqtt.client as mqtt
import time

# Create an MQTT client instance
client = mqtt.Client()
# MQTT Broker settings
broker_address = "mqtt-pi.local"  # Replace with your broker's address
broker_port = 1884  # +1 Default MQTT port

#these are abstract and should be set by the implementing script
msg_callback = None
dconn_callback = None

topic = "testTopic/test"

# Callback function when connection is established
def on_connect(client, userdata, flags, rc):
    print("on connected with result code "+str(rc))
    print("this client is now connected "+str(client.is_connected()))

# Callback function when connection is lost    
def on_disconnect(client, userdata, rc):
    print("on disconnect called")
    if rc != 0:
        print("Disconnected from broker "+str(rc))
        global dconn_callback
        if dconn_callback is not None:
            dconn_callback()
        
# Callback function when a message is received
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    print("Received message: "+message+" on topic "+topic)
    global msg_callback
    if msg_callback != None:
        msg_callback(msg.topic, message)
        
# Set up callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

def connect():
    # Connect to the broker
    global client
    client.username_pw_set("pibot", "pibot1031")
    client.connect(broker_address, broker_port, 60)
    client.loop_start()
    
def subscribe(topics):
    # Start the MQTT loop in the background
    global client
    for topic in topics:
        print("subscribing to " + topic)
        client.subscribe(topic)

def publish(topic, msg):
    global client
    print("publishing " + msg + " on " + topic)
    client.publish(topic, msg)
    
    
def kill():
    # Disconnect from the broker and stop the loop
    global client
    client.loop_stop()
    client.disconnect()
    client = None

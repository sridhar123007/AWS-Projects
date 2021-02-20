from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time,json
import datetime

host = "a22cfudg6h1klz-ats.iot.ap-south-1.amazonaws.com" #IoT core End Point url
rootCAPath = "rootCAcert.pem"
certificatePath = "37c8d05cc4-certificate.pem.crt"
privateKeyPath = "37c8d05cc4-private.pem.key"
topic = "smartparking"

# Custom MQTT message callback
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")
	

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient("smartparking")
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)


# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("smartparkin", 1, customCallback)
time.sleep(2)



while True:
        date=str (datetime.datetime.now())
        JSONPayload = {'slot':1,'time': date,'temperature': 30, 'humidity': 50}
        print json.dumps(JSONPayload)
        myAWSIoTMQTTClient.publish(topic,json.dumps(JSONPayload), 1)
        time.sleep(5)
    





/* ESP8266 AWS IoT example by Evandro Luis Copercini
   Public Domain - 2017
   But you can pay me a beer if we meet someday :D
   This example needs https://github.com/esp8266/arduino-esp8266fs-plugin
  It connects to AWS IoT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
*/

#include "FS.h"
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

#include "DHT.h"

#define DHTPIN D2     // what pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

// Update these with values suitable for your network.

const char* ssid = "Smartbridge";
const char* password = "iotgyan@sb";

char *topic="IoT123";
long lastMsg = 0;
char msg[50];
int value = 0;
int h, t;
String command;

const size_t capacity = JSON_OBJECT_SIZE(1) + 35;
DynamicJsonDocument doc(capacity);


WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

const char* AWS_endpoint = "a22cfudg6h1klz-ats.iot.us-west-2.amazonaws.com"; //MQTT broker ip


void callback(char* topic, byte* payload, unsigned int length) {
//topic="outTopic";
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    command+=(char)payload[i];
  }
  Serial.print("data:"+ command);

  if(command.equals("lighton"))
  {
    Serial.println("ledon");
    digitalWrite(D3,LOW);
    }
    if(command.equals("lightoff"))
  {
    Serial.println("ledoff");
    digitalWrite(D3,HIGH);
    }
  Serial.println();
  command= "";
}
WiFiClientSecure espClient;
PubSubClient client(AWS_endpoint, 8883, callback, espClient); //set  MQTT port number to 8883 as per //standard


void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  espClient.setBufferSizes(512, 512);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  timeClient.begin();
  while(!timeClient.update()){
    timeClient.forceUpdate();
  }

  espClient.setX509Time(timeClient.getEpochTime());

}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("harish")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe(topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");

      char buf[256];
      espClient.getLastSSLError(buf,256);
      Serial.print("WiFiClientSecure SSL error: ");
      Serial.println(buf);

      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  
  dht.begin();
  pinMode(D3,OUTPUT);

  Serial.begin(115200);
  Serial.setDebugOutput(true);
  setup_wifi();
  delay(1000);
  if (!SPIFFS.begin()) {
    Serial.println("Failed to mount file system");
    return;
  }

  Serial.print("Heap: "); Serial.println(ESP.getFreeHeap());

  // Load certificate file
  File cert = SPIFFS.open("/cert.der", "r"); //replace cert.crt eith your uploaded file name
  if (!cert) {
    Serial.println("Failed to open cert file");
  }
  else
    Serial.println("Success to open cert file");

  delay(1000);

  if (espClient.loadCertificate(cert))
    Serial.println("cert loaded");
  else
    Serial.println("cert not loaded");

  // Load private key file
  File private_key = SPIFFS.open("/private.der", "r"); //replace private eith your uploaded file name
  if (!private_key) {
    Serial.println("Failed to open private cert file");
  }
  else
    Serial.println("Success to open private cert file");

  delay(1000);

  if (espClient.loadPrivateKey(private_key))
    Serial.println("private key loaded");
  else
    Serial.println("private key not loaded");



    // Load CA file
    File ca = SPIFFS.open("/ca.der", "r"); //replace ca eith your uploaded file name
    if (!ca) {
      Serial.println("Failed to open ca ");
    }
    else
    Serial.println("Success to open ca");

    delay(1000);

    if(espClient.loadCACert(ca))
    Serial.println("ca loaded");
    else
    Serial.println("ca failed");

  Serial.print("Heap: "); Serial.println(ESP.getFreeHeap());
}



void loop() {
   h = dht.readHumidity();
  // Read temperature as Celsius (the default)
   t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) ) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  delay(2000);

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();

  const char* json = "{\"message\":\"hello word\"}";

 
//  if (now - lastMsg > 2000) {
  //  lastMsg = now;
    //++value;
    sprintf (msg,  "hello world #Humidity = %d, Temperature = %d", h,  t);
    Serial.print("Publish message: ");
    Serial.println(json);
    client.publish("outTopic", msg);
    Serial.print("Heap: "); Serial.println(ESP.getFreeHeap()); //Low heap can cause problems
 // }
}

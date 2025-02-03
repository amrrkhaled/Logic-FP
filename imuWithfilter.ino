#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <WiFi.h>

const char *ssid = "ESP8266-AP";        // ESP8266 Access Point SSID
const char *password = "12345678";      // ESP8266 Access Point password
const char *host = "192.168.4.1";       // IP of ESP8266 Access Point (default 192.168.4.1)

WiFiClient client;

Adafruit_MPU6050 mpu;
float ax, ay, az;  // Acceleration values
const float alpha = 0.9;  // Low-pass filter factor

void setup() {
  Serial.begin(115200);

  // Initialize the MPU6050 sensor
  if (!mpu.begin()) {
    Serial.println("Could not find a valid MPU6050 sensor. Check wiring!");
    while (1);
  }
  Serial.println("MPU6050 initialized successfully.");

  // Connect to ESP8266 Access Point
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi!");
}

void loop() {
  // Read the accelerometer data
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Apply low-pass filter to smooth acceleration data
  ax = alpha * ax + (1 - alpha) * a.acceleration.x;
  ay = alpha * ay + (1 - alpha) * a.acceleration.y;
  az = alpha * az + (1 - alpha) * a.acceleration.z;

  // Threshold for movement detection
  String movement = "None";
  byte movementByte = 0;

  // Determine movement direction and set corresponding byte value
  if (ay > 1.0) {
    movement = "Moving forward";
    movementByte = B10101;  // Forward command
  } else if (ay < -1.0) {
    movement = "Moving backward";
    movementByte = B01010;  // Backward command
  } else if (ax > 1.0) {
    movement = "Turning right";
    movementByte = B00101;  // Right turn command
  } else if (ax < -1.0) {
    movement = "Turning left";
    movementByte = B00011;  // Left turn command
  } else {
    movement = "Stopping";
    movementByte = B00000;  // Stop command
  }

  // Connect to ESP8266 and send the byte data
  if (WiFi.status() == WL_CONNECTED) {
    if (client.connect(host, 80)) {  // Connect to ESP8266 server
      client.write(movementByte);  // Send movement byte
      Serial.println("Sent data: " + movement);
      client.stop();  // Disconnect after sending
    } else {
      Serial.println("Connection failed");
    }
  }

  delay(1000);  // Delay before sending next data
}

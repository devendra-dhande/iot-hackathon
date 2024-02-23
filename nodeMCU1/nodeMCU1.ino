
#include <ESP8266WiFi.h>

const char* ssid = "SUNBEAM";
const char* password = "1010101010";


const int switch1Pin = D0;
const int switch2Pin = D1;
const int led1Pin = D2;
const int led2Pin = D3;


int switch1State = 0;
int switch2State = 0;
int led1State = 0;
int led2State = 0;

void setup() {
  Serial.begin(115200);


  pinMode(switch1Pin, INPUT_PULLUP);
  pinMode(switch2Pin, INPUT_PULLUP);


  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);

  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");



void loop() {
  
  switch1State = digitalRead(switch1Pin) == LOW;
  switch2State = digitalRead(switch2Pin) == LOW;

  //for toggle LED states based on switch states
  if (switch1State != led1State) {
    led1State = !led1State;
    digitalWrite(led1Pin, led1State);
  }

  if (switch2State != led2State) {
    led2State = !led2State;
    digitalWrite(led2Pin, led2State);
  }

  
  delay(10);
}
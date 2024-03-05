
#include <stdio.h>

#define ssid "SUNBEAM"
#define password "1010101010"

#define switch1Pin D0
#define switch2Pin D1
#define led1Pin D2
#define led2Pin D3


int switch1State = 0;
int switch2State = 0;
int led1State = 0;
int led2State = 0;

void setup() {
  printf("Initializing...\n");

  
  pinMode(switch1Pin, INPUT_PULLUP);
  pinMode(switch2Pin, INPUT_PULLUP);

  
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);

  
}

void loop() {
  // Read switch states
  switch1State = digitalRead(switch1Pin) == LOW;
  switch2State = digitalRead(switch2Pin) == LOW;

  // Toggle LED states based on switch states
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
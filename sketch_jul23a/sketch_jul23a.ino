int fanPin = 9; // PWM pin connected to MOSFET gate

void setup() {  //setup() is called once when the program starts.
  pinMode(fanPin, OUTPUT);   // pinMode(fanPin, OUTPUT); sets the fanPin as an output pin to control the fan.
  Serial.begin(9600); // Set up serial communication
}

void loop() {   // loop() runs repeatedly.
  if (Serial.available() > 0) {   // Serial.available() > 0 checks if there is any data coming in through the serial port.
    int speed = Serial.read(); // Read the speed value from serial
    if (speed == '2') {
      analogWrite(fanPin, 82); // Low speed
    } else if (speed == '3') {
      analogWrite(fanPin, 164); // Medium speed
    } else if (speed == '4') {
      analogWrite(fanPin, 255); // High speed
    } else if (speed == '1') {
      analogWrite(fanPin, 0); // Turn off
    }
  }
}

// this code reads fan speed commands via the serial port and adjusts the fan's speed accordingly using PWM.

// This Arduino program controls the speed of a fan using PWM on pin 9, which is connected to a MOSFET. In the setup(), it initializes the fan pin as an output and sets up serial communication. In the loop(), it checks if there is incoming data from the serial port. Based on the received value ('1' to '4'), it adjusts the fan speed using analogWrite() to set different PWM values: '2' for low, '3' for medium, '4' for high, and '1' to turn off the fan.
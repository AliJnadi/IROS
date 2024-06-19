#include<Servo.h> // Servo library

Servo my_servo; // Declare servo device

#define Pot A0
#define Servo_pin 2

void setup() {
  // put your setup code here, to run once:
  pinMode(Pot, INPUT);
  pinMode(Servo_pin, OUTPUT);

  Serial.begin(115200);
  Serial.println("Program Start");

  my_servo.attach(Servo_pin); // Attach servo to a specific pin
  my_servo.write(0); // Send the desired position 0 degree

  delay(500); // Delay 500 ms
}

void loop() {
  // put your main code here, to run repeatedly:
  int Pot_val = analogRead(Pot);                // reads the value of the potentiometer (value between 0 and 1023)  

  Serial.print("Pot value = "); Serial.println(Pot_val);
  Pot_val = map(Pot_val, 0, 1023, 0, 180);      // scale it for use with the servo (value between 0 and 180)
  Serial.print("Servo value = "); Serial.println(Pot_val);

  my_servo.write(Pot_val);                     // sets the servo position according to the scaled value
  delay(15);                                   // waits for the servo to get there
}
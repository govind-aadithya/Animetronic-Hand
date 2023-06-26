#include <Wire.h>
#include <Servo.h>
#include <MPU6050.h>

MPU6050 mpu;
Servo servo;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  mpu.initialize();
  servo.attach(9); // Connect the servo signal wire to pin 9
}

void loop() {
  // Read yaw angle from MPU-6050
  int16_t gyroYaw = mpu.getRotationY();

  // Convert yaw angle to servo position
  int servoPos = map(gyroYaw, -32768, 32767, 0, 180);

  // Constrain servo position within range
  servoPos = constrain(servoPos, 0, 180);

  // Set servo position
  servo.write(servoPos);

  // Print yaw angle and servo position
  Serial.print("Yaw angle: ");
  Serial.print(gyroYaw);
  Serial.print("  Servo position: ");
  Serial.println(servoPos);

  delay(10); // Adjust delay as needed
}
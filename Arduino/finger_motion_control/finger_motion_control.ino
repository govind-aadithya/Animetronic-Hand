// str(mapped[0][0]) + ',' + str(mapped[1][0]) + ',' + str(mapped[2][0]) + ',' + str(mapped[3][0]) + ',' + str(mapped[4][0]) + '\n'
// To collect the data from the computer
// Decode the string
// send it to servo 

#include <Servo.h>

Servo servo[5];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo[0].attach( 9);
  servo[1].attach(10);
  servo[2].attach(11);
  servo[3].attach(12);
  servo[4].attach(13);
}

String digit[5];
int delimiter[5];

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 2){
    String readString = Serial.readStringUntil('\n');
    
    int j = readString.indexOf('\\');
    readString.remove(j);
    
    //Serial.println(readString+String(j));
    delimiter[0] = readString.indexOf(',');
    digit[0] = readString.substring(0,delimiter[0]);
    servo[0].write(digit[0].toInt());
    for(int i = 1; i <= 4; i++){
      delimiter[i] = readString.indexOf(",",delimiter[i-1]+1);
      Serial.println(delimiter[i]);
      digit[i] = readString.substring(delimiter[i-1]+1,delimiter[i]);
      servo[i].write(digit[i].toInt());
    }
	//Serial.println(String(digit[0])+" "+String(digit[1])+" "+String(digit[2])+" "+String(digit[3])+" "+String(digit[4]));
  }
}

#include <Wire.h>
#include "Adafruit_TCS34725.h"


//initialize the RGB sensor class
Adafruit_TCS34725 sensor = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_700MS, TCS34725_GAIN_1X);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  if(sensor.begin()){
    Serial.println("Successful connection");
    
  }
  else{
    Serial.println("Did not find sensor");
  }
  

}

void loop() {
  // put your main code here, to run repeatedly:
  uint16_t r,g,b,c;

  sensor.getRawData(&r,&g,&b,&c);
  Serial.print(r);Serial.print(",");Serial.print(g);Serial.print(',');Serial.print(b);
  Serial.print(",");Serial.print(c);

}

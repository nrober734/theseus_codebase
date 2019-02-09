void setup() {
  pinMode(11,INPUT);
  pinMode(3,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  digitalWrite(3,HIGH);
  int rec = digitalRead(11);
  digitalWrite(3,LOW);
  int rec2 = digitalRead(11);
  Serial.println(rec);
  Serial.println(rec2);

}

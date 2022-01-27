long sensor1;
long sensor2;
long sensor3;

void setup() {
  Serial.begin(9600);
}

void loop() {
 sensor1 = random(10,20);
 sensor2 = random(20,30);
 sensor3 = random(30,40);  
  Serial.print(sensor1);
  Serial.print(",");
  Serial.print(sensor2);
  Serial.print(",");
  Serial.print(sensor3);
  Serial.println();
  delay(100);
}

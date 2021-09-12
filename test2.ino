void setup() {
 Serial.begin(9600);
}

void loop() {

 while (Serial.available() > 0)
 {
  int namba;
  
  String trigger = (Serial.readString());
  if(trigger == "1"){
    digitalWrite(8, 1);
    Serial.println("Turn on!");
    }
  else if(trigger == "0"){
    digitalWrite(8, 0);
    Serial.println("Turn off!");
    }
  }
 
}

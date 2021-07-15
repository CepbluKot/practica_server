
void setup() {
 Serial.begin(9600);
}

void loop() {

 while (Serial.available() > 0)
 {
  int namba;
  
  String num = Serial.readString();
  for(int x = 0 ; x < num.length(); x++){
    if (num[x] == ' ' ) {
      namba = num[x+1] - '0';
      }
    }
  Serial.println(namba);
  
 } 
 
}

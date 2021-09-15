#include <Wire.h> // библиотека для управления устройствами по I2C 
#include <LiquidCrystal_I2C.h> // подключаем библиотеку для QAPASS 1602

LiquidCrystal_I2C LCD(0x27,16,2); // присваиваем имя LCD для дисплея

void setup() {
   LCD.init(); // инициализация LCD дисплея
   LCD.backlight(); // включение подсветки дисплея
   
   
}

void loop() {
  String trigger;
  while (Serial.available() > 0)
 {
  LCD.setCursor(1, 0);
  String trigger = (Serial.readString());
  
  Serial.println("Done!");
  }
   LCD.print(trigger);
}

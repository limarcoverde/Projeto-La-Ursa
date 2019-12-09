char serialData;
int pin=13;
int btn = 12;
int botao = 0;
int cont = 0;

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3f,2,1,0,4,5,6,7,3, POSITIVE);

void setup() {
  pinMode(pin,OUTPUT);
  pinMode(btn, INPUT_PULLUP);
  Serial.begin(9600);
  lcd.begin (16,2);
}

void loop() {
  
  botao = digitalRead(btn);
  Serial.println(botao);
  if (cont == 0){
        lcd.setBacklight(HIGH);
        lcd.setCursor(0,0);
        lcd.print("voce tem:");
        lcd.setCursor(10,0);
        lcd.print(cont);
        lcd.setCursor(0,1);
        lcd.print("notificacoes");
        delay(2000);
      }
      
  if(Serial.available()>0){
    serialData = Serial.read();
    Serial.print(serialData);
    
    if (serialData == '1'){
      digitalWrite(pin,HIGH);
      tone(11,262,1000);
      delay(1500);
      tone(11,262,1000);

      cont = cont + 1;
      
      if (cont == 1){
        lcd.setBacklight(HIGH);
        lcd.setCursor(0,0);
        lcd.print("voce tem:");
        lcd.setCursor(10,0);
        lcd.print(cont);
        lcd.setCursor(0,1);
        lcd.print("notificacao ");
        delay(2000);
      }
       if (cont >= 2){
        lcd.setBacklight(HIGH);
        lcd.setCursor(0,0);
        lcd.print("voce tem:");
        lcd.setCursor(10,0);
        lcd.print(cont);
        lcd.setCursor(0,1);
        lcd.print("notificacoes");
        delay(2000);
      }
      
      
  }
 }
 if (botao == 0){
      digitalWrite(pin,LOW);
      cont = 0;
    }
}

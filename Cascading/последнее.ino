#include <SoftwareSerial.h>
#include <Wire.h>

SoftwareSerial mySerial(10, 11);

int pins[7]={8,7,6,5,4,3,2};

byte numbers[10] = { B11111100, B01100000, B11011010, B11110010, B01100110,
B10110110, B10111110, B11100000, B11111110, B11110110};


void setup() {
  Serial.begin(9600);
  for(int i=0;i<10;i++)
    pinMode(pins[i],OUTPUT);
}

int number = 0;

void loop() {
  if (Serial.available() == 2){
    int numb = Serial.parseInt();
    int first=numb/10;
    int second=numb%10;
    Serial.println(first);
    for(int i=0;i<10;i++)
    {
      if (first==i){
        Serial.println(first);
        number=i;
        showNumber(number);
      }
    }
  }
}

void showNumber(int f)
{
  Serial.println(f);
  for(int i=0;i<7;i++)
  {
    if(bitRead(numbers[f],7-i)==HIGH) // зажечь сегмент
    digitalWrite(pins[i],HIGH);
    else // потушить сегмент
    digitalWrite(pins[i],LOW);
  } 
}
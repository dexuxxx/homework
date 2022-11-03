#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11);
void setup() {
Serial.begin(9600);
while (!Serial) { }
Serial.println("...");
mySerial.begin(9600);
mySerial.println("...");
}
void loop() {
if (mySerial.available())
 Serial.write(mySerial.read());
if (Serial.available())
 mySerial.write(Serial.read());
}

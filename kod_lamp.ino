#define sensor_pin A2
#define led_pin 3
void setup() {
Serial.begin(9600);
pinMode(led_pin, OUTPUT);
}

void loop() {
int val = analogRead(sensor_pin);
Serial.println(val);
delay(10);
if (val < 850){
digitalWrite(led_pin, HIGH); // turn the LED on (HIGH is the voltage level)
delay(100);
}
else{
digitalWrite(led_pin, LOW); // turn the LED off by making the voltage LOW
delay(100);
}
// wait for a second

}
#define sensor_pin A3

long interval = 900;
long start;

void setup() {
  pinMode(sensor_pin, INPUT);
  Serial.begin(9600);
  start = millis();
}

void loop() {
  if (Serial.available() >= 2){
    if (Serial.read() == 'I'){
      interval = long(Serial.read());
    }
  }
  long time = millis() - start;
  if (time >= interval){
    char value = analogRead(sensor_pin) / 1024.0 * 101;
    Serial.write(value);
    start = millis();
  }
}
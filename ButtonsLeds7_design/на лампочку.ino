#define btn_pin 7
#define led_pin 3
#define check_time 20
#define toogle_time 1000

long prev = 0;
int pwr = 0;
bool pwr_mode = false;
bool mode;
bool pwr_on = false;

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
  pinMode(btn_pin, INPUT);
}

void loop() {
  int val = digitalRead(btn_pin);
  if (val == 1){
    if (millis()-prev > check_time){
      mode = true;
      if (millis()-prev > toogle_time){
        mode = false;
        pwr_on = true;
        if (pwr_mode) {
          pwr += 1;
          if (pwr >= 255) {
            pwr_mode = false;
          }
        } else {
          pwr -= 1;
          if (pwr <= 0) {
            pwr_mode = true;
          }
        }
        Serial.println(pwr);
        analogWrite(led_pin, pwr);
      }
    }
  } else {
    prev = millis();
  	if (mode) {
      if (pwr_on) {
        pwr_on = false;
        analogWrite(led_pin, 0);
        pwr = 0;
      } else {
        pwr_on = true;
        analogWrite(led_pin, 255);
        pwr = 255;
      }
      pwr_mode = !pwr_on;
      mode = false;
    }
  }
}

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("EWA ONLINE");
}

void loop() {

  if (Serial.available()) {

    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    Serial.print("CMD:");
    Serial.println(cmd);

  }

}
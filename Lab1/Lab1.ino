

String inputString = "";      
bool isStringComplete = false;  

void setup() {
  // initialize serial:
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (isStringComplete) {
    //TODO: Do the command!
    if(inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("The LED is now on!");
    } else if(inputString.equals("LED OFF")){
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("The LED is now off!");
    } else {
      Serial.print("Unknown command -->");
      Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}

// Serial event only called when there's bites available
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read(); //cast to char (unsigned 8-bit int)
    if (inChar == '\n') {
      isStringComplete = true;
    } else { 
      inputString += inChar;
    }
  }
}

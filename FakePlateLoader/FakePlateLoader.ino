

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
    if(inputString.equals("RESET")) {
      delay(500);
      Serial.println("READY, SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
    } else if(inputString.startsWith("MOVE")){ //.startsWith = similar to .equals
      delay(3000);
      Serial.println("READY");
    
    } else if(inputString.equals("GRIPPER OPEN")) {
      delay(3000);
      Serial.println("GRIPPER OPENED");
    } else if(inputString.equals("GRIPPER CLOSE")) {
      delay(3000);
      Serial.println("GRIPPER CLOSED");
    
    } else if(inputString.equals("EXTEND")) {
      delay(3000);
      Serial.println("Z-AXIS EXTENDED");
    } else if(inputString.equals("RETRACT")) {
      delay(3000);
      Serial.println("Z-AXIS RETRACTED");
    
    } else if(inputString.startsWith("X-AXIS")) {
      delay(3000);
      Serial.println("READY");
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

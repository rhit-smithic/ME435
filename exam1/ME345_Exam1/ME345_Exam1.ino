

String inputString = "";      
bool isStringComplete = false;  

int flashes = 0;
int period = 0;

void setup() {
  // initialize serial:
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (isStringComplete) {
    //LED ON
    if(inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      Serial.println("LED On");
    
    //LED OFF
    } else if(inputString.equals("LED OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      delay(100);
      Serial.println("LED Off");
    
    //FLASHES PERIOD (ms)
    } else if(inputString.startsWith("FLASH")){ 
      int input1 = inputString.indexOf(' '); //use indexOf to retrieve input location
      int input2 = inputString.indexOf(' ', input1 + 1);
      flashes = inputString.substring(input1 + 1, input2).toInt(); //and theeen specify substring and convert to int
      period = inputString.substring(input2 + 1).toInt();
      
      for (int i = 0; i < flashes; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(period / 2);
        digitalWrite(LED_BUILTIN, LOW);
        delay(period / 2);
      }
    
    Serial.print("Flashes = ");
    Serial.print(flashes);
    Serial.print("    PeriodMs = ");
    Serial.println(period);
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

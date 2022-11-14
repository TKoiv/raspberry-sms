int RELAY_PIN1 = 3;
int RELAY_PIN2 = 5;

int OHJ1 = 0;
int OHJ2 = 0;

int Data = 0;

int DataInt = 0;

int buttonPin1 = 7;     // Lock's open pin

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN1, OUTPUT);
  pinMode(RELAY_PIN2, OUTPUT);

  pinMode(buttonPin1, INPUT);
  
  

}

void loop() {

    if (Serial.available()>0){
    String Data = Serial.readString();
    Serial.print("You sent me: ");
    Serial.println(Data);
    DataInt = Data.toInt();
}
    /*int buttonState1 = 0;
    buttonState1 = digitalRead(buttonPin1);
  while (buttonState1 == HIGH and DataInt == 0){
      digitalWrite(RELAY_PIN1, HIGH);
      digitalWrite(RELAY_PIN2, HIGH);
      Serial.println("While loopissa ollaan");
      Serial.println(DataInt);
      if (DataInt != 0){
        break; 
      }
  }
*/

  

  //DataInt = Data.toInt();
  Serial.print("DataInt on:" );
  Serial.println(DataInt);

  switch (DataInt){
    case 0:
      digitalWrite(RELAY_PIN1, LOW);
      digitalWrite(RELAY_PIN2, LOW);
      Serial.println("Case 0");
      break;
    case 1:
      digitalWrite(RELAY_PIN1, HIGH);
      digitalWrite(RELAY_PIN2, HIGH);
      Serial.println("Case 1");
      delay(5000);
      DataInt = 2;
      break;
    case 2:
      digitalWrite(RELAY_PIN1, HIGH);
      digitalWrite(RELAY_PIN2, LOW);
      Serial.println("Case 2");
      break;
    case 3:
      digitalWrite(RELAY_PIN1, HIGH);
      digitalWrite(RELAY_PIN2, HIGH);
      Serial.println("Case 3");
      break;
    
  }


}

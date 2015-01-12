/*
Serial communication for the Giant Atom Manipulator for Education (GAME project)
Author: Jesus Martinez-Blanco
Date: May 2014
*/
int sensorIN = 1;       // IRsensor on Analogue Pin 1
int aiValue = 0;       // input value
int values;

void setup()
{
  Serial.begin(9600);
}

void loop() {
  
  // if there's any serial available, read it:
  if (Serial.available() > 0) {
    
    if (Serial.read() == 32) { //space has been sent, so read a line with ppl points
             
      for (int i=0; i < 64; i++){
        
        values = analogRead(sensorIN);
//        Serial.write(values);
        Serial.print(values);
        Serial.print(";");
        delay(20);

         
      } 
      
     Serial.print("\r");     
   //  aiValue = analogRead(sensorIN);    // Read the analogue input value
   //  Serial.println(aiValue);
    }
    
  }

}


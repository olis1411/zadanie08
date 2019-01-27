## Czujnik temperatury, który jeśli wykryje ( ustawimy ) temp. większą niż 30*C Ostrzeże nas, że jest zbyt gorąco

float temp;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  temp = analogRead(A0);
  temp = (temp * 0.48828125)-50.78;
  if (temp > 30){
    Serial.print("za goraco");
	Serial.println();
  }
  else{
  		Serial.print("Temperatura otoczenia to");
  		Serial.print(temp);
  		Serial.print("*C");
  		Serial.println();
  }
    delay(500);
}

## Czujnik odleglosci, który tylko w przedziale 755-800mm mówi, że jesteśmy w dobrym miejscu. W przeciwnym razie informuje, że jesteśmy zbyt blisko lub zbyt daleko
int punkt1 = 0;
int dystans = 0;

void setup(){
Serial.begin(9600);
        pinMode(A0, INPUT);
}

void loop(){
    punkt1 = analogRead (A0);
    dystans = ((67870 / (punkt1 - 3)) - 40);
    if (dystans > 800){
        Serial.println("Odszedles za daleko");
      	Serial.print(punkt1);
    }
     if (dystans < 755){
        Serial.println("Podszedles za blisko");
       	Serial.print(punkt1);
    }
    else{
        Serial.print ("Stoisz w dobrym miejscu");
      	Serial.print(punkt1);
        Serial.println();
    }
    delay (500);
}
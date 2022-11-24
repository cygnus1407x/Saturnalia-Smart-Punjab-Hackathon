#define R1 2
#define G1 3
#define R2 4
#define G2 5
#define R3 6
#define G3 7
#define R4 8
#define G4 9
#define ech 10
#define trig 11
#define del 5000

int ini;
int timee;
void setup()
{
  pinMode(R1, OUTPUT);
  pinMode(G1, OUTPUT);
  pinMode(R2, OUTPUT);
  pinMode(G2, OUTPUT);
  pinMode(R3, OUTPUT);
  pinMode(G3, OUTPUT);
  pinMode(R4, OUTPUT);
  pinMode(G4, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(ech, INPUT);

  Serial.begin(9600);

  digitalWrite(trig,LOW);
  delay(100);
  digitalWrite(trig,HIGH);
  delay(100);
  digitalWrite(trig,LOW);
  
  
  timee=pulseIn(ech,HIGH);
  ini=timee*0.034/2;
  // int ini=2900;
  Serial.println("INITIAL: ");
  Serial.print(ini);
 }

int ser;

void loop()
{
  int dist;
  long time;
 
   
  ser=1;

  switch(ser)
  {
    case 1:
    digitalWrite(G1, HIGH);
    digitalWrite(R2,HIGH);
    digitalWrite(R3,HIGH);
    digitalWrite(R4,HIGH);
    digitalWrite(trig, LOW);
   delay(100);
   digitalWrite(trig, HIGH);
   delay(100);
   digitalWrite(trig, LOW);

   time=pulseIn(ech,HIGH);
   dist= time *0.034/2;

   Serial.println("DISTANCE: ");

   Serial.print(dist);
   Serial.print("\n");

    if (dist<ini-50)
    {
      digitalWrite(R1, HIGH);
      digitalWrite(G1, LOW);
      delay(5000);
      digitalWrite(R1,LOW);
    }else {
      digitalWrite(R1,LOW);
      digitalWrite(G1,HIGH);
    }
    break;

    case 2:
    digitalWrite(G2, HIGH);
    digitalWrite(R1,HIGH);
    digitalWrite(R3,HIGH);
    digitalWrite(R4,HIGH);
    delay(del+5000);
    break;

    case 3:
    digitalWrite(G3, HIGH);
    digitalWrite(R2,HIGH);
    digitalWrite(R3,HIGH);
    digitalWrite(R4,HIGH);
    delay(del+5000);
    break;

    case 4:
    digitalWrite(G4, HIGH);
    digitalWrite(R2,HIGH);
    digitalWrite(R3,HIGH);
    digitalWrite(R1,HIGH);
    delay(del+5000);
    break;
    }  
   
}

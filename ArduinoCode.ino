#include <NewPing.h>

// Sonar Ports
#define SonarLeftEcho 13
#define SonarLeftTrig 12

#define SonarRightEcho 8
#define SonarRightTrig 7

#define SonarFrontEcho 4
#define SonarFrontTrig 2

// Motor Ports
//#define motorSpeedLeft A4
//#define motorSpeedRight A3

//#define motorDirLeft 6
//#define motorDirRight 5

// Variables initialisation
int SonarLeftVal = 0;
int SonarRighttVal = 0;
int SonarFrontVal = 0;

//int motorSpdL = 0;
//int motorSpdR = 0;

// defining motor terminals
int motRightIn1 = 10;
int motRightIn2 = 9;
int En1 = 11;

int motLeftIn1 = 6;
int motLeftIn2 = 5;
int En2 = 3;

int maxPing = 20;         // minimum distance between sensor and wall

NewPing SonarLeft(SonarLeftTrig, SonarLeftEcho, maxPing);
NewPing SonarRight(SonarRightTrig, SonarRightEcho, maxPing);
NewPing SonarFront(SonarFrontTrig, SonarFrontEcho, maxPing);


void Reset() {
    digitalWrite(motorDirLeft, LOW);
    digitalWrite(motorDidRight, LOW);
    analogWrite(motorSpeedLeft, 0);
    analogWrite(motorSpeedRight, 0);
    delay(10);
}

void ReadSensor() {
  delay(5);
  
  sonarLeftVal = SonarLeft.ping.cm();
  if(sonarLeft.check_timer() == 0) sonarLeftVal = maxPing;
  delay(5);

  sonarRightVal = SonarRight.ping.cm();
  if(sonarRight.check_timer() == 0) sonarRightVal = maxPing;
  delay(5);

  sonarFrontVal = SonarFront.ping.cm();
  if(sonarFront.check_timer() == 0) sonarFrontVal = maxPing;
  delay(5); 
}

void forward(){
    digitalWrite(motRightIn1, HIGH);
    digitalWrite(motRightIn2, LOW);
    digitalWrite(motLeftIn1, LOW);
    digitalWrite(motLeftIn2, HIGH);
}

void left(){
    digitalWrite(motRightIn1, HIGH);
    digitalWrite(motRightIn2, LOW);
    digitalWrite(motLeftIn1, LOW);
    digitalWrite(motLeftIn2, LOW);
}

void right(){
    digitalWrite(motRightIn1, LOW);
    digitalWrite(motRightIn2, LOW);
    digitalWrite(motLeftIn1, LOW);
    digitalWrite(motLeftIn2, HIGH);
}

void stop(){
    digitalWrite(motRightIn1, LOW);
    digitalWrite(motRightIn2, LOW);
    digitalWrite(motLeftIn1, LOW);
    digitalWrite(motLeftIn2, HIGH);
    delay(1000);
}

void AvoidWalls(){
  
}


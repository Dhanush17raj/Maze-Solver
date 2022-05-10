#include <NewPing.h>

// Sonar Ports
#define SonarLeftEcho 13
#define SonarLeftTrig 12

#define SonarRightEcho 8
#define SonarRightTrig 7

#define SonarFrontEcho 4
#define SonarFrontTrig 3

// Motor Ports
#define motorSpeedLeft A4
#define motorSpeedRight A3

#define motorDirLeft 6
#define motorDirRight 5

// Variables initialisation
int SonarLeftVal = 0;
int SonarRighttVal = 0;
int SonarFrontVal = 0;

int motorSpdL = 0;
int motorSpdR = 0;

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



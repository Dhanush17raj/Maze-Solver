#include <NewPing.h>

// Sonar Ports
#define SonarLeftEcho 13
#define SonarLeftTrig 12

#define SonarRightEcho 8
#define SonarRightTrig 7

#define SonarFrontEcho 4
#define SonarFrontTrig 3

// Motor Ports
#define motorSpeedLeft 10
#define motorSpeedRight 11

#define motorDirLeft 6
#define motorDirRight 5

// Variables initialisation
int SonarLeftVal = 0;
int SonarRighttVal = 0;
int SonarFrontVal = 0;

int motorSpdL = 0;
int motorSpdR = 0;

int maxPing = 20;         // minimum distance between sensor and wall


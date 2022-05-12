#include <NewPing.h>

int motor_lA = 9;
int motor_lB = 10;
int motor_enableA = 11;

int motor_rA = 3;
int motor_rB = 4;
int motor_enableB = 5;

int trigger_front = A0;
int echo_front = A1;

int trigger_left = A2;
int echo_left = A3;

int trigger_right = A4;
int echo_right = A5;


void setup() {
  // put your setup code here, to run once:
  pinMode(motor_lA,OUTPUT);   //left motors forward
  pinMode(motor_lB,OUTPUT);   //left motors reverse
  pinMode(motor_enableA, OUTPUT);

  pinMode(motor_rA,OUTPUT);   //right motors forward
  pinMode(motor_rB,OUTPUT);   //rignt motors reverse
  pinMode(motor_enableB, OUTPUT);

  pinMode(trigger_front,OUTPUT);
  pinMode(echo_front,INPUT);

  pinMode(trigger_left,OUTPUT);
  pinMode(echo_left,INPUT);

  pinMode(trigger_right,OUTPUT);
  pinMode(echo_right,INPUT);
  
  analogWrite(motor_enableA, 80);
  analogWrite(motor_enableB, 88);

}

void loop(){
  long distance_front, distance_right, distance_left;
  
  distance_front = sonar(trigger_front, echo_front);
  distance_left = sonar(trigger_left, echo_left);
  distance_right = sonar(trigger_right, echo_right);
  
  //Serial.print("front = ");
  //Serial.println(distance_front);
  //Serial.print("Left = ");
  //Serial.println(distance_left);
  //Serial.print("Right = ");
  //Serial.println(distance_right);  
  //delay(50);
  
  if (distance_front >20){
    forward();
    if(distance_left > 10&& distance_left<20){
      forward();
    }
    if(distance_left >=20){
       left();
       delay(30);
       forward();
    }
    if(distance_left<10 && distance_left>0){
      right();
      delay(30);
      forward();
    }
 } 
  
  if(distance_front<=20&& distance_right > 20){
    Stop();
    delay(1000);
    right();
    delay(400);
    
  }

  if(distance_front<=20 && distance_right<20){
    Stop();
    delay(1000);
    right();
    delay(800);
   
  }
}

long sonar(int trigger, int echo){
  long duration, distance;
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  duration = pulseIn(echo, HIGH);
  distance = duration*0.034/2;
  return distance;
}

void forward(){
  digitalWrite(motor_lA,1);
  digitalWrite(motor_lB,0);
  digitalWrite(motor_rA,1);
  digitalWrite(motor_rB,0);
  delay(1000);
}


void right(){
  digitalWrite(motor_lA,1);
  digitalWrite(motor_lB,0);
  digitalWrite(motor_rA,0);
  digitalWrite(motor_rB,1);
 delay(10);
}


void left(){
  digitalWrite(motor_lA,0);
  digitalWrite(motor_lB,1);
  digitalWrite(motor_rA,1);
  digitalWrite(motor_rB,0);
  delay(10);
}



void Stop(){
  digitalWrite(motor_lA,0);
  digitalWrite(motor_lB,0);
  digitalWrite(motor_rA,0);
  digitalWrite(motor_rB,0);
  delay(300);
}

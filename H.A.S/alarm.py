import datetime as dt
import time
import os
from playsound import playsound # Import playsound

ALARM_SOUND = 'alarm.mp3'

def current_time():
    current_time = dt.datetime.now().time()
    current_time=current_time.strftime("%H:%M")
    return current_time

def alarm_time():
    try:    
        alarm = input("Enter time: ")
        alarm = dt.datetime.strptime(alarm,"%H:%M").time()
        return alarm
    except Exception as e:
        print(f"Invalid Time \n {e}")
        return False
    
def snooz():
    stop = input("Enter stop or snooz: ")
    if stop.lower() =="stop":
        return True
    elif stop.lower()=="snooz":
        now = dt.datetime.now()
        future_minute = (now.minute + 1) % 60
        future_hour = now.hour if (now.minute + 1) < 60 else (now.hour + 1) % 24
        

def alarm(at=alarm_time()):
    while True:
        if at == False:
           at = alarm_time()

        elif at == current_time():
            # playsound(ALARM_SOUND)  # uncomment to play sound
            print("Time over")

            
if __name__ =="__main__":
    alarm()
    # pass
import datetime as dt
import playsound as ps

hour= int(input("enter hour\n"))
min= int(input("enter minute\n"))
time= input("enter am/pm\n")
time=time.lower()

if time=="pm":
    hour +=12 
while True:     
    if hour==dt.datetime.now().hour and min == dt.datetime.now().minute:
        ps.playsound("C:\\code\\Popular Alarm Clock Sound Effect_77S70NhRoBc.mp3")
        print("time up")
        break
from datetime import datetime
from playsound import playsound
try:
    alarm=input("Enter the alarm:HH:MM:SS\n")
    alarm_hour=alarm[0:2]
    alarm_minute=alarm[3:5]
    alarm_seconds=alarm[6:8]
    alarm_period=alarm[9:11].upper()
    print("Setting up Alarm..........")
    while True:
        now=datetime.now()
        current_hour=now.strftime("%I")
        current_minute=now.strftime("%M")
        current_seconds=now.strftime("%S")
        current_period=now.strftime("%p")
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    if(alarm_seconds==current_seconds):
                        print("Wake Up!!")
                        playsound("alarm.mp3")
                        break

except KeyboardInterrupt:
    print("you stop the alarm!!!")
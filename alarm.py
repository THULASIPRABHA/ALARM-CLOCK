import datetime
import winsound
import random
import time
from plyer import notification
alarmhour=int(input("WHAT TIME TO WAKE YOU UP?   "))
alarmminute=int(input("WHAT MINUTE DO I RING?  "))
amPm=input("am or pm ")
print("Hurray! Alarm set")
if (amPm=="pm" or amPm=="PM"):
    alarmhour =alarmhour+12
elif  (amPm == 'am' or amPm=="AM"):  
    alarmhour -= 12
else:
    pass
while True:
        if alarmhour == datetime.datetime.now().hour and alarmminute == datetime.datetime.now().minute:
            print("\nIt's the time!")
            notification.notify( 
            title = "ALARAM TIME", 
            message=" WAKEUP GO TO YOUR WORK" , app_icon="alarm.ico",
              timeout=10,
              toast=True) 
            for i in range(5):
                winsound.Beep(random.randint(37,10000), random.randint(750,3000))
            break

import schedule
import time
import datetime
import winsound
import random
from plyer import notification
def day():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    while True:
        notification.notify( title = "ALARM TIME", message=" WAKEUP GO TO YOUR WORK" , app_icon="alarm.ico",timeout=10,toast=True) 
        for i in range(5):
            winsound.Beep(random.randint(37,10000), random.randint(750,3000))
        break
def min():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    while True:
        notification.notify( title = "ALARM TIME", message="Time Is percious Make use of it " , app_icon="alarm.ico",timeout=10,toast=True) 
        break
schedule.every(1).minutes.do(min)
schedule.every(1).hour.do(min)
schedule.every(1).day.at("01:45").do(day)
while True:
    schedule.run_pending()
    time.sleep(10)

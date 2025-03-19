import time
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%I:%M:%p")

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting....")

    while True:
        current_time = get_current_time()

        if current_time == alarm_time:
            print(f"Alarm! It's {alarm_time}, Time to wake up!")
            break
        time.sleep(60)

alarm_time = input("Set alarm time (e.g., 07:30 AM): ")

set_alarm(alarm_time)
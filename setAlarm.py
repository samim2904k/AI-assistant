from dateutil import parser
from datetime import datetime, timedelta
import time
import sys
import winsound
from Body import Listen,Speak

def parse_alarm_time(alarm_string):
    try:
        if "tomorrow" in alarm_string.lower():
            alarm_string = alarm_string.replace("tomorrow", "").strip()
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            alarm_time = parser.parse(alarm_string, fuzzy=True)
            
            alarm_time += timedelta(days=1)
        else:
            alarm_time = parser.parse(alarm_string, fuzzy=True)

        current_time = datetime.now()
        if alarm_time < current_time:
            alarm_time += timedelta(days=(7 - alarm_time.weekday()))
        
        return alarm_time
    except Exception as e:
        print(f"Error: {e}")
        return None


def Main():
    user_input = str(Listen.Enzo_fun())
    alarm_time = parse_alarm_time(user_input)

    if alarm_time:
        print(f"Alarm scheduled for: {alarm_time}")
        Speak.voice_of_aiwin(f"Alarm scheduled for: {alarm_time}")
        alarm_time = str(alarm_time)
        target_time = datetime.strptime(alarm_time, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()
        time_until_target = (target_time - current_time).total_seconds()

        if time_until_target > 0:
            time.sleep(time_until_target)
            end_time = target_time + timedelta(minutes=1)
            while datetime.now() < end_time:
                print("alarm triggered")
                winsound.PlaySound('abc',winsound.SND_LOOP)
                time.sleep(1)
    sys.exit()

Main()
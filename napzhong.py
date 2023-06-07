import datetime
import time

def set_alarm(alarm_time):
    """
    Set a new alarm with the specified time in (HH:MM) format.
    """
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == alarm_time:
            print("Time's up!")
            break
        else:
            print(f"Current time is {now}. Waiting for {alarm_time}...")
        
        time.sleep(60) # Check once a minute

# Example usage of set_alarm function
set_alarm('11:15')  # Set the alarm to 11:15 AM
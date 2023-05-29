import time

def focus_timer(minutes):
    """
    Count down a timer for specified minutes
    """
    seconds = minutes * 60
    start = time.time()  # start time
  
    while True:
        elapsed_time = time.time() - start
        
        if elapsed_time >= seconds:
            print("Time's up!")
            break
        
        mins_left = (seconds - elapsed_time) // 60   # remaining minutes
        secs_left = (seconds - elapsed_time) % 60     # remaining seconds
        
        # display the countdown timer
        print(f"Time left: {mins_left} min {secs_left} sec")
        time.sleep(1)

# Example usage of focus_timer function
focus_timer(25)  # Set a 25-minute timer for focus session

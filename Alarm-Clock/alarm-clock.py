import time
import datetime
import os

def set_alarm(alarm_time):
    """Sets the alarm and waits until the specified time to trigger the sound."""
    print(f"Alarm set for {alarm_time}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")  # Overwrites the line for clean output
        
        if current_time == alarm_time:
            print("\nWAKE UP! 😴")
            play_alarm_sound()
            break
        
        time.sleep(1)

def play_alarm_sound():
    """Plays the alarm sound."""
    try:
        # Use the "say" command on macOS;
        os.system("say 'Alarm is ringing!'")
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format! Please enter the time in HH:MM:SS format.")
    else:
        set_alarm(alarm_time)

import time
import datetime
import os


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

def play_alarm_sound():
    os.system("say 'Alarm is ringing!'")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

        time.sleep(1)

play_alarm_sound()

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
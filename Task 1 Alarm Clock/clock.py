import time
import platform


def set_alarm(hour, minute, am_pm):
    # Convert 12-hour format to 24-hour format
    if am_pm.upper() == "PM" and hour != 12:
        hour += 12
    elif am_pm.upper() == "AM" and hour == 12:
        hour = 0

    # Get the current time
    current_time = time.localtime()

    # Set the alarm time
    alarm_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                   hour, minute, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))

    # Calculate the time difference until the alarm
    time_diff = time.mktime(alarm_time) - time.mktime(current_time)

    # Sleep until the alarm time
    if time_diff > 0:
        print(f"Alarm set for {hour:02}:{minute:02} {am_pm.upper()}")
        time.sleep(time_diff)
        print("Alarm ringing...")
        play_alarm_sound(duration=10)  # Set the duration to 10 seconds
    else:
        print("Invalid alarm time. Please set a future time.")


def play_alarm_sound(duration=1):
    # Play a sound based on the operating system
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000 * duration)  # For Windows, duration in milliseconds
    elif platform.system() == "Darwin":
        import subprocess
        subprocess.run(["afplay", "-t", str(duration), "/System/Library/Sounds/Ping.aiff"])  # For macOS
    elif platform.system() == "Linux":
        import os
        os.system(f"aplay -d {duration} /usr/share/sounds/alsa/Front_Center.wav")  # For Linux (requires ALSA)


if __name__ == "__main__":
    try:
        # Get user input for the alarm time
        alarm_hour = int(input("Enter the hour for Alarm between 1 to 12: "))
        alarm_minute = int(input("Enter the minute for Alarm between 0 to 59: "))
        am_pm = input("Enter AM or PM: ")

        # Set the alarm
        set_alarm(alarm_hour, alarm_minute, am_pm)

    except ValueError:
        print("1Please enter valid numbers for hour and minute.")
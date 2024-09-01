# Part 2: 24-Hour Clock Alarm

# Input: Request the current time in hours from the user and the number of hours to wait for the alarm to activate.

current_time = int(input("What is the current time in hours (0-23): "))
time_to_wait = int(input("Input the number of hours to wait for the alarm: "))

# Calculate time the alarm will go off
alarm_time = (current_time + time_to_wait) % 24

# Output: Display the alarm time
print(f"\nThe alarm will go off at: {alarm_time:02d}:00 hours")

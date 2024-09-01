# Part 2: 24-Hour Clock Alarm

# Input: Request the current time in hours from the user and the number of hours to wait for the alarm to activate.

current_time = int(input("What is the current time in hours (0-23): "))
time_to_wait = int(input("Input the number of hours to wait for the alarm: "))

# Calculate time the alarm will go off
alarm_time = (current_time + time_to_wait) % 24
# % 24 ensures that the resulting time is always within the range of 0 to 23

# Store the inputs and result in a list
time_data = [current_time, time_to_wait, alarm_time]

# Output: Display the alarm time using the list
print(f"\nCurrent Time: {time_data[0]:02d}:00 hours")
print(f"Wait Time: {time_data[1]} hours")
print(f"The alarm will go off at: {time_data[2]:02d}:00 hours")

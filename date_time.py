# import datetime

# x = datetime.datetime.now()

# # print(x.year)
# # print(x.time())
# print(x.strftime("%I:%M:%S %p"))




import time
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

while True:
    # Clear the screen
    clear_screen()
    
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Format the time
    formatted_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    
    # Print the time
    print(formatted_time)
    
    # Wait for one second before updating the time
    time.sleep(1)

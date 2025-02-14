# Write a Python program to extract year, month, date and time using Lambda

import datetime

# Get current date and time
now = datetime.datetime.now() #now named object milgya hame!
print(now) # python ne internally now naam se ek object bnadya he



# Lambda functions to extract parts
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%Ss")  # Formatting time as HH:MM:SS

# Output
print("Year:", get_year(now))
print("Month:", get_month(now))
print("Day:", get_day(now))
print("Time:", get_time(now))



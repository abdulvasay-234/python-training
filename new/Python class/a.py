# 1 # Ask the user for a number of seconds
total_seconds = int(input("Enter a number of seconds: "))

# 2 # Convert it to hours, minutes and remaining seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# 3 # Print in the format 1 hour(s), 1 minute(s), 1 second(s)
print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
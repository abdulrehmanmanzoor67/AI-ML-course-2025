# Input from user
minutes = int(input("Enter number of minutes: "))

# Convert to hours and minutes
hours = minutes // 60            # Whole hours
remaining_minutes = minutes % 60  # Remaining minutes

# Output the result
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")

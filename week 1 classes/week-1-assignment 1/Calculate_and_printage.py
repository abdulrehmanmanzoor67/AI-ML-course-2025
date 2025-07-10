# Age in Months, Days, Hours, and Minutes

# Input from user
age_years = int(input("Enter your age in years: "))

# Calculations
age_months = age_years * 12
age_days = age_years * 365       # Approximate
age_hours = age_days * 24
age_minutes = age_hours * 60

# Output
print("Age in Months: ", age_months)
print("Age in Days: ", age_days)
print("Age in Hours: ", age_hours)
print("Age in Minutes: ", age_minutes)

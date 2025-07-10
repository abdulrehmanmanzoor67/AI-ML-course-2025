# Input: Basic Salary
basic_salary = float(input("Enter basic salary: "))

# Calculate HRA (20% of basic)
hra = 0.20 * basic_salary

# Calculate DA (15% of basic)
da = 0.15 * basic_salary

# Calculate Total Salary
total_salary = basic_salary + hra + da

# Output
print("HRA =", hra)
print("DA =", da)
print("Total Salary =", total_salary)

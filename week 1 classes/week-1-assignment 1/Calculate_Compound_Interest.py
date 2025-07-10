# User input lena
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time in years: "))
n = int(input("Enter number of times interest applied per year: "))

# Compound Interest formula:
# A = P * (1 + R/n)^(n*T)
# CI = A - P

amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

# Result print karna
print("Compound Interest is:", round(compound_interest, 2))
print("Total Amount after interest:", round(amount, 2))

# Currency Converter: USD to PKR

# Fixed exchange rate (example: 1 USD = 278 PKR)
exchange_rate = 278

# Input amount in USD
usd_amount = float(input("Enter amount in USD: "))

# Convert to PKR
pkr_amount = usd_amount * exchange_rate

# Output
print("USD amount in PKR:", pkr_amount)

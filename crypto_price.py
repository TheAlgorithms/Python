# Let's assume 1 ETH = 2500 USD (you can change this number)
eth_price_usd = 2500  

print("=== ETH to USD Converter ===")

# Ask user for ETH amount
eth_amount = float(input("Enter amount of ETH: "))

# Convert to USD
usd_value = eth_amount * eth_price_usd

# Show result
print(f"{eth_amount} ETH = ${usd_value} USD")

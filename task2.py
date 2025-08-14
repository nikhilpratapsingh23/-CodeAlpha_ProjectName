# Stock Portfolio Tracker - CodeAlpha Internship Task 2

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print(" Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices (USD):")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter your stock holdings (type 'done' to finish):")

# Taking user input
while True:
    stock_name = input("Enter stock symbol: ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print(" Stock not available in the list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print(" Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
print("\n Your Portfolio Summary:")
for stock, qty in portfolio.items():
    investment = qty * stock_prices[stock]
    total_investment += investment
    print(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${investment}")

print(f"\n Total Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save_choice == "yes":
    file_name = "portfolio_summary.txt"
    with open(file_name, "w") as file:
        file.write(" Portfolio Summary\n")
        for stock, qty in portfolio.items():
            investment = qty * stock_prices[stock]
            file.write(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${investment}\n")
        file.write(f"\n Total Investment Value: ${total_investment}\n")
    print(f"Summary saved to {file_name}")

print(" Thank you for using Stock Portfolio Tracker!")



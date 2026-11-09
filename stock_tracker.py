STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dictionary."""
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Type 'done' when finished.\n")

    while True:
        name = input("Stock symbol: ").upper().strip()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not found. Try again.\n")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Enter a whole number greater than 0.\n")
            continue

        portfolio[name] = portfolio.get(name, 0) + int(qty_text)
        print(f"Added {qty_text} x {name}\n")

    return portfolio


def calculate_total(portfolio):
    """Return the total value and a list of text lines for each holding."""
    total = 0
    lines = []
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        lines.append(f"{name}: {qty} x ${STOCK_PRICES[name]} = ${value}")
    return total, lines


def save_result(lines, total, filename="portfolio_result.txt"):
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write("-" * 30 + "\n")
        for line in lines:
            f.write(line + "\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total investment: ${total}\n")
    print(f"Result saved to {filename}")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered.")
        return

    total, lines = calculate_total(portfolio)

    print("\n--- Portfolio Summary ---")
    for line in lines:
        print(line)
    print(f"Total investment: ${total}")

    save = input("\nSave result to a file? (y/n): ").lower().strip()
    if save == "y":
        save_result(lines, total)


if __name__ == "__main__":
    main()

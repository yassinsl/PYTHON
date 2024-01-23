def max_price(bid_1):
    if not bid_1:
        print("No bids available.")
        return None

    max_bid = max(bid_1.values())
    
    for name, price in bid_1.items():
        if price == max_bid:
            print(f"The highest bid is from {name} with a price of {price}")

    return max_bid

# Example usage:
bid_1 = {'John Doe': 100, 'Alice Smith': 150, 'Bob Johnson': 120}
max_bid = max_price(bid_1)
print(f"The maximum bid is: {max_bid}")

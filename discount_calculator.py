# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        # No discount applied
        return price

# Ask the user for the original price
original_price_input = input("Enter the original price of the item: ")
original_price = float(original_price_input)

# Ask the user for the discount percentage
discount_input = input("Enter the discount percentage: ")
discount_percent = float(discount_input)

# Use the function to calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied. Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {original_price}")

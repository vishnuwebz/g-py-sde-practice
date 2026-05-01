# variable initialization
product_name = "Gaming Mouse"
price = 79.99
quantity = 2
in_stock = True

# calculation
total_cost = price * quantity

# Logical and Relational operator to check if an order is priority order
is_priority = total_cost > 100 and in_stock

# order summary
print(f"Order Summary: {quantity} x {product_name} @ ${price}. Total: {total_cost}. Priority Order: {is_priority}")


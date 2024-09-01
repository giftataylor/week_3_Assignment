# Part 1: Meal Cost Calculation with Lists

# Input: Request the food charge from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Store results in a list
costs = [food_charge, tip, tax, total]

# Display the results using the list
print(f"\nFood Charge: ${costs[0]:.2f}")
print(f"Tip (18%): ${costs[1]:.2f}")
print(f"Tax (7%): ${costs[2]:.2f}")
print(f"Total Amount: ${costs[3]:.2f}")

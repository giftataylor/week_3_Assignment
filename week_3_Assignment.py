# Part 1: Meal Cost Calculation

# Input: Request the food charge from the user
food_charge = float(input("Enter the charge for the food: $"))

#Calculate tip and tax and total
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Output:Display the food charge, tip amount, tax amount, and total amount 
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")

"""
Program Name: Restaurant Tip Calculator
Author: Kaleb Quinn
Purpose: This program calculates tips
Starter Code: None
Date: January 24, 2026
"""

# Bill total
bill_total = float(input("Enter the total cost of your dinner: $"))

# Calculate tip 
tip_15 = bill_total * 0.15
tip_20 = bill_total * 0.20

# Calculate total plus tip
total_with_15 = bill_total + tip_15
total_with_20 = bill_total + tip_20

# Display
print(f"\nSuggested 15% tip: ${tip_15:.2f}")
print(f"Total with 15% tip: ${total_with_15:.2f}")

print(f"\nSuggested 20% tip: ${tip_20:.2f}")
print(f"Total with 20% tip: ${total_with_20:.2f}")

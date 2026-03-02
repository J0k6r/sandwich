"""
Program Name: Sandwich
Author: Kaleb Quinn
Purpose: 
Date: 03/01/2026
"""
# Part 1 - Making Sandwiches

sandwich_orders = ['tuna', 'turkey', 'blt', 'veggie', 'club']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll done! Here's what was made:")
for sandwich in finished_sandwiches:
    print(sandwich)

  # Part 2 - No Pastrami

sandwich_orders_2 = ['pastrami', 'tuna', 'pastrami', 'turkey', 'pastrami', 'blt']
finished_sandwiches_2 = []

print("\nSorry, we are out of pastrami today!")

while 'pastrami' in sandwich_orders_2:
    sandwich_orders_2.remove('pastrami')

while sandwich_orders_2:
    sandwich = sandwich_orders_2.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches_2.append(sandwich)

print("\nAll done! Here's what was made:")
for sandwich in finished_sandwiches_2:
    print(sandwich)
      
#User inputs cost of food
food_cost = float(input("Enter food cost(in dollars($))\n"))
tip_rate = 0.18
tax_rate = 0.07

#calculate tax tip and total values
tip_cost = food_cost*tip_rate
tax_cost = food_cost*tax_rate
total_cost = food_cost + tip_cost + tax_cost

#Output tip tax and total strings
print("Tip (18%): ${:.2f}".format(tip_cost))
print("Sales Tax (7%): ${:.2f}".format(tax_cost))
print("Total Price: ${:.2f}".format(total_cost))
input("Press Enter to exit.")

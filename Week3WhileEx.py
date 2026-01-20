# Running Total Program
# This program asks the user to enter numbers and
# calculates the total until a negative number is entered.

# Step 1: Prompt for input
total = 0
number = float(input("Enter a number (enter a negative number to stop): "))

# Step 2 & 3: Loop and calculate running total
while number >= 0:
    total += number
    number = float(input("Enter another number (enter a negative number to stop): "))

# Step 4: Output the total sum
print("\nThe total sum of the numbers entered is:", total)






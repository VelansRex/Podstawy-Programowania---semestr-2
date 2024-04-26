# 42. Write a  Python program to calculate the sum and
# average of n integer numbers (input from the user). Input 0 to finish.

# Display a prompt asking the user to input integers to calculate their sum and average,
# specifying that entering 0 will exit the program
print("Input some integers to calculate their sum and average. Input 0 to exit.")

# Initialize variables for count, sum, and the first number to 1
count = 0
sum = 0.0
number = 1

# Iterate until the user inputs 0
while number != 0:
    # Prompt the user to input a number and convert it to an integer
    number = int(input(""))

    # Add the entered number to the sum
    sum = sum + number

    # Increment the count of entered numbers
    count += 1

# Check if no numbers were entered
if count == 0:
    print("Input some numbers")
else:
    # Calculate and display the average and sum of the entered numbers
    print("Average and Sum of the above numbers are: ", sum / (count - 1), sum)
# 34. Write a  Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

# Define a function named 'sum' that takes two parameters 'x' and 'y'
def sum(x, y):
    # Calculate the sum of 'x' and 'y' and assign it to the variable 'sum'
    sum = x + y

    # Check if the calculated sum falls within the range of 15 to 19 (inclusive)
    if sum in range(15, 20):
        return 20  # If the sum falls within the specified range, return 20
    else:
        return sum  # If the sum doesn't fall within the specified range, return the calculated sum


# Call the 'sum' function with different arguments and print the results
print(sum(10, 6))  # Call the function 'sum' with arguments 10 and 6, then print the result
print(sum(10, 2))  # Call the function 'sum' with arguments 10 and 2, then print the result
print(sum(10, 12))  # Call the function 'sum' with arguments 10 and 12, then print the result
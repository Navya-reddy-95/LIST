'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
'''
# Function to calculate the sum of elements in the array
def calculate_sum(elements):
    return sum(elements)

# Input number of elements
n = int(input("Enter the number of elements: "))

# Check if the number of elements is within the limit
if n > 20:
    print("Error: The maximum number of elements allowed is 20.")
else:
    # Input the array elements
    elements = []
    print(f"Enter {n} elements:")
    for _ in range(n):
        elements.append(int(input()))

    # Calculate the sum of the elements
    total_sum = calculate_sum(elements)

    # Output the result
    print(total_sum)

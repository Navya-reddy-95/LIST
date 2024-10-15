'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
# Function to count occurrences of a value in the list
def count_occurrences(elements, value):
    return elements.count(value)

# Input the list elements
elements = list(map(int, input("Enter the list elements separated by space: ").split()))

# Input the value to count
value_to_count = int(input("Enter the value to count: "))

# Count the occurrences
count = count_occurrences(elements, value_to_count)

# Output the result
print(count)

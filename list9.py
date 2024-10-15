'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
# Function to print the list in reverse order
def print_reverse(elements):
    reversed_list = elements[::-1]  # Reverse the list
    print(" ".join(map(str, reversed_list)))  # Print the reversed list

# Input the list elements
elements = list(map(int, input("Enter the list elements separated by space: ").split()))

# Print the list in reverse order
print_reverse(elements)

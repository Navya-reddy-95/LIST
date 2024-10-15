'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
'''
# Function to separate even and odd numbers
def separate_even_odd(size, elements):
    even_numbers = []
    odd_numbers = []

    for num in elements:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

# Input size of the list
size = int(input("Enter the size of the list: "))

# Input the list elements
elements = []
print(f"Enter {size} elements:")
for _ in range(size):
    elements.append(int(input()))

# Get even and odd lists
even_list, odd_list = separate_even_odd(size, elements)

# Output the results
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)


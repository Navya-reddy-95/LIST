'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
def find_largest_number():
    # Input the size of the list
    size = int(input())
    
    # Initialize an empty list
    numbers = []
    
    # Input the elements of the list
    for _ in range(size):
        element = int(input())
        numbers.append(element)
    
    # Find the largest number
    largest = max(numbers)
    
    # Output the largest number
    print(largest)

# Call the function
find_largest_number()

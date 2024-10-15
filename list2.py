'''
)Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
'''
def create_and_display_list():
    # Input the size of the list
    size = int(input())
    
    # Initialize an empty list
    numbers = []
    
    # Input the elements of the list
    for _ in range(size):
        element = int(input())
        numbers.append(element)
    
    # Output the list elements separated by space
    print(" ".join(map(str, numbers)))

# Call the function
create_and_display_list()

'''
Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
Sample Input 1:
5
1 2 3 6 5
3
Sample Output 1:
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
Sample Output 2:
4 is not present in the given list
'''
# Function to search for an element in the list
def search_element(elements, target):
    if target in elements:
        return f"{target} is present in the given list"
    else:
        return f"{target} is not present in the given list"

# Input size of the list
size = int(input("Enter the size of the list: "))

# Input the list elements in a single line
elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))

# Input the element to search
target = int(input("Enter the element to search: "))

# Search for the element
result = search_element(elements, target)

# Output the result
print(result)

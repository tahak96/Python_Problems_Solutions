#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#THIS PROBLEM COULD HAVE BEEN MUCH SIMPLER BY USING DIVISION, BUT I IMPLEMENTED WITHOUT USING IT.

lst = [3,2,1]

#this is a function that returns the product of numbers
def product_function(SOMEINPUT):
    product = 1
    for num in SOMEINPUT:
        product = product*num
    return product

#define  a function that uses a for loop to increment the value of the index and then using slicing input these
#values to a function that calculates product for the remaining values in the list.
def fname(lst):
    result = []
    for nums in range(len(lst)):
        result.append((product_function(lst[nums+1:]))*(product_function(lst[:nums])))
    return result

x = fname(lst)
print(x)

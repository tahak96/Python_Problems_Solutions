#Problem
#Given an array of integers, find the first missing positive integer
#in linear time and constant space. In other words, find the lowest
#positive integer that does not exist in the array.The array can
#contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#Solution
#using a for loop check if all the numbers from range(lowest_num, highest_num) are there,
    #if yes, then return highest_num+1
    # if no, then return the missing no.

lst = [1,2]

def fname(lst):
    if min(lst) < 0:
        lowest_num = 0
    else:
        lowest_num = min(lst)

    highest_num = max(lst)

    for num in range(lowest_num+1,highest_num):
        if num not in lst:
            return num
    return highest_num+1

x = fname(lst)
print(x)

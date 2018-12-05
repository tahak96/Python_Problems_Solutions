# Given a list of numbers L, implement a method sum(i, j) which returns the sum
#from the sublist L[i:j] (including i, excluding j).
#
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.
            # Indexes     0  1  2  3  4

lst = [1,2,3,4,5]
sum_index = (1,3)

#define a function that calculates the sum of all the values between lst[i] + .... + lst[j-1]
def sum_function(lst,sum_index):
    if (len(sum_index) < 2) or (len(sum_index) > 2):      #checks if i and j are provided or not
        return False

    i = sum_index[0]
    j = sum_index[1]
    if i == j:
        return False
        
    return sum(lst[i:j])

x = sum_function(lst,sum_index)
print(x)

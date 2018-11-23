#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#since the list is not sorted,the best method to use would be to implement a dictionary

lst = [10,15,3,7]
k = 18

def fname(lst,k):
    d = {}
    if len(lst) <= 1:
        return lst
    for nums in lst:
        d[nums] = k-nums
        if (k-nums) in d:
            return d[nums],d[k-nums]

x = fname(lst,k)
print(x)

#Time complexity is O(n) and space complexity is O(n)

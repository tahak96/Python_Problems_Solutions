# Given a list of integers and a number K, return which contiguous elements of the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].

#Applying a brute force solution, as it doesn't have any specified time complexity requirements
lst = [1,2,3,4,5]
k = 5

def fname(lst,k):
    for i in range(len(lst)):
        if k <= sum(lst):
            for j in range(i,len(lst)):
                if sum(lst[i:j+1]) == k:
                    result = lst[i:j+1]
                    return result
        else:
            return "Not found"

x =fname(lst,k)
print(x)

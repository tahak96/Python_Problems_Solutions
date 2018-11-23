#Find the minimum number of coins required to make n cents.

#Recursion problem
list_coins = [1,5,10,25]

"""
Create a function that takes in the N input. And then recursively check
if coins add upto that number and return the no. of coins used to so.
"""
n = 15
DENOMINATIONS = [1, 5, 10, 25]

def minimum_coins_dp(n):
    cache = [0 for _ in range(n + 1)]

    for d in DENOMINATIONS:
        if d < len(cache):
            cache[d] = 1

    for i in range(1, n + 1):
        cache[i] = min(1 + cache[i - d] for d in DENOMINATIONS if i - d >= 0)

    return cache[n]

x = minimum_coins_dp(n)
print(x)

#Find the first recurring character in a String

#Solution
#Implement a counter using a dictionary and whenever the counter is > 1
#return that as the result
#TIme complexity = O(n), Size = O(n)

str1 = "ABCA"

def fname(str1):
    d = {}
    counter = 1
    for chars in range(len(str1)):
        if str1[chars] in d:
            return str1[chars]
        d[str1[chars]] = counter

x = fname(str1)
print(x)

# heapq module has 2 functions nlargest & nsmallest
import heapq as hq

# 4 built-in data types in Python used to store collections of data
numList = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numSet = { 10082, 256, 74, 12, 343, 99, 2383 }
numTuple = ( 1, 2, 3, 4, 5, 6, 7 )
numListOfDict = [
    { "price": 1 },
    { "price": 2 },
    { "price": 3 }
]

# find 3 largest number in List
print(hq.nlargest(3, numList))

# find 3 smallest number in List
print(hq.nsmallest(3, numList))

# find 3 largest number in Set
print(hq.nlargest(3, numSet))

# find 3 smallest number in Set
print(hq.nsmallest(3, numSet))

# find 3 largest number in Tuple
print(hq.nlargest(3, numTuple))

# find 3 smallest number in Tuple
print(hq.nsmallest(3, numTuple))

# find 3 largest number in Dict
cheap = hq.nsmallest(3, numListOfDict, key=lambda s: s['price'])
print(cheap)

# find 3 smallest number in Dict
expensive = hq.nlargest(3, numListOfDict, key=lambda s: s['price'])
print(expensive)

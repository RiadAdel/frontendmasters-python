# list: collection of similar items

# mixed
l = [1, "string", True]

# create list [4,4,4,4,4]
l = list([4] * 5)
l = [4] * 5

# get size
len(l)

# accessing
l = ["a", "b", "c", "d", "e"]
print(l[:3])  # [a,b,c]
print(l[::2])  # [a,c,e]
print(l[2])  # c

# you can add comma after last elm
l = [
    1,
    2,
    3,
]

# sorted doesn't change l but returns new sorted list
sorted(l, reverse=True)  # [3,2,1]

# sort change the list
l.sort()
l.reverse()  # for descending

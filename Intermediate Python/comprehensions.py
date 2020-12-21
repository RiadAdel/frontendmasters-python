# for lists
skills = ["html", "css", "javascript"]
capitalized_skills = [elm.upper() for elm in skills]
nums = [1, 2, 3, 4]
squared = [num * num for num in nums]
# condition
even_squared = [num * num for num in nums if not num % 2]
# nested
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
flat_matrix = [col for row in matrix for col in row]

# for sets, dictionaries, and tuples
num_sqr = {num: num * num for num in range(10)}  # dict
names = ["a", "b", "c", "d", "b", "c", "d"]
name_set = {name + name for name in names}  # set

# generators: performance >>>>> when using large lists
# note: using sum(seq) works only once then return zero because i = 3 after the first iteration
seq = (i for i in range(3))
for ix in range(10):
    print(sum(seq))

# slicing
# it returns a copy not a reference
l = [1, 2, 3, 4, 5, 6]
list_slice = l[:-1]  # ignore last one

# zipping
players = ["Sam", "Dani", "Max"]
scores = [1, 2, 3, 4]
print([f"name:{name}, Score:{score}" for name, score in zip(players, scores)])

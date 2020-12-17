colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# range function is written in c, you can't pass keyword arguments
# for indx in range(start=0, stop=10, step=2): #this will cause error due to ['start','stop','step']
for indx in range(0, 10, 2):
    print(indx)

person = {
    "name": "Riad",
    "age": 23,
    "city": "Cairo",
}
# if you used
#   x in person: this will iterate over keys only
for key, val in person.items():
    print(f"my {key} is {val}")

# control flow
if "name" in person:
    print(person["name"])

# no do while

# break, return and continue
# break only breaks one loop
for i in range(5):
    for j in range(10):
        print(f"i = {i} , j = {j}")
        if j == 2:
            break
# default params are created after the first call, then shared
# don't use default list or any ref var, it will aggregate
def insert(elm, arr=[]):
    arr.append(elm)
    print(arr)


insert(10)  # [10]
insert(20)  # [10,20]

x = 10

# use global keyword to access global vars
def foo():
    global x
    x = 20
    print(x)


def ops(x, y):
    print(f"this is x: {x}")
    print(f"this is y:{y}")


# ordering doesn't matter
print(ops(y=20, x=0))

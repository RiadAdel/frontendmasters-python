# tuple: a collection of related but different items

# tuples are immutables
t = ("Riad", 23)
t = "Riad", 23
# t[0] = "Ahmed" will cause error

# destructure
name, age = t

# for ignoring age
name, _ = t

# tuple must contain comma
# t = (2) # int
t = (2,)  # tuple

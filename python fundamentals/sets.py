# sets: collection of not ordered immutable unique items
s = {1, 4}

# sets use hashing to store items

# empty set
# if you used {} it will create dict not empty set
s = set()

# sets doesn't support indexing

# to remove item, if it doesn't exist
# s.remove() ==> raise error
# s.discard() ==> no errors

# union
{1, 2, 3} | {2, 5, 64}
{1, 2, 3}.union({2, 5, 64})

# intersect
{1, 2, 3} & {1, 2, 5}
{1, 2, 3}.intersection({1, 2, 5})

# diff
{1, 2, 3} - {1, 2, 5}
{1, 2, 3}.difference({1, 2, 5})

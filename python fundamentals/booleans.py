# True
True
# all numbers except 0
# non-empty containers [2,3]
"abc"

# False
False
0
# any empty container {} []
""
None

# equality
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # true
a is b  # false
a is not b  # true

# logical operators
a = True
b = False
a and b  # false
b or a  # true
not a  # false

# return the first false-y one
[] and {} and [1, 2, 3]  # []
# return the last true value
[1] and {2}  # {2}

# return the first true one
[] or {} or [1]  # [1]
# return the last false value
[] or None or {}  # {}

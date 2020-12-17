# key-value collection
# key: immutable
# value: anything
person = {"name": "Riad", "age": "23", "city": "Cairo"}
x = "fav-number"
person[x] = 2
print(person)

# access items
person.get("NotFound")  # no error
# person["NotFound"] #error

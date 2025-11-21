"""Week 6 dictionaries"""

phonebook = {}
phonebook["Alice"] = "555-1234"
phonebook["Bob"] = "555-5678"
phonebook["Charlie"] = "555-9999"

name = input("Who do you want to look up?")
print(phonebook[name])

for name, number in phonebook.items():
    print(f"{name}: {number}")
    
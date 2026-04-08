my_tuple = (1, 2, 1, 4, 5)

for item in my_tuple:
    print(item)


my_list = [3, 2, 3, 4, 78]
print("=======")
for item in my_list:

    print(item)

print("===set====")
set = {3, 2, 3}

for item in set:
    print(item)


person = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(person.get("city"))

for key,value in person.items():
    print(key,value)
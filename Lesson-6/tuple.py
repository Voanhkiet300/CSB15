# collection data types in Python:
#   list []: ordered, changeable, allow duplicate members
#   tuple(): ordered, unchangeable, allow duplicate members
#   set{}: unordered, unchangeable (add, remove items),  no duplicate members
#   dictionary {key: value}: ordered, changeable,  no duplicates

student = ("Kiet", 16, "male", "Kiet")

# print(student.count("Kiet"))
# print(student.index("Kiet"))

# for i, value in enumerate(student, start=0):
#     print(f"{i}: {value}")

# if "Kiet" in student:
#     print("True")


# slicing
number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(number[::-1])
print(number[-7:-1:2])

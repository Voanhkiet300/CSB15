# collection data types in Python:
#   list []: ordered, changeable, allow duplicate members
#   tuple(): ordered, unchangeable, allow duplicate members
#   set{}: unordered, unchangeable (add, remove items),  no duplicate members
#   dictionary {key: value}: ordered, changeable,  no duplicates



# 1D list
animal = ["cat", "dog", "elephant"]
animal[0] = "monkey"
# print(animal[0])

# # foreach
# for item in animal:
#     print(item)

# # for
# for i in range(len(animal)):
#     print(animal[i])

# # function
# animal.append("cat")
# animal.remove("monkey")
# animal.pop() # delete last item
# item = animal.pop() # get last element and delete
# animal.insert(1, "dog") # insert at specific position
# print(animal)
# animal.clear()

# 2D list
fruit = [["apple", "banana"], ["cherry", "date"], ["elderberry", "fig"]]
print(fruit[1])
print(fruit[1][0])




food = ["cupcake", "pancake"]
drink = ["milk tea", "coffee"]
meal = [food, drink]

# clone list
list_clone = meal.copy()

# join 2 list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 # way 1
list4 = list1.extend(list2) # way 2
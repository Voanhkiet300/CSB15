# lambda:
# function 1 dong
def sum(x, y):
    return x+y

sum_lambda = lambda x, y: x+y



# sort, map, filter:
# sort() method = used with lists
# sorted() function = used with iterables



students = (
    ("A", 12),
    ("E", 15),
    ("B", 13),
    ("D", 14),
    ("C", 11),
    ("F", 16),
)
sorted_student = sorted(students)
# print(sorted_student)


age = lambda item: item[1]
sorted_age = sorted(students, key=age)
# print(sorted_age)


students_name = ["A", "B", "C", "D", "E", "F"]
students_name.sort() # A => Z
students_name.sort(reverse=True) # Z => A



# map() = applies a function to each item in an iterable (list, tuple, ...)
# map(function, iterable)
store_dollars = [("apple", 1), ("jacket", 50), ("paints", 40), ("skirt", 80)]
store_euros = list(map((lambda item: (item[0], item[1]*0.82)), store_dollars))

# print(store_euros)


# filter() = creates a collection of elements from an iterable for which a func returns
# filter(function, iterable)
filter_students = tuple(filter((lambda item: item[1] >= 14), students))
# print(filter_students)



# viet tat list, dict:
# rut gon for + lambda
# list = [expression for item in iterable]
cols = 5
rows = 3
new_map = []
for i in range(rows):
    col = []
    for i in range(cols):
        col.append('-')
    new_map.append(col)

print(new_map)



# new_map 2
new_map_2 = [['-']*cols for i in range(rows)]
print(new_map_2)



# dict = {key: expression for (key, value) in iterable}
cities_in_F = {"New York": 32, "Boston": 75, "Los Angles": 100, "Chicago": 50}
cities_in_C = {
    key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()
}
print(cities_in_C)


# list = [expression for item in iterable if conditional]
print(True) if 10 % 2 == 0 else print(False)
odd_list = [item for item in range(1, 11) if item % 2 == 0]



# dict = {key: expression for (key, value) in iterable if conditional}
warm_cities = {key: value for (key, value) in cities_in_F.items() if value > 40}


# list = [expression if/else for i in iterable]
students = [50, 40, 70, 60, 80, 100, 0]
passed_list = list(filter(lambda sc: sc >= 60), students)
new_class = [item if item >= 60 else False for item in students]



# dictionary = {key: if/else for (key, value) in iterable}
cities_status = {
    key: "WARM" if value >= 40 else "COLD" for (key, value) in cities_in_F.item()
}

# dictionary = {key: function(value) if/else for (key, value) in iterable}
# def check_temp(value):
#     if value > 60:



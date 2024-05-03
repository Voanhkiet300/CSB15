# collection data types in Python:
#   list []: ordered, changeable, allow duplicate members
#   tuple(): ordered, unchangeable, allow duplicate members
#   set{}: unordered, unchangeable (add, remove items),  no duplicate members
#   dictionary {key: value}: ordered, changeable,  no duplicates

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Vietnam': 'Hanoi'}

# get item
print(capitals['Vietnam'])
print(capitals.get('USA'))
print()

# update item
capitals['USA'] = 'Boston'
print(capitals['USA'])
print()
print()
capitals.update({'aaa': 'Ndd', 'Vietnam': 'Ho Chi Minh'})

# remove + clear
capitals.pop('China')
del capitals['India']
print(capitals)
print()
# capitals.clear()

# print list
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print()
# for
for key, value in capitals.items():
    print(key, value)
print()

for i in capitals:
    print(i)
print()

for i in capitals.values():
    print(i)
print()

# check
print('USA' in capitals)
print('China' in capitals)
print('Vietnam' in capitals)
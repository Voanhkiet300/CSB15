x = 12 # global var 

def my_func ():
    global x
    x = 10 

print(x)
my_func()
print(x)


a = 10
b = 5

def my_func(a, b):
    global sum
    sum = a + b


my_func(a, b)
print(sum)


if sum == 15:
    sum = 10


print(sum)
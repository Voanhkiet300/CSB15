import time

# userInput = None
# while (not userInput):
#     userInput = input("Can you help me? ")
#     if (userInput == "yes"):
#         print("I am so happy")
#         break
#     else:
#         print("Pls say yes")
#         userInput = None
#         continue



# for

# for i in range(1, 10, 2):
#     print(i)

# for i in "hello":
#     print(i)
#     time.sleep(0.5)

a = input("Enter a even number: ")

if (a.isdigit()):
    while (a%2 != 0 or a <= 0):
        print("This is not an even number")
        a = int(input("Enter a even number: "))
        continue

    print("The entered number is ", a)
print("This is not an even number")
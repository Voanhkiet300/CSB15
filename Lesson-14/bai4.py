print("== Welcome to MindX Restaurant ==")


dishs = []
y = True
while y:
    dish = input("\nPlease choose a dish: ")
    if dish in dishs:
        i = input("You chose this already. Anything else? (y/n): ")
        while i != "y" and i != "n":
            i = input("You chose this already. Anything else? (y/n): ")
        if i == "n":
            y = False
    else:
        dishs.append(dish)
        i = input("Great choice! Anything else? (y/n): ")
        while i != "y" and i != "n":
            i = input("Great choice! Anything else? (y/n): ")
        if i == "n":
            y = False

print("Well done! Your order:\n-", "\n- ".join(dishs))

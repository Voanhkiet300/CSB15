list = ["red", "blue", "Yellow"]

print(f"color list:\n{' '.join(list)}")

color = input("Input a new color: ")
list.append(color)
print(f"color list:\n{' '.join(list)}")
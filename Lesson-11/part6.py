light = {"Name": "Light", "Age": 17, "Strength": 8, "Defense": 10, "HP": 100, "Backpack": ["Shield", "Bread Loaf"], "Gold": 100, "Level": 2}

# bai 2:
light["Gold"] += 50
print("Gold:", light["Gold"])

# bai 3:
light["Backpack"] += ["FlintStone"]
print("Backpack:", ', '.join(light["Backpack"]))
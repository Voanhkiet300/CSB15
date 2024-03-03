deposit = float(input("Enter the deposit amount: "))

amount_1_year = deposit * (1 + 0.05)
print(f"After 1 year, you will have: {amount_1_year:.2f} VND")

amount_2_year = deposit * (1 + 0.05) ** 2
print(f"After 2 years, you will have: {amount_2_year:.2f} VND")

amount_10_year = deposit * (1 + 0.05) ** 10
print(f"After 10 years, you will have: {amount_10_year:.2f} VND")
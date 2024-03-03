from datetime import datetime

date_input = input("Enter a date in MM/DD/YYYY format: ")

if date_input.find("/") != 2 or date_input.find("/") != 5 or len(date_input) != 10:
    print("Invalid date format. Please use MM/DD/YYYY format.")
else:
    date = datetime.strptime(date_input, "%m/%d/%Y")
    print("The date you entered is:", date.strftime("%d/%m/%Y"))
import calendar

print("\033c")

yy = int(input("Enter the year : "))
mm = int(input("Enter the month as integer : "))

month = calendar.month(yy, mm)

print(month)
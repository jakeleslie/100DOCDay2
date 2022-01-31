#s = "jake"

#print(s[0]) # prints out J


# type casting in pycharm, integer to string

#ournum = 4

#print(type(str(ournum)))

#print(2 ** 3)

# Life until 90

#age = input("Please enter your current age\n")
#age_in_int = int(age)

# 90 - age = how many years left
#until_90 = 90 - age_in_int
# 90 - age * 365 shows how many days left
#until_90_days = until_90 * 365
# 90 - age * 52 shows how many weeks left
#until_90_weeks = until_90 * 52
# 90 - age * 12 shows how many months left
#until_90_months = until_90 * 12

#print(f"You have {until_90_days} days, {until_90_weeks} weeks, and {until_90_months} months left.")

# BMI CALCULATOR
# bmi is weight / height
# 99 killos 1.74 meters
kilos = input("Enter your weight in KG\n")
height = input("Enter your height in meters\n")

# Weight in kilos / height squared. Needed to make it its own variable and equation, I was trying to do it in one line which didn't work.
# Keep KG as an int
bmi = int(kilos) / float(height) ** 2
# Want to make it an int so it will round up or down, which makes it work better.
bmi_as_int = int(bmi)

print(f"Your BMI is: {bmi_as_int}")


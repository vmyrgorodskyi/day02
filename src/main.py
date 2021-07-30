#lesson17

#print("Hello"[4])

#print(123 + 234)

#lesson18

#num_char = len(input("what is your name? "))
#new_num_char = str(num_char)
#print("Your name has " + num_char + " chars")

#print(new_num_char)

#a = float(123)
#print(type(a))

#print(70 + float("100.5"))

#lesson19
# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#new_nums = int(two_digit_number)
#num1 = two_digit_number[0]
#print(num1)
#num2 = two_digit_number[1]
#print(num2)
#final = int(num1) + int(num2)

#print(final)

#lesson20

#print(3 * (3 + 3) / 3 - 3)

#lesson21

# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#n_height = float(height)
#n_weight = int(weight)
#bmi = int(weight) / float(height) ** 2
#n_bmi = int(bmi)
#print(n_bmi)

#lesson22

#print(8%3)

#f-string
#score = 1
#height = 1.8
#isWinning = True
#print(f"your score is {score}, your height is {height}, your are winnnig is {isWinning}")

#lesson23
# 🚨 Don't change the code below 👇
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#new_age = int(age)
#death_y = 90 - new_age
#death_m = int(death_y * 52)
#death_d = death_y * 365
#print(f"You have left {death_y} years until 90 or {death_m} weeks or {death_d} days to live")

#lesson24

print("Welcome to the tip calculator")
total_bill = input("What is the total bill? ")
percentage = input("what percentage tip would you like to give? 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")
c_total_bill = float(total_bill)
c_percentage = float(percentage)
c_number_of_people = int(number_of_people)
result = (c_total_bill + (c_total_bill * (c_percentage / 100))) / c_number_of_people
print(round(result, 2))
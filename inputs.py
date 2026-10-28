"""
Ask user for age → print age next year
Task 2
Ask for two numbers → print their sum
Task 3 (Important)
Ask for a price → add 10 → print new price
"""
#Answer:
age = int(input("what is your age"))
print("you will be ", age + 1, "years old next year")

num = int(input("enter a numbers"))
num1 = int(input("enter a num"))
print(num + num1)

price = float(input("enter price"))
print(price + 10)


#conversion to float
price = float(input(" Enter a price"))
print(price + 2, "this is cheap")

#conersion of int
testScore = int(input("enter your score"))
print(testScore +5 )

# User input
age = int(input("what year where you born"))
print(age + 10 , "wow so young")
#Final Practice Before the Next Lesson

#Write a program that asks the user for:

#1. Their name
#2. Their age
#3. Their favorite programming language
"""Then print:
Hello Gift!
You are 20 years old.
Your favorite programming language is Python.

**Important:** Don't type `"Gift"` or `"Python"` directly in the `print()`
 statements. Use the variables that store the user's input.
 """

name = input("what is your name :")
age = input("how old are you :")
faviourite =input("what is your favorite programming language:  ") 

print("hello", name , "!")
print("You are", age , "years old. ")
print("Your favorite programming language is ", faviourite )

name = input("what is your name? ")
favouriteColor = input("what is your faviourite color ")
marry = input("are you ready for marriage ")
print("helo", name)
print("your favourite color is :",favouriteColor )
print("would you marry me ", marry)
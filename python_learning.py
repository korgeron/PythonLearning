# print("Hello World")


# TODO: DEFINE A FUNCTION TO TAKE IN TWO NUMBERS AND RETURN THE SUM

# def addNums(a, b):
#     return a + b
# twenty = addNums(10 , 10)
# print(twenty)


# TODO: LET THE USER INPUT TWO VALUES TO SEND TO THE addNums() FUNCTION

# num1 = input("Give me a number! ")
# num2 = input("Give me another number to add to the first! ")
# ans = addNums(float(num1), float(num2))
# print(ans)
# print(str(num1) + " + " + str(num2) + " = " + str(ans))


# TODO: PRINT INT VALUE IF BOTH NUMBERS ARE WHOLE NUMBERS. PRINT FLOAT VALUE IF ANY VALUE HAS A DECIMAL

# print("." in str(num1))
# if "." in str(num1) or "." in str(num2):
#    ans = addNums(float(num1), float(num2))
#    print(str(num1) + " + " + str(num2) + " = " + str(ans))
#
#    print("There is a floating value!")
# else:
#    ans = addNums(int(num1), int(num2))
#    print(str(num1) + " + " + str(num2) + " = " + str(ans))
#
#    print("There is only whole numbers!")


# TODO: REFACTOR ABOVE CODE TO USE ELSE IF STATEMENT

# if "." in str(num1):
#    ans = addNums(float(num1), float(num2))
#    print(str(num1) + " + " + str(num2) + " = " + str(ans))
#
#    print("There is a floating value!")
# elif "." in str(num2):
#    ans = addNums(float(num1), float(num2))
#    print(str(num1) + " + " + str(num2) + " = " + str(ans))
#
#    print("There is a floating value!")
# else:
#    ans = addNums(int(num1), int(num2))
#    print(str(num1) + " + " + str(num2) + " = " + str(ans))
#
#    print("There is only whole numbers!")


# TODO: LETS LEARN STRING MANIPULATION

# name = "Van Heizer"
# print(name)


# TODO: PRINT FIRST NAME AND LAST NAME IN SEPARATE VARIABLES

# first_name = name.split(" ")[0]
# print("First Name: " + first_name)
# last_name = name.split(" ")[1]
# print("Last Name: " + last_name)


# TODO: PRINT LENGTH OF STRING

# print("Length = " + str(len(name)))


# TODO: CHANGE FIRST NAME TO WINSTON FROM ORIGINAL STRING

# new_name = name.replace(first_name , "Winston")
# print(new_name)


# TODO: PRINT NEW FIRST NAME AND LAST NAME IN SEPARATE VARIABLES

# first_name = new_name.split(" ")[0]
# last_name = new_name.split(" ")[1]
# print("First Name: " + first_name)
# print("Last Name: " + last_name)


# TODO: PRINT NEW LENGTH OF STRING

# print("Length = " + str(len(new_name)))


# TODO: MESSING WITH STORAGE DATA TYPES

# Tuple (can not change stored data)

# tpl = ("Jess", "Ron", "Max", "Rachel")
# print(tpl)

# List (can change stored data)

# lst = [1 , 2 , 3]
# lst.insert(0 , "1")
# lst.append(True)
# print(lst)
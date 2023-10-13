# print("Hello World")
import doctest

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

# Tuple (can not change stored data) ex code = tuple_name = (value , value , value)

# tpl = ("Jess", "Ron", "Max", "Rachel")
# print(tpl)

# List (can change stored data) ex code = list_name = [value , value , value]

# lst = [1 , 2 , 3]
# lst.insert(0 , "1")
# lst.append(True)
# print(lst)

# UNPACK THE LIST ABOVE (lst)
# one,two,three = lst

# printing using multiple prints
# print(one)
# print(two)
# print(three)

# printing using single print
# print(str(one) + "\n" + str(two) + "\n" + str(three))

# accessing certain values in list using index
# print(lst[0:2])

# updating values in a list
# names1 = ["John" , "Beck" , "Lucy"]
# names1[0] = "Danny Boy"
# print(names1)

# adding list together to make one big list
# names2 = ["Kelsi" , "Kevin" , "Keylan" , "Karson"]
# print(names2)
# biglist = names1 + names2
# print(biglist)

# changing tuple to list
# tpl = (1 , 2 , 3)
# tpl = list(tpl)
# print(tpl)


# TODO: USING FOR LOOP TO POPULATE A LIST WITH INFO FROM A TUPLE

# EXTRA TASK (function definition for code below)
# def item_multiplier(num):
#     num = int(num) * 2
#     return str(num)


# tpl = ("1", "2", "3")
# lst = []
# for item in tpl:
# take item and double it / values should stay a string (EXTRA: Make a function to do this task)

# this should return ["2", "4", "6"]
#     lst.append(item_multiplier(item))
# print(lst)


# TODO: LIST COMPREHENSION

# list1 = [2, 3, 4, 5, 6]

""" LONG WAY """
# list2 = []
# for each in list1:
#     list2.append(each*each)
# print(list2)

""" SHORT WAY """
# list2 = [each*each for each in list1]
# print(list2)


# TODO: LIST COMPREHENSION WITH IF STATEMENT

""" LONG WAY """
# list1 = [2, 3, 4, 5, 6]
# list2 = []
# for each in list1:
#     if each % 2 == 0:
#         list2.append(each*each)
# print(list2)

""" SHORT WAY """
# list2 = [item*item for item in list1 if item % 2 == 0]
# print(list2)


# TODO: LIST COMPREHENSION WITH IF / ELSE STATEMENT

""" Given a list of names, only change the name John to William """
# names = ["John", "Danny", "John", "Kelsi", "Kevin", "Johnny"]
# print(names)
# changed_names = [name.replace(name, "William") if name == "John" else name for name in names]
# print(changed_names)

# TODO: DICTIONARIES
# Dictionary (key : value pairs) ex code = dictionary_name = {key:value, key:value}
#            unique : can be anything

# dictionary = {}

# adding values to dictionary
# dictionary.update({1: "hello", 2: "there"})
# print(dictionary)
# dictionary[3] = "Testing the addition!"
# print(dictionary)

# updating value to a pair
# dictionary[1] = "Todd says hello!"
# print(dictionary)

# many ways to delete a pair
# dictionary.pop(1)
# print(dictionary)
# del dictionary[2]
# print(dictionary)


# TODO: APPLICATION THAT CAN ADD / READ FROM A "SCHOOL DATABASE"
# s_info = {"SKJ": "Southern Karate Jiujitsu... a great martial arts school",
#           "HS": "Home School... my wife is a great teacher!"}
#
# user_input = ""

# print("Hello There!")
# while user_input != "none":
#     user_input = input(
#         "Add a school or look up your school by code! ")
#
#     if user_input.upper() == "ADD":
#         key = input("Enter a school code... ")
#         value = input("Enter the school info... ")
#         s_info[key.upper()] = value.capitalize()
#         print("School info added!")
#     else:
#         if user_input.upper() in s_info:
#             print(s_info[user_input.upper()])
#         elif user_input == "none":
#             print("Have a great day!")
#         else:
#             print("School not found in database... TRY AGAIN!")

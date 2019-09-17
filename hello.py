# myList = ['Thor', 'IronMan', 'Starlord']
# var = myList


print("Calculator... ")
operOne = str(input("Enter Operator : - + / * : "))
# Developer : THOR God Of Thunder.
# Language : Python

def divide(number1, number2):
    return number1 / number2


def minus(number1, number2):
    return number1 - number2


def multiple(number1, number2):
    return number1 * number2


def add(number1, number2):
    return number1 + number2


if operOne == "+":
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    print("Sum is : ", add(number1, number2))
elif operOne == "-":
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    print("Minus is : ", minus(number1, number2))
elif operOne == "*":
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    print("Multiple is : ", multiple(number1, number2))
elif operOne == "/":
    number1 = int(input("Enter Number 1 : "))
    number2 = int(input("Enter Number 2 : "))
    print("Divide is : ", divide(number1, number2))
else:
    print("Invailed Operator...")

# for  var in myList:
# print(var)

#
# myDicitionary = [
#     {"name":"Thor" , "age":1500 , 'power':'Strong Avengers'},
#     {'team':'Avengers' , 'mission':'Final Infinity'}
# ]
# myDict = {"name": "Thor", "age": 1500, 'power': 'Strong Avengers'}
#
# for m in myDict:
#     print(f"{m} => {myDict[m]}" , end=" ")
# else:
#     print("Let them lay off!")
#
#
# # myDicitionary[0].setdefault({"isLeader": False})
#
# # name = myDicitionary[0].get('name')
# # age = myDicitionary[0].get('age')
#
# # myDicitionary[1].update({'location':'Asgard'})
#
# # print(name)
# # print(age)
#
# # print(myDicitionary[0]["power"])
# # print(myDicitionary[1]["mission"])
#
# # print(myDicitionary[0].items())
# # print(myDicitionary[1].items())
# #
# # print(myDicitionary[0].keys())
# # print(myDicitionary[0].values())
# # print(myDicitionary[1].keys())
# # print(myDicitionary[1].values())
#
# user = {'Name':'Thor' , 'Power':'Strong' , 'Age':1500}
#
# user.setdefault('isLeader',False)
# print(user['isLeader'])
# item = user.items()
# print(item)
#
# user1 = {'isAdmin': False}
# user1 = user.copy()
#
#
# print(user1.pop('Name'))
# print(user1)
#
# hero = {'Thor' , 'Aquaman' , 'Starlord' , 'IronHeart'}
# hero1 = {'Thor' , 'Aquaman' , 'Starlord', 'Superman'}
#
# mySet =  hero.difference(hero1)
#
# print(mySet)

# x = 5
# y = 4
# w = x == y
# print(w)
# age = int(input('Enter Age'))
#
# if 12 <= age != 21 :
#     print("You are 21")
# # elif age == 30:
# #     print("You are 30")
# else:
#     print("You are " + str(age))
# msg = "You are Okay" if age == 20 else "YOu not Okay"
# print(msg)

# email = True
# for i in range(3):
#     print("Attempting...")
#     if email:
#         print("Email sent...")
#         break
# else:
#     print("Error")

# x = input(">")
#
# while x.lower() != 'quit':
#     try:
#         print(eval(x))
#     except NameError as error:
#         print(error)
#     except ZeroDivisionError as error:
#         print(error)
#     except TypeError as error:
#         print(error)
#     finally:
#      x = input(">")

# def myFunc(name , mission):
#     print(f"i am {name} & my mission is {mission}")
#
# def isMissionOn(missionName):
#     print(f"{missionName} and time is 20 Mints")
#
# def isTest(n):
#     x = 0
#     if x ==n:
#         return True
#     else:
#         return False
# myFunc("Thor" , "Protect Universe")
# isMissionOn("Kill 200 People")
# vol = isTest(3)
# print(vol)
#
# def isAdd(num1 , num2):
#     return (num1 ** num2)
# result = isAdd(3,4)
# print(result)
#
# def defult(name="thor"):
#     print(f"{name}")
#
# defult()


# *Args functions

# def Hero(**hero):
#     print(hero)
# for st in hero.values():
#     print(st)
# for v in hero.values():
#     print(v)

#
# Hero(
#     name = "Thor",
#     status = "God of Thunder",
#     home = "Asgard",
#     avengers = "Strong Avengers",
#     wife =" \"Jane Foster\" Mighty Thor"
# )

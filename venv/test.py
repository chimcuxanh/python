#import time;
#localtime = time.localtime(time.time())
#print(" thoi gian hien tai la:", localtime)

#TEST 2: for beginner : mad libs
#Noun =  input("Enter your dream that you want to be in future: ")
#ADJ = input("Enter your attitude that you think good for you: ")
#something = input(" what make you better ")

#print("One day I will become " + Noun)
#print("Nothing in the world can take the place of " + ADJ)
#print(something + "good for you")
#TEST 2.1
#def madlibs(str):
 #   print(str)
 #   return
#madlibs("this is the seconds my mad libs")

#Noun = input("NOUN: ")
#Noun_Plural = input("Noun_plural: ")
#adjective = input("adjective: ")

#print("Be kind to your" + Noun + "- footed" + Noun_Plural)
#print("for a duck may be somebody's " + Noun)
#print("You may think that this is the " + adjective)
#print("Well it is")

#TEST 3
import random
# number = random.randrange(1,16)
# guess = int(input("guess a number between 1 and 16: "))
# while guess !=number:
#     if guess < number:
#         print("you need to guess higher. Try again")
#         guess = int(input("guestt a number between 1 and 16: "))
#     else:
#         print("guess a number lower. Try again")
#         guess = int(input("guess a number between 1 and 16: "))
#
#         print("you guessted the number correctly")

def rolldice():
    number = random.randint(1,6)
    print(number)

    rolldice()
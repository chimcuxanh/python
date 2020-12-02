# import random
# number = random.randint(1, 25)
# # number_of_guesses = 0
# for i in range(4):
# # while number_of_guesses < 5:
#     print('Guess a number between 1 and 25:')
#     guess = input()
#     guess = int(guess)
#     # number_of_guesses = number_of_guesses + 1
#     if guess < number:
#         print('Your guess is too low')
#     if guess > number:
#         print('Your guess is too high')
#     if guess == number:
#         print('You guessed the number!')
#         break
# #if guess == number:
#     #print('You guessed the number!')
# else:
#     print('You did not guess the number. The number was ' + str(number))

def concho_ty(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

number1 = int(input("nhap so thu nhat:"))
number2 = int(input("nhap so thu hai:"))

print("\n")
result = concho_ty(number1, number2)
print("The result is", result)


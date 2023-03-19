import random

# number = float(input("Enter your number: "))
#
# amount = 0
#
# while number >= 0:
#     amount += number
#     number = float(input("Enter your number: "))
#
# print(f"You entere a negative number {number}")
# print(f"Summ amount {amount}")


# my_list = []
# number_wors = int(input("How many words: "))
#
# for sarasa in range(number_wors):
#     my_list.append(input("Enter your word: "))
#
# print(f"Number of words {len(my_list)}")
#
# for word in my_list:
#     print(f"Zodzio {word} ilgis {len(word)} ir eiles numeris {my_list.index(word)+1}")


# i = 0
#
# while i < 3:
#     number = random.randint(1, 6)
#     i += 1
#     print(number)
#     if number == 5:
#         print(f"You lose {number}")
#         break
# else:
#     print("You won")


metai = int(input("ENTER DATE: "))

if (metai % 400 == 0) or (metai % 100 != 0) and (metai % 4 == 0):
    print(f"Leap year {metai}")
else:
    print(f"Not leap {metai}")
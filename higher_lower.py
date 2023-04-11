import random

random_number_list = list(range(1,101))
random_number = random.choice(random_number_list)

while True:
    try:
        number = input("Enter a number from 0 to 100: ")
        number = int(number)
        if number < 0:
            print("The number is positive!")
        elif number > 100:
            print("The numbers don't go higher than 100")
        elif number < random_number:
            print("Higher")
        elif number > random_number:
            print("Lower")
        else:
            print(str(number) + " is the right number!!")
            break
    except ValueError:
        print("Enter a number!")





def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 0
    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_number]:
            print(i)
        guess = input("Enter(A, B, C or D) ")
        guess = guess.upper()
        question_number += 1
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses, guesses):
    print("----------------------")
    print("Results")
    print("----------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

def play_again():
    response = input("\nDo you want to play again? (yes or no): ")
    response = response.lower()
    if response == "yes":
        return True
    else:
        print("Bye")
        return False

questions = {
    "Who created Python? ": "A",
    "What year was Python created? ": "B",
    "Python is tributed to which comedy group? ": "C",
    "Is the earth flat? ": "B"
}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Marc Zuckerburg "],
          ["A. 1989", "B. 1991","C. 200", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True", "B.False", "C.sometimes", "D. What's Earth"]]

while True:
    new_game()
    if not play_again():
        break
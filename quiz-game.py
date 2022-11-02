# Quiz Game in Python

print("Welcome to my Computer Game!!")

playing = input("Do you want to play?: ").lower()

if playing != "yes":
    quit()
while True:
    print("Okay! Let's play :")
    score = 0

    answer = input("What does a CPU stand for? ").lower()
    if answer == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does a GPU stand for? ").lower()
    if answer == "graphic processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does a TPU stand for? ")
    if answer.lower() == "tensor processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does a IPU stand for? ").lower()
    if answer == "infrastructure processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correcct!")
    print("You got " + str((score / 4) * 100) + "%")

    play_again = input("Do you want to play again? (yes/no)").lower()

    if play_again != "yes":
        break
print('Bye!!')

print("Welcome to my quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okey! Let's play then!")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer != "central processing unit":
    print("That's incorrect, please try again.")
    print("Your score: " + str(score))
    answer = input("What does CPU stand for? ").lower()
elif answer == "central processing unit":
        print("Congratulations! That's correct answer!")
        score += 1
        print("Your score: " + str(score))
        answer = input("What does GPU stand for? ").lower()
        if answer != "graphics processing unit":
            print("That's incorrect, please try again.")
            print("Your score: " + str(score))
            answer = input("What does GPU stand for? ").lower()
        elif answer == "graphics processing unit":
                print("Congratulations! See you in the next game.")
                score += 1
                print("Your score: " + str(score))
                quit()





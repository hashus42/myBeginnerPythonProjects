import random

def main():
    type_of_range = input("Type a number: ")

    a_number = type_of_range.isdigit()


    if a_number == False:
        print("Please enter a number.")
        main()
    elif a_number == True:
        r = random.randrange(0, int(type_of_range))

        def main2(x):
            t1 = "Guess my number it is between 0 and " + str(type_of_range) + "(includes 0 and " + str(type_of_range) + "): "
            t2 = "Try to guess my number again: "
            answer = input(x)
            if answer.isdigit() == False:
                        print("Please enter a number.")
                        main2(t1)
            while answer:
                if int(answer) > r:
                    print("Your guess is greater than my number.")
                    answer = input("Try to guess my number again: ")
                    if answer.isdigit() == False:
                        print("Please enter a number.")
                        main2(t2)
                if int(answer) < r:
                    print("Your guess is smaller than my number.")
                    answer = input("Try to guess my number again: ")
                    if answer.isdigit() == False:
                        print("Please enter a number.")
                        main2(t2)
                if int(answer) == r:
                    print("Congratulations, you guessed correct number!")
                    quit()
        main2("Guess my number it is between 0 and " + str(type_of_range) + "(includes 0 and " + str(type_of_range) + "): ")
main()




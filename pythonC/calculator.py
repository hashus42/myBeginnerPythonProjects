# def main():
#     while True:
#         firstValue = input("Please enter the first value: ")
#         operation = input("Please enter the operation: ")
#         secondValue = input("Please enter the second value: ")
#         print(str(firstValue) + str(operation) + str(secondValue) + " = " + str(eval(f"{firstValue}{operation}{secondValue}")))
#         again = input("Do you want to operate again?(yes or no) ")
#         if not again.lower().startswith("y"):
#             break
#
# print("Goodbye!")
# main()

def main():
    while True:
        operation = ""
        if not operation.isdecimal():
            operation = input("Enter the operation: ")
            print(" = " + str(eval(operation)))

        again = input("Do you want to calculate again? ")
        if not again.lower().startswith("y"):
            break

    print("Goodbye!")

main()
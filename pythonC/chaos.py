def chaos():

    nothing = eval(input("Enter the money: "))
    annualPercentageRate = eval(input("Enter the interest rate: "))
    yearNum = eval(input("Enter that how many years money will stay in the account: ")) + 1

    for i in range(yearNum):
        nothing = nothing * (annualPercentageRate + 1)
    print(nothing)
chaos()
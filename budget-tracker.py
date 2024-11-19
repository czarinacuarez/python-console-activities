def border():
    print("\n********************************************************************************************************************************************************************")

def start():
    print("\n************************************************************************** Expenses Tracker ************************************************************************")

    print("Welcome to the Oura Kingdom! I see that you are new here. What is your name?")

    # .capitalize() is used to capitalize the first letter of an user input.
    name = input("Name: ").capitalize()
    print(
        "\n\tHello " + name + ", You are chosen by Queen Hermione to be sent to Hogwarts School of Witchcraft and Wizardry, granting you a scholarship due to your potential. "
                             "\nAn amount of 20,000 gold will be given to you as a monthly allowance. Since you live quite far from Hogwarts, we have reserved a room for you in the boarding"
                             "\nhouse inside the campus which costs 4,000 gold monthly. To make sure that you at least eat everyday, we have arranged the meal plan subscription in the cafeteria"
                             "\nfor you which costs 300 gold per day. If you compute the total default expenses which are housing, and food and drink, you still have some allowance "
                             "\nfor other things like transportation, healthcare, leisure, and school. But remember that you only have exactly 20,000 gold for all your expenses monthly,  "
                             "\nso you have to make sure that you don’t overspend. Let me help you keep track of your expenses.")

def end(End):
    totalMoney = 0
    for cash in totalCash:
        totalMoney+=cash

    totalExpenses = 0
    for exp in expenses:
        totalExpenses+= exp

    left = totalMoney - totalExpenses
    if left < 0 :
        left = 0

    #str method is used to convert an int data type to string.
    if End == 0:
        print("\nAt the end of Day " + str(Day) + ", you have " + str(balance) + " gold left.")

    # round is used in order to round of the number, and it also included digits wherein you can round off the number based on
    # it's decimal places.

    elif End == 1:
        print("\n..." + str(dayLeft) +" days have passed...\n")
        print("\nAt the end of " + str(Day)  +", you have " + str(balance)+ " gold left."
              "\n\tFood and Drink ( "+ str(round(foodAndDrink / monthlyWholeBalance * 100,2)) +"% ) : "+ str(foodAndDrink) +
              "\n\tTransportation ( "+ str(round(transportation / monthlyWholeBalance * 100,2)) + "% ): " + str(transportation) +
              "\n\tHealthcare ( "+ str(round(healthcare / monthlyWholeBalance * 100,2)) +"% ): " + str(healthcare) +
              "\n\tHousing and Utilities ("+ str(round(housingAndUtilities / monthlyWholeBalance * 100,2)) +"% ): " + str(housingAndUtilities) +
              "\n\tLeisure ( "+ str(round(leisure / monthlyWholeBalance * 100,2)) + "% ): " + str(leisure) +
              "\n\tSchool ( "+ str(round(school / monthlyWholeBalance * 100,2)) +"% ): " + str(school))

    elif End == 2:
        print("\n\tOn day " + str(Day) + ", you quit Hogwarts. During your entire stay, Queen Hermione"
          "\nhas bestowed you a total of "+ str(totalMoney) + " . You spent a total of "+ str(totalExpenses) +" which is "
          "\n"+ str(round(totalExpenses/totalMoney * 100,2)) + " % of the total money you received. You are left with "+ str(left)+" gold.")

    border()

def out():
        print("\nOh no!"
          "\nYou ate the meals without paying."
          "\nHogwarts is no place for thieves."
          "\nThe Queen is greatly disappointed."
          "\nThe scholarship is now cancelled.")

def displayCurrentRecords():

    print("\nDay " + str(Day) +
          "\nBalance: " + str(balance) +
          "\nFood and Drink: " + str(foodAndDrink) +
          "\nTransportation: " + str(transportation) +
          "\nHealthcare: " + str(healthcare) +
          "\nHousing and Utilities: " + str(housingAndUtilities) +
          "\nLeisure: " + str(leisure) +
          "\nSchool: " + str(school))



def addAmount():

    # exception handling - Value Error is used in order to detect errors when there is an error value when converting the user input into int
    inputt = True
    while inputt == True:
        try:
            amount = int(input("Enter the amount: "))
            assert amount > 0, "Amount must be greater than zero."
        except AssertionError as e:
            print(e)
        except ValueError:
            print("Only enter numbers. Try Again.\n")
        else:
            inputt = False
            print("\nExpenses Successfully Added.")
            expenses.append(amount)
            return amount


if __name__ == "__main__" :
    start()
    border()
    #START OF BUDGETING
    Day = 1
    DayinMonth = 1
    balance = 0
    foodAndDrink = 0
    transportation = 0
    healthcare = 0
    housingAndUtilities = 0
    leisure = 0
    school = 0

    # TOTAL MONEY GIVEN AND EXPENSES
    totalCash = []
    expenses = []

    startOfDayMonth = True
    while startOfDayMonth == True:
        #Start of the Month
        DayinMonth = 1
        monthlyWholeBalance = 20000
        balance += monthlyWholeBalance

        # Adding the monthlyWholeBalance value in the totalCash list.
        totalCash.append(monthlyWholeBalance)

        #RESET EXPENSES
        foodAndDrink = 0
        transportation = 0
        healthcare = 0
        housingAndUtilities = 0
        leisure = 0
        school = 0

        #Deducting 4000 from the balance while adding it to housing and utilities expenses
        balance -= 4000
        housingAndUtilities += 4000

        # Adding 4000 in the expenses list.
        expenses.append(4000)

        # set the day variable to True so that it can be used in while function and continue the loop.
        # this loop will end if the value is changed to False, since break -   continue- pass -quit - exit statements are not allowed.
        day = True
        while day == True:
            #Start of the Day
            balance -= 300
            foodAndDrink += 300
            expenses.append(300)

            if balance <= 0 :
                out()
                end(2)
                day = False
                startOfDayMonth = False

            else:
                menu = True
                displayCurrentRecords()
                while menu == True:
                    print("\nWhat would you like to do today? "
                          "\n1 - add Food and Drink expenses"
                          "\n2 - add Transportation expenses"
                          "\n3 - add Healthcare expenses"
                          "\n4 - add Housing and Utilities expenses"
                          "\n5 - add Leisure expenses"
                          "\n6 - add School expenses"
                          "\n7 - end the Day"
                          "\n8 - end the Month"
                          "\n0 - exit the program")

                    choice = input("Enter the number of your choice: ")

                    if choice == "1":
                        # since the addAmount method has a return, we have used this statement so that the returned value in the method
                        # will be stored in the amount variable.
                        amount = addAmount()
                        foodAndDrink += amount
                        balance -= amount

                    elif choice == "2":
                        amount = addAmount()
                        transportation += amount
                        balance -= amount

                    elif choice == "3":
                        amount = addAmount()
                        healthcare += amount
                        balance -= amount

                    elif choice == "4":
                        amount = addAmount()
                        housingAndUtilities += amount
                        balance -= amount

                    elif choice == "5":
                        amount = addAmount()
                        leisure += amount
                        balance -= amount

                    elif choice == "6":
                        amount = addAmount()
                        school += amount
                        balance -= amount

                    elif choice == "7":
                        if DayinMonth == 30:
                            end(1)
                            menu = False
                            day = False

                        elif balance <= 0:
                            out()
                            end(2)
                            menu = False
                            day = False
                            startOfDayMonth = False

                        else:
                            end(0)
                            Day += 1
                            DayinMonth += 1
                            menu = False


                    elif choice == "8":
                        dayLeft = 30 - DayinMonth
                        Day += dayLeft
                        balance -= dayLeft * 300
                        foodAndDrink += dayLeft * 300
                        expenses.append(dayLeft * 300)

                        if balance <= 0:
                            print("\n..." + str(dayLeft) + " days have passed ...")
                            out()
                            end(2)
                            menu = False
                            day = False
                            startOfDayMonth = False

                        else:
                            end(1)
                            Day += 1
                            menu = False
                            day = False

                    elif choice == "0":
                        end(2)
                        menu = False
                        day = False
                        startOfDayMonth = False

                    else:
                        print("Invalid Choice, Please Try Again.")



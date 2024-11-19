class main:

    def function(self):
        self.a = "|                                                       0:00                                                               |"
        self.b = "|                                                       Cafe                                                               |"
        self.c = "|                         Menu                             |"
        self.d = "|                       APPETIZER                          |"
        self.e = "|      CODE      |    Order Menu       |       Price       |"
        self.f = "|      FF1       |    French Fries     |      ₱135.00      |"
        self.g = "|      CW1       |    Chicken Wings    |      ₱155.00      |"
        self.h = "|      B1        |    Buffalo          |      ₱155.00      |"
        self.i = "|      SHG       |    Soy Honey Garlic |      ₱155.00      |"
        self.j = "|      N1        |    Nachos           |      ₱165.00      |"
        self.k = "|                        PASTA                             |"
        self.l = "|      TP        |    Tuna Pesto       |      ₱165.00      |"
        self.m = "|      B2        |    Bolognese        |      ₱170.00      |"
        self.n = "|      AC1       | Authentic Carbonara |      ₱180.00      |"
        self.o = "|      CC1       |    Creamy Carbonara |      ₱185.00      |"
        self.p = "|                       SANDWICH                           |"
        self.q = "|      C1        |    Clubhouse        |      ₱185.00      |"
        self.r = "|                        Coffee Menu                       |"
        self.s = "|      B3        |     Barako          |  S(₱85)   L(₱90)  |"
        self.t = "|      B4        |     Americano       |  S(₱80)   L(₱85)  |"
        self.u = "|      B5        |     Caffe Latte     |  S(₱90)   L(₱100) |"
        self.v = "|      B6        |     Spanish Latte   |  S(₱90)   L(₱100) |"
        self.x = "|      B7        |     Sea Salt Latt   |  S(₱110)  L(₱110) |"
        self.y = "|      B8        |     Dark Mocha      |  S(₱100)  L(₱110) |"
        self.z = "|      B9        |     Matcha Latte    |  S(₱100)  L(₱110) |"
        self.aa ="|      B0        |     Chocolate       |  S(₱90)   L(₱100) |"
        self.ab ="|      ADD       |     Add-Ons         |        ₱30        |"

    def funtionPrint(self):
        print("╭────────────────────——————————————————————————————————————————————————————————————————————————————————────────────────────╮")
        print(self.a, "\n"+self.b)
        print("╰────────────────────—————————————————————————————————————————————————————————————————————————————————─────────────────────╯")
        print("╭────────────────────——————————————————────────────────────╮\t╭────────────────────——————————————————────────────────────╮")
        print(self.c, "\t"+self.r)
        print("|——————————————————————————————————————————————————————————|\t|────────────────╮─────────────────────╮───────────────────|")
        print(self.d,"\t|      CODE      |     Order Menu      |       Prices      |")
        print("|                                                          |","\t"+self.s)
        print(self.e,"\t"+self.t)
        print(self.f,"\t"+self.u, "\n"+self.g,"\t"+self.v, "\n"+self.h,"\t"+self.x, "\n"+self.i,"\t"+self.y,"\n"+self.j, "\t"+self.z)
        print("|────────────────╯─────────────────────╯———————————————————|","\t"+self.aa)
        print(self.k,"\t"+self.ab)
        print("|                                                          |","\t╰────────────────╯─────────────────────╯───────────────────╯" )
        print(self.l, "\n"+self.m,"\n"+self.n,"\n"+self.o)
        print("|────────────────╯─────────────────────╯———————————————————|")
        print(self.p)
        print("|                                                          |")
        print(self.q)
        print("╰────────────────╯─────────────────────╯───────────────────╯")


cl = main()
cl.function()
cl.funtionPrint()

# INVENTORY [VARIABLE]
c_order = []
c_total = []
c_quantity = []
c_sizes = []
c_code =[]

o_order = []
o_total = []
o_quantity = []
o_code = []

c_cash = []

others = {
    "FF1": [135.00,"French Fries"],
    "CW1": [155.00,"Chicken Wings"],
    "B1": [155.00, "Buffalo"],
    "N1": [165.00, "Nachos"],
    "SHG": [155.00, "Soy Honey Garlic"],
    "TP": [165.00, "Tuna Pesto"],
    "B2": [170.00, "Bolognese"],
    "AC1": [180.00, "Authentic Carbonara"],
    "CC1": [185.00, "Creamy Carbonara"],
    "C1": [185.00, "Clubhouse"]
}

coffee = {
    "B3S": [80.00,"Barako","S"],
    "B4S": [80.00,"Americano","S"],
    "B5S": [90.00,"Caffe Latte","S"],
    "B6S": [90.00, "Spanish Latte","S"],
    "B7S": [100.00, "Sea Salt Latt","S"],
    "B8S": [100.00,"Dark Mocha","S"],
    "B9S": [100.00, "Matcha Latte","S"],
    "B0S": [90.00, "Chocolate","S"],
    "B3L": [85.00, "Barako", "L"],
    "B4L": [85.00, "Americano", "L"],
    "B5L": [100.00, "Caffe Latte", "L"],
    "B6L": [100.00, "Spanish Latte", "L"],
    "B7L": [110.00, "Sea Salt Latte", "L"],
    "B8L": [110.00, "Dark Mocha", "L"],
    "B9L": [110.00, "Matcha Latte", "L"],
    "B0L": [100.00, "Chocolate", "L"],
    "ADD":[30.00,"Add-Ons","S/L"]
}

def receipt():
    sumcoffee = sum(c_total)
    sumothers = sum(o_total)
    total = sumcoffee + sumothers

    print("                                           ")
    print("                   0:00                    ")
    print("                   CAFE                    ")
    print("-------------------------------------------")
    print("             SUMMARY OF ORDERS             ")
    print("-------------------------------------------")
    print("Item\t\t\tQuantity\t\t\tPrice")

    if not c_total:
        for i in range(len(o_code)):
            print(str(o_code[i]) + "\t\t\t\t\t" + str(o_quantity[i]) + "\t\t\t\t" + str(o_total[i]))
        print("-------------------------------------------")
        print("Amount                             ", sumothers)
    else:
        for i in range(len(c_code)):
            print(str(c_code[i])+"\t\t\t\t\t"+str(c_quantity[i])+"\t\t\t\t"+str(c_total[i]))

    print("-------------------------------------------")
    print("Amount                             ",sumcoffee)
    if not o_total:
        print("-------------------------------------------")
        print("Total                              ",total)
    else:
        print("-------------------------------------------")
        for i in range(len(o_code)):
            print(str(o_code[i]) + "\t\t\t\t\t" + str(o_quantity[i]) + "\t\t\t\t" + str(o_total[i]))
        print("-------------------------------------------")
        print("Amount                             ", sumothers)

    print("-------------------------------------------")
    print("Total                              ", total)
    print("Cash                               ", str(c_cash[0]))
    print("Change                             ", str(c_cash[1]))
    print("-------------------------------------------")
    print("         THANK YOU FOR DROPPING BY         ")
    exit()

def pay():
    sumcoffee = sum(c_total)
    sumothers = sum(o_total)
    total = sumcoffee + sumothers
    print("                                                       ORDER RECORD                                                         ")
    print( "                                                      ────────────                                                         ")

    if c_order and o_order:
        print("                             Coffee Name/s: ", str(c_order))
        print("                             Quantity: ", str(c_quantity))
        print("                             Sizes: ", str(c_sizes))
        print("                             Amount: ", str(c_total))
        print("\n                             Others Name/s: ", str(o_order))
        print("                             Quantity: ", str(o_quantity))
        print("                             Amount: ", str(o_total))
        print("\n                             Total: ",total)

    elif not c_order:
        print("\n                             Others Name/s: ", str(o_order))
        print("                             Quantity: ", str(o_quantity))
        print("                             Amount: ", str(o_total))
        print("\n                             Total: ", str(total))

    elif not o_order:
        print("                             Coffee Name/s: ", str(c_order))
        print("                             Quantity: ", str(c_quantity))
        print("                             Sizes: ", str(c_sizes))
        print("                             Amount: ", str(c_total))
        print("\n                             Total: ", str(total))

    print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")

    cash = int(input("Kindly enter payment in cash: "))
    if cash < total:
        print("Invalid Amount of Cash. Try Again")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        pay()

    else:
        change = cash - total
        c_cash.append(cash)
        c_cash.append(change)
        print("Payment Successfully!")
        print("\nPrinting Receipt...")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        receipt()


def others_order():
    try:
        print("How many types of others would you like to order? Press 0 if none:  ")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        inp = int(input("> "))
    except ValueError:
        print("Invalid Input")
    else:
        if inp > 0:
            i = 0
            print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")

            while i < inp:


                choice = input("Code: ")
                try:
                    q = int(input("Quantity: "))
                except ValueError:
                    print("Invalid Input")
                else:
                    if (choice in others):
                        amt = int(float(others[choice].__getitem__(0)))
                        total_ = amt * q
                        o_order.append(others[choice].__getitem__(1))
                        o_total.append(total_)
                        o_quantity.append(q)
                        o_code.append(choice)
                        i = i + 1
                    else:
                        print("The code you've entered is incorrect. Try Again")
                        i = i + 0

            print("\nOrder Successfully listed!")
        elif inp == 0:
            rep()
        else:
            print("Invalid Input")

def coffee_order():
    try:
        print("How many types of coffee would you like to order? Press 0 if none:  ")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        inp = int(input("> "))
    except ValueError:
        print("Invalid Input")
    else:
        if inp > 0:
            i = 0
            print("────────────────────————————————————————————————————────———————————————————————————————————————————————————────────────────────")
            print(
                "                                                           NOTICE!                                                             ")
            print(
                "When entering the item code, kindly follow this format:"
                "\n'B3S' = if B3 Small , 'B3L' = if B3 Large\nJust add 'S' for small size and 'L' for large size")
            print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")

            while i < inp:
                choice = input("Code: ")
                try:
                    q = int(input("Quantity: "))
                except ValueError:
                    print("Invalid Input")
                else:
                    if (choice in coffee):
                        amt = int(float(coffee[choice].__getitem__(0)))
                        total_ = amt * q
                        c_order.append(coffee[choice].__getitem__(1))
                        c_total.append(total_)
                        c_quantity.append(q)
                        c_sizes.append(coffee[choice].__getitem__(2))
                        c_code.append(choice)
                        i = i + 1
                    else:
                        print("The code you've entered is incorrect. Try Again.")
                        i = i + 0

            print("\nOrder Successfully listed!")
        elif inp == 0:
             rep()
        else:
            print("Invalid Input")

def rep():

    ex = "x"

    while True:
        print("────────────────────————————————————————————————————────———————————————————————————————————————————————————────────────────────")
        print("Select the following choices you wished to do:"
           "\n[1] ORDER COFFEE"
           "\n[2] ORDER OTHERS ( APPETIZERS / PASTA / SANDWICH )"
           "\n[3] PAY (CASH ONLY)"
           "\n[4] SHOW MENU"
           "\n[x] EXIT")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        choose = input("> ")
        print("──────────────────────────—————————————————————————————————————————————————————————————————————————————————────────────────────")
        if choose == "1":
            coffee_order()

        elif choose == "2":
            others_order()

        elif choose == "3":
            if not c_total and not o_total:
                print("No Order")
            else:
                pay()

        elif choose == "4":
            cl = main()
            cl.function()
            cl.funtionPrint()

        elif choose == ex:
            print("Thank You")
            break

        else:
            print("Invalid Input")


pri = rep()

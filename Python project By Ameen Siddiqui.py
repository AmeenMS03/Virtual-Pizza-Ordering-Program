name=input("\nPlease enter your name.   ")
welcome= int(input("\nWelcome to Sidd's Pizza " +name+ "! Please select the following options to proceed. \n 1.MENU \n 2.Order a Pizza \n 3.Exit \n \n"))
price=0
no_pizzas=0
toppings_limit=0

while welcome>0:
    welcome_command=1
    while welcome==1:
        menu= str("Pepperoni Pizza:   AED 60 Code(P) \nMargherita Pizza:  AED 65 Code(M) \nVegetarian Pizza:  AED 40 Code(V) \nNeapolitan Pizza:  AED 54 Code(N) \n\nTOPPINGS ASSORTED -------------------------\n\n(First 3 toppings are free. Others add 4 AED each)\n\nO= Olives    T= Tomatoes   M= Mushrooms   J= Jalapenos")
        welcome=int(input("\nMENU CARD -------------------------\n \n" + menu +"\n \nTo order pizza directly, type 2.\n\n"))
        if(welcome==2):
            break

    order_flavors = []
    order_size = []
    order_price = []
    order_toppings=[]
    topping_price = []
    pizza_amount=[]
    topping_count = []

    while welcome==2:
        print("\nPLEASE BOOK YOUR ORDER-------------------------")
        flavor = int(input("\nEnter Pizza Flavor\n1. Pepperoni Pizza:   Code(1)\n2. Margherita Pizza:   Code(2)\n3. Vegetarian Pizza:   Code(3)\n4. Neapolitan Pizza:   Code(4)\n\n"))
        no_pizzas=int(input("\nPlease enter the amount of selected flavor: \n\n"))
        order= str(input("\nL=Large 100AED,     M=Medium 60AED,     S=Small 40AED\n\n"))
        
        if no_pizzas>0:
            pizza_amount.append(no_pizzas)
        else:
            break

        if flavor == 1:
            print("\nPepperoni Pizza selected!\n")
            order_flavors.append("Pepperoni ")
        elif flavor == 2:
            print("\nMargherita Pizza selected!\n")
            order_flavors.append("Margherita")
        elif flavor == 3:
            print("\nVegetarian Pizza selected!\n")
            order_flavors.append("Vegetarian")
        elif flavor == 4:
            print("\nNeapolitan Pizza selected!\n")
            order_flavors.append("Neapolitan")
        else:
            print("Incorrect number entered.")
            order_flavors.append("No Flavour added")

        if order.capitalize() == "L":
            order_size.append("Large ")
            price+=100*no_pizzas
            order_price.append(100*no_pizzas)
            print("\nLarge Pizza selected!\n")
        elif order.capitalize() == "M":
            order_size.append("Medium")
            price+=60*no_pizzas
            order_price.append(60*no_pizzas)
            print("\nMedium Pizza selected!\n")
        elif order.capitalize() == "S":
            order_size.append("Small ")
            price+=40*no_pizzas
            order_price.append(40*no_pizzas)
            print("\nSmall Pizza selected!\n")
        else:
            print("Incorrect letter entered.")
            order_size.append("No")

        num_of_toppings = 0
        while(1):
            toppings = str(input("\nPlease select a topping. You can choose upto 3 for free, additional will be charged\n\t O= Olives    T= Tomatoes   M= Mushrooms   J= Jalapenos 4=Exit\n\n"))

            if toppings.upper() =='O':
                print("\nOlives topping selected\n")
                order_toppings.append("Olives  ")
            elif toppings.upper() =='T':
                print("\nTomato topping selected\n")
                order_toppings.append("Tomato  ")
            elif toppings.upper() =='M':
                print("\nMushroom topping selected\n")
                order_toppings.append("Mushroom")
            elif toppings.upper() =='J':
                print("\nJalapeno topping selected\n")
                order_toppings.append("Jalapeno")
            elif toppings.upper()=="4":
                topping_count.append(num_of_toppings)
                break
            else:
                print("Incorrect topping entered.")

            num_of_toppings += 1
            # used for adding amount of additional toppings in topping_price_list
            if (num_of_toppings > 3):
                topping_price.append(3)
                price += 3
            else:
                topping_price.append(0)


        another= str(input("Do you wish to order another pizza? (yes/no)\n\n"))
        if another.lower()=="no":
            welcome = 3
            print("\nTHANK YOU FOR ORDERING!")
            print("----------------------------------------------------------------------------")
            print("                          YOUR ORDER RECIPT IS")
            print("----------------------------------------------------------------------------")
            print("Flavours           No. of Pizzas            Size               Price")
            print("----------------------------------------------------------------------------")
            for x in range(0, len(order_flavors)):
                print("\n"+str(order_flavors[x])+"\t\t\t\tx"+str(pizza_amount[x])+"\t\t\t\t\t"+str(order_size[x])+"\t\t\t\t"+str(order_price[x]))
                print("\t\t\t\t\t\t\t\t\t\t -----------------------------------")
                print("\t\t\t\t\t\t\t\t\t\t  Order Toppings\t  Topping Price")
                print("\t\t\t\t\t\t\t\t\t\t -----------------------------------")
                for y in range(0, topping_count[x]):
                    print("\t\t\t\t\t\t\t\t\t\t\t"+str(order_toppings[y])+"\t\t\t\t"+str(topping_price[y]))
            print("----------------------------------------------------------------------------")
            print("TOTAL AMOUNT TO BE PAYED: \t\t\t\t\t|\t"+str(price)+"\t|")
            print("----------------------------------------------------------------------------")
            print("\n\nThank you for eating at Sidd's Pizza "+name+"\nPlease visit again!")
            print("See you later!")
            quit()
    else:
        print("You have entered an incorrect command. Please try again.")
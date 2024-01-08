

# create 'home menu' for users to select options from

checkout = False

print("-"*80)
print("\n Welcome to the Paws N Cart store! \n")            
print("-"*80)

shop_cart = []                                  # sets up shopping cart as emtpy list before opening while loop
cart_prices = []

while checkout == False:

    items_in_cart = len(shop_cart)

    if items_in_cart == 0:                      # doesn't print full shopping cart if there is nothing in it
        print("")
        print("-"*80)
        print("\nYour shopping cart is currently empty.\n")
        print("-"*80)
    else:
        print("-"*80)                           # prints full shopping cart
        print("\nThis is your current shopping cart: \n")
        for cart_item in range(0, items_in_cart):
            print(f"{shop_cart[cart_item]} \t £{"%.2f" % cart_prices[cart_item]}")
        print("")
        print("-"*80)


    print("\nPlease select an option from the list below: \n")
    print("1. \t Add an item to your cart")
    print("2. \t Remove an item from your cart")
    print("3. \t View the total cost of your cart")
    print("4. \t Checkout \n")

    user_choice = int(input("Please enter your selection here: "))

    print("")
    print("-"*80)
    print("")

    if user_choice == 1:
        new_item = input("What item would you like to add?: ")
        shop_cart.append(new_item)
        item_price = float(input("How much does this item cost in £?: "))
        cart_prices.append(item_price)

        print("\n")
        print("-"*80)
        print(f"\n{new_item} has been added to your cart successfully.\n")


    elif user_choice == 2:
        removal_item = input("Please enter the item you would like to remove: ")
        if removal_item in shop_cart:
            removal_pos = shop_cart.index(removal_item)
            shop_cart.pop(removal_pos)
            cart_prices.pop(removal_pos)
            print(f"{removal_item} has been successfully removed from your cart.")
        else:
            print(f"{removal_item} not found in your cart.\n")

    elif user_choice == 3:
        total_cost = sum(cart_prices)
        print(f"The total cost of the items in your cart is currently £{"%.2f" % total_cost}.\n")

    elif user_choice == 4:
        print("Thank you for shopping with Paws N Cart!")
        checkout = True
    
    else:
        print("\nPlease choose a number 1-4: ")

    


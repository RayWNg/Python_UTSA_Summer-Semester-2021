'''
Student Name: Raymond Ng
Exam 03
'''

choice = 0

# Ensures the last option to choose from in the menu is the exit option.
Exit = 11
            
# Create function for menu options.
def show_menu(options):
    ''' this is a function that takes parameter options and returns choice
    choice is an input that will be used in the while loop
    '''
    print('\nPlease choose from the following choices:')
    for i in range(len(options)):
        print(i + 1, ')', options[i])
    choice = int(input('\nEnter your choice here: '))
    return choice


# Create a dictionary with the available food items.
food_items = {'Single meat hamburger meal': 7.14,
            'Double meat hamburger meal': 8.39,
            'Bacon cheeseburger meal': 8.44,
            'Junior hamburger meal': 5.04,
            'Chicken sandwich meal': 7.74,
            'Chicken strip meal': 7.19,
            'French fries': 2.39,
            'Onion rings': 2.99,
            'Soft drink': 2.14}

# Menu will display following options to user.
menu = []
menu.append('Display all the Food Items and Prices')
menu.append('Display how many Food Items exists')
menu.append('Display all the Food Items')
menu.append('Display all the Food Items with Prices under $7.50')
menu.append('Confirm that a Food Item is an option')
menu.append('Look up a specific Food Item\'s information')
menu.append('Add a Food Item and its Price to the available Item options')
menu.append('Change a Food Item\'s Price')
menu.append('Remove a Food Item and its Price from the dictionary')
menu.append('Remove all Food Items and Prices from the Food Item options')
menu.append('Exit the program menu\n')

# function will display all food items and their prices.
def display_food_items_prices():
    # Iterating over food items in dictionary.
    for items in food_items:
        # Displays all Food Items and their prices.
        print(items +':','$'+ str(food_items[items]))
    return

# function will display all food items without prices.
def display_food_items():
    for items in food_items:
        # Displays all the food item names available to user.
        print(items)
    return

# function will check if item exists in dictionary.
def confirm_food_item():
# Asks user which item he/she/they would like to confirm.
        food = input('Which food items do you want to confirm? ')
        # Checks if food item is in dictionary.
        if food in food_items:
            # Lets user know food item is available in dictionary.
            return (f'{food} is available.')
        return 'Food Item not found'

# function will check how many food item exists in dictionary.
def items_in_food_list():
    return len(food_items)

    
# Begin loop.
while choice != Exit:
    choice = show_menu(menu)
    print()
    
    # If user selects option 1, display all Food Items and Prices.
    if choice == 1:
        print('Below are all the Food Items, and their prices, available:')
        display_food_items_prices()

    # If user selects option 2, display how many Food Items exists in dictionary.
    elif choice == 2:
        # Lets user know that food item exists in the dictionary.
        print(items_in_food_list(), 'food items exist.')
  
    # If user selects option 3, display all Food Items.
    elif choice == 3:
        display_food_items()

    # If user selects option 4, display all Food Items under $7.50.
    elif choice == 4:
        print('Food Items under $7.50 are: ')
        print()
        for items in food_items:
            # Will check if the price of food item is less than $7.50.
            if food_items[items] < 7.50:
                # Displays all food items under $7.50 to user.
                print(items)
  
    # If user selects option 5, confirm that a Food Item is an option.
    elif choice == 5:
        print(confirm_food_item())
  
    # If user selects option 6, look up a specific food item's information.
    elif choice == 6:
        # Asks user which food item he/she/they would like information.
        food = input('Which food items do you want to look for? ')
        print()
        # Will check if food item is in the dictionary.
        if food in food_items:
            # Diplays food item and its price to user.
            print(f'Price of {food} is ${food_items[food]}')
        else:
            print('Food Item not found.')
  
    # If user selects option 7, add a food item and its price to item options.
    elif choice == 7:
        # Asking user to enter food name and storing it in variable food.
        food = input('Enter Food Item name to be added: ')
        # Will check if food item is already in dictionary.
        if food in food_items:
            # Lets user know the food item already exists in dictionary.
            print(f'{food} already exists.')
        else:
            # Store price input in price.
            price = float(input('Enter Food Item price: '))
            # Adds food and price to dictionary.
            # does this look correct? food : price
            # if yes, add
            print('Please confirm, your food item to be added is', food, 'and its price is $', price)
            check = int(input('Press 1 to confirm, or Press 2 to cancel: '))
            if check == 1:
                food_items[food]=price
            # Lets user know item has been added to dictionary.
                print('Food Item added.')
            # If no, then don't add it.
            else:
                print("Food Item not added.")
  
    # If user selects option 8, change a Food Item's price.
    elif choice == 8:
        
        # Asking user to enter food name and storing it in variable food.
        food = input('Enter food item name whose price you want to change: ')
        
        # Will check if food item is in dictionary.
        if food in food_items:
            
            # Store price input in price.
            price = float(input('Enter Food Item\'s new price: '))
            print()
            print('Please confirm new price:', price)
           
            # Lets user know the foot item's price has been updated.
            check = int(input('Press 1 to confirm, or Press 2 to cancel: '))
            if check == 1:
                food_items[food]=price
            # Lets user know item has been added to dictionary.
                print('Price of Food Item has been updated.')
            # If no, then don't add it.
            else:
                print("No change in price was made on Food Item.")
  
    # If user selects option 9, remove a food item and its price.
    elif choice == 9:
        # Asking user to enter food name and storing it in food.
        food = input('Enter Food Item name to be removed: ')
        print()
        if food in food_items:
            print('Please confirm item to be removed: ', food)
            # Lets user know the foot item's price has been updated.
            check = int(input('Press 1 to confirm, or Press 2 to cancel: '))
            if check == 1:
                # Deletes food item from dictionary
                del food_items[food]
                # Lets user know item has been added to dictionary.
                print('Food Item has been removed.')
            # If no, then don't add it.
            else:
                print("Food Item was not removed.")
  
    # If user selects option 10, remove all food items and prices from food
    # item options.
    elif choice == 10:
        # Removes all items from the dictionary.
        food_items.clear()
        print('All Food Items have been removed.')
    
    # If user selects option 11, exits the program.
    elif choice == 11:
        
        # Lets user know he/she/they has exited the program.
        print('Goodbye!')
        
    
    # If user inputs an erroneous option, i.e., if user enters option 12 
    # program will let user know that it is not a valid option.
    else:
        print('NOT A VALID CHOICE!')
# Student Name: Raymond Ng
# Exam 2


# Items/Integers assigned to the variable my_integers_list.
my_integers_list = [1,3,5,7,9,2,4,6,8,0,11,21,31,41,51,61,71,81,91]

# Define menu function, displays menu options.
def display_menu():
    print('_____________________Menu_____________________')
    print('Please choose from the following menu options: ')
    print()
    print(' 1) Display the items in the list.')
    print(' 2) Display how many items are in the list.')
    print(' 3) Tell the user if an item exists in the list.')
    print(' 4) Get the index number of an item.')
    print(' 5) Add an item to list (integers).')
    print(' 6) Remove an item from the list.')
    print(' 7) Display the item that has the maximum value.')
    print(' 8) Display the item that has the minimum value.')
    print(' 9) Display the average of all the items.')
    print('10) Display the total (sum) of all the items.')
    print('11) Copy the list into a new list and display both lists.')
    print('12) Exit the menu.')


# Function will remove an item from the list.
def remove_integer():
    
    integer = int(input('Enter item: '))
    
    if integer in my_integers_list:
        
        # Removes item/integer from my_integers_list.
        my_integers_list.remove(integer)
        
        # Lets the user know item/integer has been removed from list.
        return 'Item has been removed from the list.'
    
    # Lets user know item/integer does not exist in list.
    return 'Item not found.'

# Function will add an item to list (integers).
def add_integer():     
    
    # Getting user input and storing it into integer.
    integer = int(input('Enter item: '))
    
    # Adds item/integer to integer_list.
    my_integers_list.append(integer)     
    
    # Confirms item/integer was added to my_integers_list.
    return 'Item has been added to the list.'


# Function tells user if an item/integer exists in the list.
def check_integer(): 
    
    # Getting user input and storing it into integer.    
    integer = int(input('Enter item: '))
    
    if integer in my_integers_list:
        
        return 'The item exists in the list.'
    
    # Lets user know item/integer does not exist in list.
    return 'Item not found.'


# Validate if user input is an integer and between 0 and 12.
def validate(prompt):
    if not prompt.isdigit():
        return False
    elif int(prompt) < 0 or int(prompt) > 12:
        return False
    return True


# Define main function.
def main():
   
    # Greeting
    # The greeting is placed before the loop so that it will not display to
    # user every time the menu appears after selecting an option.
    print('****************   Welcome!   ****************')
    print()
    print('--------------Ray\'s Number List--------------')
    print()
    
    # Loop will validate each function corresponding to menu options.
    while True:

        # Call menu function
        display_menu()
        
        # Prompts user to choose an option from menu.
        menu_option = input('Input option here: ')

        # Identifies erroneous entries by user.
        # Lets user know entry made (or option selected) is not valid.
        # For example, if user enters "13", "13" is not an option; program will
        # display NOT A VALID INPUT!
        if not validate(menu_option):
            print('NOT A VALID INPUT!')
            print()
            
            # Continue loop.
            continue
        
        i = int(menu_option)
        
        # Menu Option 1) Display the items in the list.
        if i == 1:
            print('The list of integers: ', my_integers_list)
            print()
        
        # Menu Option 2) Display how many items are in the list.
        elif i == 2:
            # Return the length of list in my_integer_list.
            items_in_list = len(my_integers_list)
            # Displays total number of items in list.
            print('The number of items in list: ', items_in_list)
            print()
        
        # Menu Option 3) Tell the user if an item exists in the list.
        elif i == 3:
            # Call and display check_integer function.
            print(check_integer())
            print()

        # Menu Option 4) Get the index number of an item.
        elif i == 4:
            integer = int(input('Enter item: '))
            index = my_integers_list.index(integer)
            # Displays index number of item/integer.
            print('Index number of item: ', index)
            print()

        # Menu Option 5) Add an item to list (integers).
        elif i == 5:
            # Call and display add_integer function.
            print(add_integer())
            print()

        # Menu Option 6) Remove an item from the list.
        elif i == 6:
            # Call and displays remove_integer function.
            print(remove_integer())
            print()

        # Menu Option 7) Display the item that has the maximum value.
        elif i == 7:
            # Displays highest value in my_integers_list.
            print('Maximum value: ', max(my_integers_list))
            print()

        # Menu Option 8) Display the item that has the minimum value.
        elif i == 8:
            # Displays lowest value in my_integers_list.
            print('Minimum value: ', min(my_integers_list))
            print()

        # Menu Option 9) Display the item average of all the items.
        elif i == 9:
            # The sum of items in the assigned variable/list, item_list, will be 
            # divided by the total number of items/integers in list, 19.
            # Displays average to the nearest hundredths; limiting
            # output to two decimal places.
            print('Average of all items: ', round(sum(my_integers_list) / 19, 2))  
            print()

        # Menu Option 10) Display the total (sum) of all the items.
        elif i == 10:
            # Displays sum of items/integers.
            print('Sum of all items: ', sum(my_integers_list))
            print()

        # Menu Option 11) Copy the list into a new list and display both lists.
        elif i == 11:
            # Create a list with value.
            original_list = [my_integers_list]
            # Create a copy of original_list.
            copy_of_list =[] + original_list
            # Displays original list.
            print('Original: ', my_integers_list)
            # Displays copy of list.
            print('Copy: ', copy_of_list)
            print()
            
        # Menu Option 12) User exits program.
        elif i == 12:
            
            # Lets user know he/she/they has exited the program.
            print("Goodbye!")
            
            # Terminates loop.
            break

# Call the main function.
main()
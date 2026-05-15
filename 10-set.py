# This is a comment

"""

This is a multi-line comment
It can span multiple lines
And is very useful for explaining code

"""



# this is the calculation variale that will be used to calculate the number of hours in a given number of days
calculation_units = 24
# this is our unit of measurement
name_unit = "hours"

"""
    validate and execute is the main user defined function that is used to validate and execute the user input
    it takes one argument "num_of_days_element" which is the number of days entered by the user
    exit comment will exit the program
    unless the user enters a valid number the program will not execute
    if the user enters 0 the program will print "You entered 0, please enter a valid positive number"
    if the user enters a negative number the program will print "You entered a negative number, please enter a valid positive number"
    if the user enters a non-integer value the program will print "Your input is not a valid number. Don't ruin my program"
    
"""
def validate_and_execute():
    # Error Exception Handling
    try:
        user_input_number = int(num_of_days_element)
        # Conditions
        if user_input_number > 0:
            calculated_value = user_input_number * calculation_units
            print(f"{user_input_number} days is equal to {calculated_value} {name_unit}")
        
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")
        else: 
            print("You entered a negative number, please enter a valid positive number")
    # Exception Handling
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program")

"""
here is the main user  
we are calling the functions and executing them and view the resuts. 

"""

"""

SET 

- another built-in data type of python
- as with lists, used to store multiple items of data
- does not allow duplicate values

Nested function execution 

print(type(set(list_of_days)))

1. set(list_of_days)
    => imput: the user input array
    => Output: Return the converted set 

2. type(return_value_of_previous_func)
    => imput: the converted set
    => Output: returns the data type of the set

3. print(return_value_of_previous_func)
    => imput: the data type
    => Output: prints the value in the console

"""



user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter the number days in comma saparated values and i will convert all to hours  !: \n")
    list_of_days = user_input.split(", ")
    print(set(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()




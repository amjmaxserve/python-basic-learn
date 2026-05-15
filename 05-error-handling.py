
calculation_units = 24
name_unit = "hours"

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = user_input_number * calculation_units
            print(f"{user_input_number} days is equal to {calculated_value} {name_unit}")
        
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")
        else: 
            print("You entered a negative number, please enter a valid positive number")
        
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program")


user_input = input("Hey user, Enter a number of days and i will convert it to hours for you !: \n")
validate_and_execute()
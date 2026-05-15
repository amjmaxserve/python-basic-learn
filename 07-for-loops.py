
calculation_units = 24
name_unit = "hours"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = user_input_number * calculation_units
            print(f"{user_input_number} days is equal to {calculated_value} {name_unit}")
        
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")
        else: 
            print("You entered a negative number, please enter a valid positive number")
        
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter the number days in comma saparated values and i will convert all to hours  !: \n")
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
        


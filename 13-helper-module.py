def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24 } Hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} Minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} are {num_of_days * 24 * 60 * 60} Seconds"
    else:
        return "Unsupported Unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, Please enter a valid positive number")
        else:
            print("Your entered a -ve number , No converion for you")
    except ValueError:
        Print("Your input is not valid, please don't ruin my program")

user_input_message = "Hey user, please enter number of days and conversion unit: \n"
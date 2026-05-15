def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24 } Hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} Minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} are {num_of_days * 24 * 60 * 60} Seconds"
    else:
        return "Unsupported Unit"


def validate_and_execute():
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


user_input = ""
user_input = input("Hey user, please enter number of days and conversion unit: \n")
days_and_unit = user_input.split(":")
print(days_and_unit)
days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
print(days_and_unit_dictionary)
print(type(days_and_unit_dictionary))

validate_and_execute()


def  all_datatypes():
    message = "Enter some value"
    days = 20
    price = 9.99
    valid_number = True
    exit_input = False
    list_of_days = [20, 30, 20, 100]
    list_of_months = ["Jan", "Feb", "Mar"]
    Set_of_num = {10, 20, 30, 40}
    days_and_unit = {"days": 20, "unit": "hours"}

    print(message)
    print(type(message))
    print(days)
    print(type(days))
    print(price)
    print(type(price))
    print(valid_number)
    print(type(valid_number))
    print(exit_input)
    print(type(exit_input))
    print(list_of_days)
    print(type(list_of_days))
    print(list_of_months)
    print(type(list_of_months))
    print(Set_of_num)
    print(type(Set_of_num))
    print(days_and_unit)
    print(type(days_and_unit))


all_datatypes()


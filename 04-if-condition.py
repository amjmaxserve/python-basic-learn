calcuation_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):

    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days >= 0:
        return f"{num_of_days} days are {num_of_days * calcuation_units} {name_of_unit}"
    else:
        return "Negative number of days is not possible"

user_input = input("hey user, Enter a number of days you want to convert :\n")

user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)

print(calculated_value) 



print(type(30.11))
print(type(30))
print(type(4 + 5j))
print(type("hello"))

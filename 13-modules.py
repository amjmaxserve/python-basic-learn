# Modules is just a .py files that contains functions where we can use in another python files. 

from helper import user_input_message, validate_and_execute

"""
also we can call modules in different formats


1) from helper import *   ===> importing all files from the helper modules
2) import helper as h     ===> importing helper modules as h
    now functions will be calling like 

    h.user_input_message
    h.validate_and_execute

"""

user_input = ""
user_input = input(user_input_message)
days_and_unit = user_input.split(":")
print(days_and_unit)
days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
print(days_and_unit_dictionary)
print(type(days_and_unit_dictionary))

validate_and_execute(days_and_unit_dictionary)


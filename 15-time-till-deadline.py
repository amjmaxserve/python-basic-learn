import datetime 

user_input = input("Enter your goal with a deadline separated by colon \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

# calculate how many days from now till deadline 
time_till = deadline_date - today_date

print(f"Dear user!, time remining for your goal: {goal} is {time_till.days} days")

hours_till = int(time_till.total_seconds() /60 /60)
print(f"Dear user!, time remining for your goal: {goal}, is {hours_till} Hours")


"""

Built in Vs Third-party

python comes only with a set of built in modules

many more modules out there, which are not part of the python installation

examples: pandas, numpy, pytorch, plotly, tensorflow, keras etc.

you need to install these third-party packages

built in modules and packages are most common ones

depending on what application you write add specific ones. 


Web application: Django

you can find the packages inside the site pypi.org



"""
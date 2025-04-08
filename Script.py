calculate_hours = 24
unit3 = "hours"


def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculate_hours} {unit3}'
    

my_var = days_to_units(25)
print(my_var)


user_input = input("Mention days and i will convert to hours\n")
user_input_no = int(user_input)

final_value = days_to_units(user_input_no)
print(final_value)

# John Smith -> dairyfarm
# john.smith@dairyfarm.com.au

# Get first name from user
first_name = input("Enter your first name: ")

# Get last name from user
last_name = input("Enter your last name: ")

# Get the company's name from user
company_name = input("Enter your company's name: ")

# create the email according to the format and save it into a variable
predicted_email = f'{first_name}.{last_name}@{company_name}.com.au'.lower().replace(" ", "")

# display the email
print(predicted_email)

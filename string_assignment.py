'''
Question 1:

Task 1: Code Correction
You are provided with a scripot that is supposed to format customer names by ensuring the first letter is
uppercase and the rest are lowercase, regardless of how the data was entered.
However, the script contains errors. Correct the script so that it functions as intended.
'''
print()

def format_customer_name(name):
    # Check if the input is a valid string
    if not isinstance(name, str):
        return "Invalid input. Please provide a string."

    # Convert the first letter to uppercase and the rest to lowercase
    formatted_name = name.lower().capitalize()
    return formatted_name

# while loop to run program and break if no more names need entered
while True:
    customer_name = input("Enter customer name: ")
    formatted_name = format_customer_name(customer_name)
    print("Formatted name:", formatted_name)

    continue_program = input("Would you like to enter another name? y or n? ").lower()
    if continue_program != 'y':
        break

# There was no code for me to correct, so instead I just wrote my own script for this and commented some of my thoughts/steps I took while figuring out the problem.
    
'''
Task 2

Write a function that checks a list of email addresses for a SaaS application's user accounts. 
The function should verify that each email contains an "@" symbol and a "." after it, indicating a valid email format. 
If an email doesn't meet this criterion, print it out for further review.
'''
print()

def check_email_format(email_list):
    for email in email_list:
        if "@" not in email or "." not in email[email.index("@"):]:
            print("Invalid email format:", email)

emails = [
    "user1@example.com",
    "user2@example",
    "user3@.com",
    "user4",
    "user5@example.com",
    "user6@test.co.uk",
    "user7@invalidformat",
    "user8@test.org"
]

print(f"Emails = \n{emails}\n")
print("Checking email formats...")
check_email_format(emails)

'''
Task 3:

Create a script that generates a username for each new user. 
The username should be a combination of the first three letters of their first name and the first three letters of their last name. 
If the name is shorter than three letters, use the full name.
Ensure all usernames are in lowercase.
'''
print()

def generate_username(first_name, last_name):
    first_part = first_name[:3].lower()
    last_part = last_name[:3].lower()

    if len(first_name) < 3:
        first_part = first_name.lower()
    if len(last_name) < 3:
        last_part = last_name.lower()

    username = first_part + last_part
    return username

while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    username = generate_username(first_name, last_name)
    print("Your username is:", username)

    continue_program = input("Would you like to generate another username? y or n: ")
    if continue_program != 'y':
        break
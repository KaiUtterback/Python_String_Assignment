# Question 1

'''
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

# Question 2
    
'''
Task 1: Keyword Highlighter
Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
Print out each review with the keywords in uppercase so they stand out.
'''
print()

def highlight_keywords(review):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    words = review.split()
    highlighted_words = []

    for word in words:
        if word.lower() in keywords:
            highlighted_words.append(word.upper())
        else:
            highlighted_words.append(word)

    highlighted_review = ' '.join(highlighted_words)
    return highlighted_review

reviews = [
    "The product is good, but the service is poor.",
    "Excellent product quality!",
    "Bad experience with this product.",
    "Average performance, nothing special."
]

print("Highlighted Reviews:")
for review in reviews:
    highlighted_review = highlight_keywords(review)
    print("- ", highlighted_review)

'''
Task 2: 
Develop a function that tallies the number of positive and negative words in each review. 
Use a predefined list of positive and negative words to check against. 
The function should return the count of positive and negative words for each review.
'''
print()

def tally_sentiment(review, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    words = review.split()

    for word in words:
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1

    return positive_count, negative_count

positive_words = ["good", "excellent", "great", "awesome", "superb"]
negative_words = ["bad", "poor", "terrible", "awful", "horrible"]

reviews = [
    "The product is good, but the service is poor.",
    "Excellent product quality!",
    "Bad experience with this product.",
    "Average performance, nothing special."
]

print(reviews)
print()
print("Sentiment Tally:")
for index, review in enumerate(reviews):
    positive_count, negative_count = tally_sentiment(review, positive_words, negative_words)
    print(f"Review {index + 1}: Positive words: {positive_count}, Negative words: {negative_count}")

'''
Task 3: Review Summary
Implement a script that takes the first 50 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.
'''
print()

def create_review_summary(review):
    if len(review) <= 50:
        return review
    else:
        last_space_index = review[:50].rfind(' ')
        if last_space_index == -1:
            summary = review[:50] + "..."
        else:
            summary = review[:last_space_index] + "..."
        return summary

reviews = [
    "The product is good, but the service is poor. Overall, not satisfied with the experience.",
    "Excellent product quality, fast delivery, and great customer service!",
    "Bad experience with this product. It arrived damaged and the customer support was unhelpful.",
    "Average performance, nothing special. Expected better quality for the price."
]

print("Review Summaries:")
for index, review in enumerate(reviews):
    summary = create_review_summary(review)
    print(f"Review {index + 1}: {summary}")

'''
Q3

The aim of this assignment is to format and extract information from raw log files generated by a SaaS application to improve readability and analysis.

Task 1: Timestamp Extraction
Write a script that extracts the timestamp from each log entry. 
Assume that the timestamp is always at the beginning of each line and is enclosed in square brackets (e.g., "[2023-03-15 10:00:00]").

Task 2: Error Identification
Create a function that scans through the log file and identifies any error messages. 
Assume that all error messages start with the word "ERROR:". 
The function should print out each error message with its corresponding timestamp.

Task 3: Log Summary
Develop a script that creates a summary of the log file, including the total number of entries, the number of error messages, 
and the number of unique timestamps in the file.
'''
print()

import re

def extract_timestamps(log_data):
    timestamps = re.findall(r'\[(.*?)\]', log_data)
    return timestamps

def identify_errors(log_data):
    error_messages = re.findall(r'\[(.*?)\]\s+ERROR:(.*?)\n', log_data)
    return error_messages

def log_summary(log_data):
    total_entries = log_data.count('\n')
    error_count = len(re.findall(r'\bERROR\b', log_data))
    unique_timestamps = len(set(re.findall(r'\[(.*?)\]', log_data)))
    return total_entries, error_count, unique_timestamps

simulated_log_data = """
[2023-03-15 10:00:00] INFO: Application started
[2023-03-15 10:05:00] ERROR: Unable to connect to database
[2023-03-15 10:10:00] ERROR: Invalid input received
[2023-03-15 10:15:00] INFO: Request processed successfully
[2023-03-15 10:20:00] INFO: Application started
[2023-03-15 10:25:00] ERROR: Database connection lost
[2023-03-15 10:30:00] ERROR: Permission denied
[2023-03-15 10:35:00] WARNING: Disk space running low
"""
print("Log Data: ")
print(simulated_log_data)

# Task 1: Extract timestamps
timestamps = extract_timestamps(simulated_log_data)
print("Timestamps extracted:", timestamps)

# Task 2: Identify errors
error_messages = identify_errors(simulated_log_data)
print("\nError messages identified:")
for timestamp, error_message in error_messages:
    print(f"Timestamp: {timestamp}, Error: {error_message}")

# Task 3: Log Summary
total_entries, error_count, unique_timestamps = log_summary(simulated_log_data)
print("\nLog Summary:")
print(f"Total Entries: {total_entries}")
print(f"Error Count: {error_count}")
print(f"Unique Timestamps: {unique_timestamps}")

'''
Q4

Objective:
The aim of this assignment is to validate and correct a SaaS application's configuration files to ensure they adhere to the required format.

Task 1: Property Format Checker
You are given a configuration file where each line contains a property and its value separated by an "=" sign. 
Write a script that checks each line to ensure it follows this format. 
If a line does not contain an "=" sign or has more than one, print an error message with the line number.

Task 2: Whitespace Remover
Modify the script from Task 1 to remove any leading or trailing whitespace from the property names and values.

Task 3: Duplicate Property Finder
Extend the script to check for duplicate property names. 
If a duplicate is found, print out the property name and the line numbers where the duplicates are located.
'''
print()

def property_format_checker(config):
    errors = []
    lines = config.split('\n')
    for i, line in enumerate(lines, start=1):
        if '=' not in line or line.count('=') > 1:
            errors.append(f"Error in line {i}: {line}")
    return errors

def whitespace_remover(config):
    cleaned_config = ""
    lines = config.split('\n')
    for line in lines:
        if '=' in line and line.count('=') == 1:
            prop, value = line.split('=')
            prop = prop.strip()
            value = value.strip()
            cleaned_config += f"{prop}={value}\n"
        else:
            cleaned_config += line + '\n'
    return cleaned_config.strip()

def duplicate_property_finder(config):
    properties = {}
    errors = []
    lines = config.split('\n')
    for i, line in enumerate(lines, start=1):
        if '=' in line and line.count('=') == 1:
            prop, _ = line.split('=')
            prop = prop.strip()
            if prop in properties:
                errors.append(f"Duplicate property '{prop}' found in lines {properties[prop]} and {i}")
            else:
                properties[prop] = i
    return errors


simulated_config = """
user=admin
password = 12345
port= 8080
host=localhost
user = guest
port=9090
"""

# Task 1: Property Format Checker
print("Property Format Checker")
errors_task1 = property_format_checker(simulated_config)
if errors_task1:
    for error in errors_task1:
        print(error)
else:
    print("All lines follow the correct format.")

# Task 2: Whitespace Remover
print("\nWhitespace Remover")
cleaned_config = whitespace_remover(simulated_config)
print("Cleaned Configuration Data:")
print(cleaned_config)

# Task 3: Duplicate Property Finder
print("\nDuplicate Property Finder")
errors_task3 = duplicate_property_finder(simulated_config)
if errors_task3:
    for error in errors_task3:
        print(error)
else:
    print("No duplicate properties found.")

'''
Q5 User Input Data Processor

Objective:
The aim of this assignment is to process and format user input data for a SaaS application's registration form.

Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. 
If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. 
The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. 
If the password does not meet these criteria, print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format. 
onvert the entire email address to lowercase and replace any spaces with a period.
'''

print()

simulated_firstname = "John"
simulated_lastname = "Doe"
simulated_password = "P@ssw0rd"
simulated_email = "john.doe@example.com"

print("Simulated User Input Data:")
print("First Name:", simulated_firstname)
print("Last Name:", simulated_lastname)
print("Password:", simulated_password)
print("Email:", simulated_email)
print()

def input_length_validator(firstname, lastname):
    if len(firstname) < 2 or len(lastname) < 2:
        print("Error: First name and last name must be at least 2 characters long.")

def password_complexity_checker(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Error: Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one digit.")
    else:
        print("Password meets complexity requirements.")

def email_formatter(email):
    formatted_email = email.lower().replace(' ', '.')
    return formatted_email

# Task 1: Input Length Validator
print("Task 1: Input Length Validator")
input_length_validator(simulated_firstname, simulated_lastname)

# Task 2: Password Complexity Checker
print("\nTask 2: Password Complexity Checker")
password_complexity_checker(simulated_password)

# Task 3: Email Formatter
print("\nTask 3: Email Formatter")
formatted_email = email_formatter(simulated_email)
print("Formatted Email:", formatted_email)

'''
Q6 Text-Based Report Generator

Objective:
The aim of this assignment is to generate a formatted text-based report from raw data for a SaaS application's internal use.

Task 1: Header Formatter
Write a script that formats the headers of the report. 
Each header should be centered, in uppercase, and underlined with "=" characters.

Task 2: Data Alignment
Format the raw data so that each column is aligned. 
Assume the data is separated by commas and should be displayed in a table format with each value left-aligned in its column.

Task 3: Report Summary
At the end of the report, add a summary section that counts the number of data entries and calculates the average value of a numeric column.
'''
print()

def header_formatter(header):
    formatted_header = header.upper().center(50, "=")
    return formatted_header

def data_alignment(raw_data):
    formatted_data = ""
    rows = raw_data.split('\n')
    max_lengths = [max(len(value) for value in row.split(',')) for row in rows if row]  
    for row in rows:
        if row:
            values = row.split(',')
            formatted_row = ' | '.join(value.ljust(length) for value, length in zip(values, max_lengths))
            formatted_data += formatted_row + '\n'
    return formatted_data

def report_summary(raw_data):
    num_entries = raw_data.count('\n') - 1  
    numeric_values = [float(value) for row in raw_data.split('\n')[1:] for value in row.split(',')[1:] if value.isdigit()]
    average_numeric = sum(numeric_values) / len(numeric_values) if numeric_values else 0
    summary = f"Number of Entries: {num_entries}\nAverage Value: {average_numeric:.2f}"
    return summary


simulated_raw_data = """
ID, Name, Age, Score
1, John, 25, 85
2, Alice, 30, 90
3, Bob, 28, 88
4, Lisa, 22, 95
"""

print("Simulated Raw Data:")
print(simulated_raw_data)

# Task 1: Header Formatter
print("\nTask 1: Header Formatter")
formatted_header = header_formatter("ID, Name, Age, Score")
print(formatted_header)

# Task 2: Data Alignment
print("\nTask 2: Data Alignment")
formatted_data = data_alignment(simulated_raw_data)
print(formatted_data)

# Task 3: Report Summary
print("\nTask 3: Report Summary")
summary = report_summary(simulated_raw_data)
print(summary)

'''
Q7 
Interactive Help Desk Bot

Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). 
If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. 
Print out the category of the issue for the support team.

Task 3: Auto-Response Generator
For general help inquiries, create a script that generates an auto-response providing links to the FAQ section, support contact information, and a link to submit a ticket.
'''
print()
print('=' * 60)
print("Interactive Help Desk Bot")
print('=' * 60)

def command_parser(user_input):
    commands = ["help", "issue", "contact_support"]
    for command in commands:
        if command in user_input:
            return command
    return None

def issue_categorizer(user_input):
    categories = {
        "login": ["login", "authentication"],
        "performance": ["slow", "lag", "performance"],
        "error": ["error", "bug", "crash"]
    }
    for category, keywords in categories.items():
        if any(keyword in user_input for keyword in keywords):
            return category
    return None

def auto_response_generator():
    response = """
    For general help, please visit our FAQ section: [FAQ link]
    To contact support, please email us at support@example.com or submit a ticket here: [Ticket link]
    """
    return response

simulated_user_input = "I'm experiencing a performance issue with the application"
print("simulated user input:")
print(simulated_user_input)
print('=' * 60)


# Task 1: Command Parser
print("Command Parser")
command = command_parser(simulated_user_input)
if command:
    print(f"Command '{command}' identified.")
else:
    print("No command identified.")

# Task 2: Issue Categorizer
print("\nIssue Categorizer")
if "issue" in simulated_user_input:
    category = issue_categorizer(simulated_user_input)
    if category:
        print(f"Issue category: {category}")
    else:
        print("No specific issue category identified.")

# Task 3: Auto-Response Generator
print("\nAuto-Response Generator")
response = auto_response_generator()
print(response)
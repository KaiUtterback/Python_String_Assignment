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

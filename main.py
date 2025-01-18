def welcome():
    print("Hello! Thank you for using CEOBOT: BECOME A CEO LIKE ME!")
    userInfo()

def userInfo():
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f"Thank you, {name}! This information will help me guide you to BECOME A CEO LIKE ME!")

def menu():
    print("1. Ask a question")
    print("2. Update Info")
    print("3. Customer Support")
    print("4. Exit chat")
    query = int(input("How would you like to proceed? [Enter a number]"))
    return query

def askChatbot(query):
    if query == 1:
        conversation = input("Ask me something..")
        print(f"You asked: {conversation}")
    elif query == 2:
        userInfo()
    elif query == 3:
        print("Please email us at ceochatbot@code2college.org")
    elif query == 4:
        print("Thank you for using CEOBOT: BECOME A CEO LIKE ME!")
    else:
        print("Invalid option. Please enter a number between 1 and 4.")

welcome()
while True:
    query = menu()
    if query == 4:
        print("Thank you for using CEOBOT: BECOME A CEO LIKE ME!")
        break
    askChatbot(query)
# Rule-Based AI Chatbot using Functions

# Function to clean user input
def sanitize(text):
    return text.strip().lower()


# Function to generate chatbot response
def get_response(user):

    # Greetings
    if user == "hi" or user == "hello":
        return "Hello! Welcome to the AI Chatbot."

    elif user == "good morning":
        return "Good Morning!"

    elif user == "good night":
        return "Good Night!"

    # Basic conversation
    elif user == "how are you":
        return "I am fine. Thank you!"

    elif user == "what is your name":
        return "I am a Rule-Based AI Chatbot."

    elif user == "who created you":
        return "I was created using Python."

    elif user == "thank you":
        return "You are welcome!"

    # AI related questions
    elif user == "what is ai":
        return "AI means Artificial Intelligence."

    elif user == "what is python":
        return "Python is a popular programming language."

    elif user == "what can you do":
        return "I can answer simple predefined questions."

    # Help command
    elif user == "help":
        return """
You can try these commands:
- hello
- how are you
- what is ai
- what is python
- what is your name
- who created you
- bye
"""

    # Exit condition
    elif user == "bye":
        return "Goodbye! Have a nice day."

    # Default response
    else:
        return "Sorry, I don't understand."


# Main chatbot program
print("===================================")
print("      AI CHATBOT STARTED")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")


# Continuous loop
while True:

    # Taking user input
    user_input = input("You: ")

    # Cleaning input
    clean_input = sanitize(user_input)

    # Getting chatbot response
    response = get_response(clean_input)

    # Printing chatbot response
    print("Bot:", response)

    # Exit condition
    if clean_input == "bye":
        break


print("\nChatbot Ended Successfully!")
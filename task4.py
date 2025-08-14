# Basic Chatbot - CodeAlpha Internship Task 4

def chatbot_response(user_input):
    """Returns a response based on the user's input."""
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    
        
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print(" Basic Chatbot - Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Bot: {response}")
        if user_input.lower() in ["bye", "goodbye"]:
            break

if __name__ == "__main__":
    run_chatbot()


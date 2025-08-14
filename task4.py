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
    elif user_input in ["i like you", "I like you"]:
        return "me too also"
    elif user_input in ["do you love me", "Do you love me", "Do You Love me"]:
        return "Sure ! I Love You"
    elif user_input in ["What is Your Favorite Colour", "what is your favorite colour"]:
        return "Pink , Whats your"
    elif user_input in ["suggest some movie regarding my interest like tech"]:
        return "Interaseller , Coding With Dady , Genius , Genius2, "
    elif user_input in ["i am also fine", "I am also fine"]:
        return "Okay"
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print("🤖 Basic Chatbot - Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Bot: {response}")
        if user_input.lower() in ["bye", "goodbye"]:
            break

if __name__ == "__main__":
    run_chatbot()

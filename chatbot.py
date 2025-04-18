# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How can I assist you?"
    elif "your name" in user_input:
        return "I'm ChatBot! Your virtual assistant."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that. Can you try again?"

def main():
    print("🤖 Welcome to the ChatBot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            print("Bot:", chatbot_response(user_input))
            break

        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()

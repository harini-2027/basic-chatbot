#defining the chatbot function
def chatbot():
    print("Hello! How can i help you today?")
    print("Type 'help' to see available commands")
#continuously take user input until the user chooses to exit
    while True:
        user_input = input("You:").lower()
#respond to basic greetings and common questions
        if user_input == "hello" or user_input == "hi":
            print("Hello! nice to meet you.")
        elif user_input == "how are you":
            print("i'm fine, thankyou!")
        elif user_input == "what is your name":
            print("my name is bot")
        elif user_input == "good morning":
            print("good morning! have a great day")
        elif user_input == "good evening":
            print("good evening! how was your day?")
        elif user_input == "thankyou" or user_input == "thanks":
            print("Your very welcome!")
#displaying all the commands supported by the chatbot
        elif user_input == "help":
            print("available commands:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- good morning")
            print("- good evening")
            print("- thankyou")
            print("- bye")
#end the chatbot when the user enters bye
        elif user_input == "bye":
            print("Goodbye! have a nice day")
            break
#handles inputs that are not supported by the chatbot
        else:
            print("Sorry, I don't understand that")
#calling the chatbot function
chatbot()


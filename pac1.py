import datetime

print("=" * 50)
print("        WELCOME TO AI CHATBOT")
print("=" * 50)

print("\nType 'exit' to close the chatbot.\n")

while True:

    user = input("You : ")
    user = user.lower()

    if user == "hello" or user == "hi":
        print("Bot : Hello! Welcome.")

    elif user == "how are you":
        print("Bot : I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot : My name is AI ChatBot.")

    elif user == "who created you":
        print("Bot : I was created using Python.")

    elif user == "what is ai":
        print("Bot : Artificial Intelligence enables computers to think and make decisions.")

    elif user == "python":
        print("Bot : Python is a popular programming language for AI.")

    elif user == "date":
        today = datetime.date.today()
        print("Bot :", today)

    elif user == "time":
        now = datetime.datetime.now()
        print("Bot :", now.strftime("%H:%M:%S"))

    elif user == "thank you":
        print("Bot : You're welcome!")

    elif user == "bye":
        print("Bot : Goodbye! Have a Nice Day.")
        break

    elif user == "exit":
        print("Bot : Chat Closed Successfully.")
        break

    else:
        print("Bot : Sorry! I don't understand your question.")
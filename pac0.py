spam_words = [
    "lottery",
    "winner",
    "prize",
    "free",
    "offer",
    "money",
    "click",
    "claim"
]

email = input("Enter your email message:\n")

email = email.lower()

spam = False

for word in spam_words:
    if word in email:
        spam = True
        break

if spam:
    print("\nResult: Spam Mail")
else:
    print("\nResult: Not Spam Mail")
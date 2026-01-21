import re

email = input("What's your email? ").strip()


if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(edu|co.uk|com|dk|de|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")




 
def main():
    names = ["Mario", "Luigi", "Yoshi", "Toad"]

    for name in names:
        print(write_letter(name, "Princess Peach"))




def write_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~+
    Dear {reciever},

    You are cordinally invited to a ball at 
    Peach's Castle this evening, 7:00 PM

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~+
    """


main()
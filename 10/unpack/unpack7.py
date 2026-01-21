def total(galleons=0, sickles=0, knuts=0):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50}

print(total(**coins), "Knuts")



# Ved at default værdier, behøver vi ikke give 3 argumenter, men kan nøjes med 2






results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Toad")
results.append("Yoshi")
results.append("Bowser")

results.append(["Donkey Kong", "Koopa Troopa"]) # Tilføjer ekstra list inde i listen
results.remove(["Donkey Kong", "Koopa Troopa"])
results.extend(["Donkey Kong", "Koopa Troopa"])

print(results)
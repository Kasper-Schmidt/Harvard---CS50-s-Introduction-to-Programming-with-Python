for i in [0, 1, 2]:
    print("Meow")

print("---------------")

for y in range(3): # Da jeg aldrig bruger y, er det bedre bare at skrive _, som i næste.
    print("Vuff")

print("---------------")

for _ in range(3): 
    print("Vuff")


print("---------------")

print("Meow" * 3)

print("---------------")

print("Meow\n" * 3)

print("---------------")

print("Meow\n" * 3, end="")




while True:
    n = int(input("What's n? "))
    if n > 0:
        break

    for _ in range(n):
        print("Meow")

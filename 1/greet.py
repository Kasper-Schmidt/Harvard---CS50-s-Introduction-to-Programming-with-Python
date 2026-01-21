def greet(input):
    if "hello" in input:
        return ("Hello there")
    else:
        return ("I'm not sure what you mean")

print("------------------")

greeting = greet("hello computer")
print(greeting)
print("Hm, " + greeting)

print("------------------")

greeting = greet("How's the weather up there?")
print(greeting)
print("Hm, " + greeting)

print("------------------")



greeting = greet("hello, computer?")
print(greeting)
print(greeting + " James")

print("------------------")
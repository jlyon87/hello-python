message = "a"  # local


def greet():
    # global message # evil!
    message = "b"
    print(message)


greet()

print(message)

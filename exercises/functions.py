def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))  # keyword arguments for readability
print(type(increment(2, 3)))  # => tuple, like read only list

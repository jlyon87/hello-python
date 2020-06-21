def fizz_buzz(input: int):
    message: str = ""
    if input % 3 == 0:
        message = "fizz"

    if input % 5 == 0:
        message += "buzz"

    return message if message.strip() else input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
# n / 3 = fizz
# n / 5 = buzz
# n / both = fizzbuzz

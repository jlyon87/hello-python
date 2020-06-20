names = ["James", "Mary"]
for name in names:
    if name.startswith("D"):
        print("Found")
        found = True
        break

else:  # If we don't hit the break, it runs the else.
    print("Not found")

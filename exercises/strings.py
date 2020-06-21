course = "Python Programming"
print(len(course))

print(course[0])  # positive index references index from the left

print(course[-2])  # negative index references index from the right

print(course[0:3])  # Slice 3 characters from index 0

print(course[:3])  # same as above

print(course[0:])  # whole string

print(course[:])  # whole string

print(id(course))
print(id(course[0]))

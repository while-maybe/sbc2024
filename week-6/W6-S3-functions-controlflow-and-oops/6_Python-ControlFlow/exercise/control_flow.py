def first_three(l):
    l = iter(l)
    for _ in range(3):
        try:
            yield next(l)
        except StopIteration:
            return "No more elements"
    return next(l)

# stuff = first_three([1, 2, 3, 4])


squares = [x ** 2 for x in range(1, 11)]
print(squares)

uniques = {y for y in "This is one string with many characters"}
print(uniques)

squares_dict = {x: x ** 2 for x in range(1, 11)}
print(squares_dict)


for x in squares:
    print(x, end=" ")
print()


i, sum = 0, 0
while i <= 1000:
    sum += i
    if not (i % 2):
        print(i, end=" ")
    if sum > 500:
        break
    i += 1


print(first_three([1, 2, 3, 4]), squares, uniques, squares_dict)
print(f"Result of while loop is {sum}")

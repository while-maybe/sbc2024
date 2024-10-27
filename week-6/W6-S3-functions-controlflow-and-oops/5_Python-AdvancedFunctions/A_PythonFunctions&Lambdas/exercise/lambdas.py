square = lambda x: x ** 2

squares = list(map(square, [1, 2, 3, 4]))
print(squares)

# if a number is a multiple of 3, remainder of division by 3 is 0 which Python resolves to False. The not operator reverses this to True
multiples = list(filter(lambda y: not (y % 3), [1, 2, 3, 4, 5, 6]))
print(multiples)

sorted_list = sorted([('table1', 10), ('table2', 8), ('table3', 4)], key=lambda x: x[1])
print(sorted_list)

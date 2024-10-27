def get_multiples(max):
    count = 1
    while count <= max:
        if not (count % 33):
            yield count
        count += 1

# for number in count_up_to(5):
for number in get_multiples(1_000_000):
    print(number, end=" ")
print()

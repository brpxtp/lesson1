numbers = []
new_numbers = []
all_sum = 0

for i in range(1001):
    numbers.append(i)
    for i in numbers:
        if i % 2 == 0:
            numbers.pop()

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 3
print(numbers)

for ind, val in enumerate(numbers):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += numbers[ind]
print(all_sum)

for j in numbers:
    new_numbers.append(j + 17)
all_sum = 0
for ind, val in enumerate(new_numbers):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += new_numbers[ind]
print(all_sum)



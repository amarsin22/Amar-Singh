numbers = [1,2,8,9,12,46,76,82,15,20,30]
output = {}

for n in range(1, 10):
    count = 0
    for x in numbers:
        if x % n == 0:
            count += 1
    output[n] = count

print(output)


count = 0
prev = int(input())
number = int(input())
while number != 0:
    if number > prev:
        count += 1
    prev = number
    number = int(input())
print(count)
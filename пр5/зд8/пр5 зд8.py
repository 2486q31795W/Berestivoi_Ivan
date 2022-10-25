prev = count = 0 
max = 1
number = int(input())
while number != 0:
    if number == prev:
        count += 1
        if count > max:
            max = count
    else:
        count = 1
    number, prev = int(input())
print(max)
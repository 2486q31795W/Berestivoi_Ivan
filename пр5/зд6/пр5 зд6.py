number = int(input())
count, sum = 0, 0
while number != 0: 
    count += 1
    sum += number 
    number = int(input())
    print(sum/count)
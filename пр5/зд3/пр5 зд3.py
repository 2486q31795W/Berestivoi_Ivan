n = int(input())
two_in_power = 1
count = 0
while two_in_power <= n:
    two_in_power *= 2
    count += 1
    print (count - 1, two_in_power // 2)
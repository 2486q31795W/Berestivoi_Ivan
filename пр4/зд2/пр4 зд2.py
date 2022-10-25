def count(a, b):
    if a<b:
        count(a,b-1)
        print (b)
    elif(a>b):
        count(a-1,b)
a = input()
b = input()
count (a,b)
a = input("введите текст:")
b = a
p = 0
for i in range(len(a)):
    if a[i] == "а":
        b += "о"
        p += 1
    else:
        b +=a[i]    
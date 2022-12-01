def task(a, b, r, c):
    return len(list(filter(lambda z : (z[0]-a)**2+(z[1]-b)**2)<r**2, c))

print(task(1, 1, 2, [[0,0],[1,1],[1,2][2,1],[3,3]]))    
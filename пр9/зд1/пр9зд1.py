import random
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print('Исходная матри:' ,matrix)
s=[]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print("Строка с наибольшей суммой:" ,matrix[s.index(max(s))], "Сумма элементов:" ,max(s), "Строка с наименьшей суммой:" ,matrix[s.index(min(s))]),"Сумма элементов:",min(s)    
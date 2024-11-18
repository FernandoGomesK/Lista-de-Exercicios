matrix = [[1, 2, 3], 
          [1, 2, 3],
          [1, 2, 3]
         ]

def diagonal1(x):
    total = 0
    for i in range(len(x)):  
        total += x[i][i]
    return total

def diagonal2(x):
    total = 0
    row = len(x)
    for i in range(row):
        total +=x[i][row - i - 1]
    return total

result = diagonal1(matrix)
result2 = diagonal2(matrix)
print(result)
print(result2)
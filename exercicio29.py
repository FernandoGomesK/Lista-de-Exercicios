nest_list= [[1, 2, 2, 3],[4, 4, 5, 6]]

def untangle(x):
   x2 = [list(set(y)) for y in x]
   return x2

x2 = untangle(nest_list)
print(x2)
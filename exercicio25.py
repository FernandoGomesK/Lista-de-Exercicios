list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [20, 30, 40, 60, 80]
def even_finder(x):
    for y in x:
        if y % 2 == 0:
            print(y)
            
even_finder(list1)
even_finder(list2)
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.my_list=["123","1234","45ifd","ff45i","897as","123"]
def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input(
    "Введите число :\n"))
lst = [findFib(index) for index in range(1, n+2)]
#print(lst)
lst = lst[::-1] + lst[1:]
print(lst, '\n')
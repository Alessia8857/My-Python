#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]


def multi_par(my_list):
    
    new_list = []
    if len(my_list)%2 !=0:
       l = len(my_list)//2  + 1
    else :
       l = len(my_list)//2
    for i in range(l): 
            new_list = my_list[i]*my_list[len(my_list)-i-1]
            print( new_list, end=' ' )

my_list  = [2,3,4,5,6]        
multi_par(my_list)  
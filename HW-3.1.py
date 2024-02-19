
def sum(my_list):
    s = 0
    for i in range(len(my_list)):
        if i%2 == 1:
            s += my_list[i]
    print(f" сумма равна {s}")

my_list  = [2,1,5,8,3]        
sum(my_list)  
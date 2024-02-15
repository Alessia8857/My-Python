my_list=["123","1234","45ifd","ff45i","897as","123"]
print(my_list)

flag=-1
index=0

search=input('Введите число:')
for iten in range(len(my_list)):
    if search in my_list[iten]:
        flag+=1
        if flag==1:
            index=iten+1
            break
if flag==1:
    print({index})
else: 
    print(-1)  

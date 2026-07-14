list = [] 
size = int(input("Enter No. of elements you want to enter: "))

for i in range(size):
    element = int(input(f"Enter list[{i}]: "))
    
    list.append(element)
    
for i in range(size):
    
    smallest = i
    
    for j in range(i+1, size):

        if list[smallest] > list[j]:
            smallest = j
            
    temp = list[i]
    list[i] = list[smallest]
    list[smallest] = temp
            
print(list)
        

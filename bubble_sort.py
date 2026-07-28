import time

list = [] 
size = int(input("Enter No. of elements you want to enter: "))

for i in range(size):
    element = int(input(f"Enter list[{i}]: "))
    
    list.append(element)
    
start_time = time.perf_counter()
    
for i in range(size):
      
    for j in range(size-i-1):

        if list[j] > list[j+1]:
            
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
            
end_time = time.perf_counter()

print("Total time taken: ", end_time-start_time)
            
print(list)
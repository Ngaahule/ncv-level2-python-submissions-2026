
marks = [] 


mark = int(input("Enter mark (-1 to stop): "))
sum = 0
while mark != -1:
    marks.append(mark)
    #print(f"{i}. Mark: {marks[i]}")
    sum += mark
    
    mark = int(input("Enter mark (-1 to stop): "))

average = sum / len(marks)

for x in range(len(marks)):
    y= 1
    print(f"{x+1}. Mark: {marks[x]}")
    
    
print(f"Total   : {sum}")
print(f"Average : {average}")
    
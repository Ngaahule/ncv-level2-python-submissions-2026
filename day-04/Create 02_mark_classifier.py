
mark = input("Please enter a mark between 0 and 100 : ")

if mark =="":
    print("invalid entry")
else:
    mark = int(mark)
    if mark < 0 or mark > 100:
        print("enter a number between 0 and 100")
    else: 
        if mark >= 80 and mark <= 100:
            print("Outstanding")
        elif mark >= 70 and mark <= 79:
            print("Highly competent")
        elif mark >= 50 and mark <= 69:
            print("Competent")
        elif mark >= 40 and mark <= 49:
            print("Not yet competent")
        else:
            print("Not achieved")

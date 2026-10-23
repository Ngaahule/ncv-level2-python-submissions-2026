
tmark = 0
count = 0

mark = input("Please enter mark (s to stop): ")

while mark != "s":
    mark = int(mark)

    if mark < 0 or mark > 100:
        print("Number should be between 0 and 100")
    else:
        print("Mark:", mark)
        tmark += mark
        count += 1

    mark = input("Please enter mark (s to stop): ")

print("Total marks:", tmark)
print("Number of marks:", count)

if count > 0:
    average = tmark / count
    print("Average mark:", average)
else:
    print("No marks were entered.")

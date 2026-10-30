try:
    f = open("marks.txt", "r")
    
    data = {}
    total = 0
    count = 0

    for line in f:
        name, marks = line.split()
        marks = int(marks)
        
        data[name] = marks
        total += marks
        count += 1

    avg = total / count
    print("Average Marks:", avg)

    f.close()

except FileNotFoundError:
    print("FileNotFoundError")
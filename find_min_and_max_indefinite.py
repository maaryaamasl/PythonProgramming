largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float( num )
        if largest is None :
            largest = num
            smallest = num
        else:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num

    except:
        print( "Invalid input")


print("Maximum is", int(largest))
print("Minimum is", int(smallest))

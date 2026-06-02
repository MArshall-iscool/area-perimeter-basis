# Ask user for width and loop
# enter a number that is more than zero.

error = "Please enter a valid number\n"
while True:

    try:
        #ask the user for a number
        width = float(input("Width: "))

        # check that the numebr is more than zero
        if width > 0:
            break
        else:
            print(error)

       
    except ValueError:
        print(error)
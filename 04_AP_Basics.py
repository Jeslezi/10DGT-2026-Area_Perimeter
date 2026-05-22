#Ask user for width and loop until they
#enter a number that is more than zero

#Error statement
error = "Please enter a number that is more than zero\n"
while True:
    
    try:
        #Ask the user for the width
        width = float(input("Width: "))
        #Checks if the width is more than zero
        if width > 0:
            break
        else:
            #If it isn't print the error code
            print(error)
    except ValueError:
        print(error)

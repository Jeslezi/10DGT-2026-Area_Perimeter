def num_checker(question):
    
    #Error statement
    error = "Please enter a number that is more than zero\n"
    while True:
        
        try:
            #Ask the user for the width
            response = float(input(question))
            
            #Checks if the width is more than zero
            if response > 0:
                return response
            else:
                #If it isn't print the error code   
                print(error)
        except ValueError:
            print(error)

#Main routine 

keep_going = ""
while keep_going == "":
    
#Get width and height
    width = num_checker("Width: ")
    height = num_checker("height: ")
    
#Calculate area/perimeter
    area = width*height
    perimeter = 2 * (width + height)    

#display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

#Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area/perimeter calculator")
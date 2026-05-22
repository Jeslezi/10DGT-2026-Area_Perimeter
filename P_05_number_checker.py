#Ask user for width and loop until they
#enter a number that is more than zero
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

#Main Routine goes here
for item in range(0, 2):    
    width = num_checker("Width: ")
    print(width)

print()

for item in range(0, 2):    
    height = num_checker("height: ")
    print(height)
#Ask the user for the width and height
#(Assume they put in valid data)
width = float(input("Width: "))
height = float(input("Height: "))

#Calculate the area and perimeter
area = width*height
perimeter = 2 * (width + height)
#Output the area and perimeter
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")



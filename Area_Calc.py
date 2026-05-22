#Ask the user for the width and height
#(Assume they put in valid data)
width = float(input("Width: "))
height = float(input("Height: "))

#Calculate the area and perimeter
area = width*height
perimeter = 2 * (width + height)
#Output the area and perimeter
print(f"The area of {width} and {height} is {area}")
print(f"The perimeter of {width} and {height} is {perimeter}")
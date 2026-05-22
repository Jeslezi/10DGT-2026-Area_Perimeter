#ask the user for their name
username = input("What is your name? ") 

#ask the user for their favorite number
fav_num = int(input("What is you favorite number? "))

#Double, halve, and square their number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

#Greet user
print (f"\nHi {username}, your favorite number is {fav_num}")
#Output the results of doubling, halving and
#Squaring their favorite integer
print(f"\nThe result of doubling {fav_num} is {double}")
print(f"The result of halving {fav_num} is {halve}")
print(f"The result of squaring {fav_num} is {square}")
print("\nHave a nice day")

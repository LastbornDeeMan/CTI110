"""
CTI 110
P1HW1 - Variables
davisc
9/5/2023

Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them 

"""
# Part One: 
# variables. first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input, then convert it into int
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("Enter another integer")
second = int(input())
#print(" +  =", first + second)
print(first, "+", second, "=", first + second)
#print(" *  =", first * second)
print(first, "*", second, "=", first * second)



# PART TWO: MOVIES
# The variables
# string - movie name
# int- the year of the movie
# float - the gross (in million dollars)
# finally, print a quote from the movie
name = "Robocop"
year = 1987
gross = 53.42 #mil $

# Print out this information
# Then print out a movie quote

print("""

The movie Robocop was made in 1987, and it grossed 53.42 million $.

Dead or alive, you're coming with me!

""")


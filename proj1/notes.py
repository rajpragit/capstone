

# Create a variable savings
savings=100
# Print out savings
print(savings)
print(type(savings))
# Create a variable savings
savings = 100
growth_multiplier = 1.1
# Create a variable factor
factor = 1.1
# Calculate result
result = savings * factor ** 7
# Print out result
print(result)
# Create a variable desc
desc="compound interest"
# Create a variable profitable
profitable = True

#---------
# Several variables to experiment with
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and factor to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)


#------------------------------------
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)


#------------------------------------

#check these code
print("I can add integers, like " + str(5) + " to strings.")
print("I said " + ("Hey " * 2) + "Hey!")
#this will give error
print("The correct answer to this multiple choice exercise is answer number " + 2)  
print(True + False)



#-----------------------------------------------------------------------------------
#LISTS
#-----------------------------------------------------------------------------------

# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [ hall,kit,liv,bed,bath]

# Print areas
print(areas)

#Valid lists
a= [1, 3, 4, 2] 
b= [[1, 2, 3], [4, 5, 7]] 
c= [1 + 2, "a" * 5, 3]

#List Indexes are 0 based 
listname =  ["AA","BB","CC","DD","EE","FF","GG"]
#Indexes      0    1    2    3    4    5    6
#Indexes     -7   -6   -5   -4   -3   -2   -1
#Subset  listname[start index to include : end index which is not included]
subset=listname[2:5]
#subset will be ["CC", "DD", "EE"]
subset=listname[:5]  # from begining to index 4
subset=listname[5:]  # from index 5 till end including index 5

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[-4:]
print(downstairs)
print(upstairs)

#subsetting
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]  # selects ["g"]
x[2][:2]  # selects ["g","h"]
x[2][1:2] # selects ["h"]


#List Manipulations
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area
areas[-1]=10.50
# Change "living room" to "chill zone"
areas[4]="chill zone"
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

#Delete list elements
#Finally, you can also remove elements from your list. You can do this with the del statement:

x = ["a", "b", "c", "d"]
del(x[1])
#Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!


#Inner workings of lists

#The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first element in the areas_copy list is changed and the areas list is printed out. If you hit Run Code you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.
#If you want to prevent changes in areas_copy from also taking effect in areas, you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = areas
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)


#-----------------------------------------------------------------------------------
#FUNCTIONS
#-----------------------------------------------------------------------------------
# to make a copy of list use any of the following two lines
areas_copy =list(areas) 
areas_copy = areas[:]
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first+second
# Sort full in descending order: full_sorted
print(full)
# Print out full_sorted
full_sorted =  sorted(full, reverse=True)
print(full_sorted)
#max and len functions
print(max(full_sorted))
print(len(full_sorted))


#-----------------------------------------------------------------------------------
#METHODS
#----------------------------------------------------------------------------------- 

# string to experiment with: room
room = "poolhouse"
# Use upper() on room: room_up
room_up = room.upper()
# Print out room and room_up
print(room)
print(room_up)
# Print out the number of o's in room
print(room.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(9.5))



# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)
# Print out areas

print(areas)
# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)



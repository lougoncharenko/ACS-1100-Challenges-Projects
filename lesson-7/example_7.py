#TODO: Using a for loop, print out each color from the list 
# called colors.
colors = ["red", "orange", "green", "blue", "purple"]


for color in colors:  
  print(color)

# For however many colors are in the list called colors
# exectute this for loop

for i in range(len(colors)):
  color = colors[i]
  print(color + " is awesome!") 


#TODO: Create a list of 4 names.
list_names = ['Louisa', 'Parul', 'Paloma', 'Kyle', "Marty"]
#TODO: Using a for loop, print out each name with " is 
# awesome!" added after each name.



for i in range(len(list_names)):
  print(f"{list_names[i]} is awesome!")




#TODO: create a list of five integers
#TODO: print the sum of the numbers in the list
integers = [56,3,23,16,78,3,4]

# for integer in integers:
#   print(integer)
total = 0
for i in range(len(integers)):
  total += integers[i]
print(total)


#TODO: After calulcating the sum, calculate the average.
# To calculate average, we take the sum divided by the 
# number of elements in the list called numbers


average = (total/7)
print(average)



# Redo these with range() 



# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!
print("Welcome to MadLibs!")
name = input("Enter a person's name: ") 
noun1 = input("Enter a noun: ")
feeling1 = input("Enter a feeling:") 
verb1 = input("Enter a verb:")
feeling2 = input("Enter a feeling:") 
animal1 = input ("Enter an animal:")
verb2 = input("Enter a verb:")
color1 = input("Enter a color:")
verb3 = input("Enter a verb ending in 'ing' :")
adverb = input ("Enter an adverb ending in ly: ")

color2 = input("Enter a color:")
animal2 = input ("Enter an animal:")


print(f"This weekend I am going camping with {name} \n I packed my lantern, sleeping bag, and {noun1}. \n I am so {feeling1} to {verb1} in a tent. \n I am {feeling2} we might see a {animal1}, \n they are kind of dangerous. We are going to hike, fish, and {verb2}. \n I have heard that the {color1} lake is great for {verb3}. \n Then we will {adverb} hike through the forest. \n If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!")
 





































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")
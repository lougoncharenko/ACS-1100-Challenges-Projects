'''
Use while loops to solve the problems below.
'''


# TODO - Exercise 1: Repeatedly print the value of the variable price,
# decreasing it by 0.7 each time, as long as it remains positive.

# price = 5
# while price > 0:
#     price -= 0.7
#     print(price)



# TODO - Exercise 2: Print ONLY even numbers from 0 to 20
# number = 0
# while number < 20:
#     number += 2
#     print(number)

number = 0
while(number < 20):
    if number % 2 == 0:
        print(number)
        number += 1
    else:
        continue

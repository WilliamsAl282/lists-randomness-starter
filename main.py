# 10/22/2024
# Alexander Williams
# Web and App Development




# Problems using randrange()
# 1. random color
import random
colors = ['red','blue','green','purple','orange']


num_items = len(colors)
print(f'The number of elements in ths list is {num_items}')

random_index = random.randrange(num_items)

print(f'The randomly selected index was: {random_index}')
print(f'The color at index {random_index} is: {colors[random_index]}')



# 2. Random Animal index
import random
animals = ['snake', 'zebra', 'bear','hawk','shark']

print(len(animals))

num_animals = len(animals)


random_animal_index = random.randrange(num_animals)


print(f'The animal at index number {random_animal_index} is {animals[random_animal_index]}')
random_animal_index = random.randrange(num_animals)
print(f'The animal at index number {random_animal_index} is {animals[random_animal_index]}')
random_animal_index = random.randrange(num_animals)
print(f'The animal at index number {random_animal_index} is {animals[random_animal_index]}')

# 3. Random Number from a list
import random

numbers = ['1','2','3','4','5','6','7','8','9','10']
print(len(numbers))
index_number = len(numbers)
numbers_rand = random.randrange(index_number)

print(f' The index number {numbers_rand} corresponds to the number {numbers[numbers_rand]}')


# Problems using randint()

# 1. Random Fruit Selector
import random
fruits = ['apple','banana','cherry','orange','strawberry']
num_fruits = len(fruits)
print(f' The number of fruits in this list are {num_fruits}')

random_fruit = random.randint(0,4)

print(f'The random fruit that has been chosen is {fruits[random_fruit]}')






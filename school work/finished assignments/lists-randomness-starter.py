# Arden Boettcher
# 10/23/24
# Lists Randomness Starter
import random
import colorama

print(colorama.Fore.GREEN + 'Problem 1' + colorama.Fore.RESET)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors_len = len(colors)
colors_rand = random.randrange(0, colors_len)

print(colors[colors_rand])



print(colorama.Fore.GREEN + '\nProblem 2' + colorama.Fore.RESET)

animals = ['dog', 'cat', 'snake', 'bird']

animals_len = len(animals)
animals_rand = lambda: animals[random.randrange(0, animals_len)]

print(f'randomly selected animal 1: {animals_rand()}')
print(f'randomly selected animal 2: {animals_rand()}')
print(f'randomly selected animal 3: {animals_rand()}')



print(colorama.Fore.GREEN + '\nProblem 3' + colorama.Fore.RESET)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_len = len(numbers)
numbers_rand = random.randrange(0, numbers_len)

print(f'The Number at the index of {numbers_rand} is {numbers[numbers_rand]}')



print(colorama.Fore.GREEN + '\nProblems Using Randint')
print('Problem 1' + colorama.Fore.RESET)

fruit = ['apple', 'banana', 'orange', 'strawberry', 'tomato']
# Tecnically fruit can be the plural of fruit so this is gramatically correct

fruit_len = len(fruit) - 1
fruit_rand = fruit[random.randint(0, fruit_len)]

print(f'Random Fruit GO: {fruit_rand}')



print(colorama.Fore.GREEN + '\nProblem 2' + colorama.Fore.RESET)

students = ['dave', 'greg', 'placeholder', 'oliver']

def score():
    return random.randint(0, 100)

students_len = len(students) - 1
students_rand = lambda: random.randint(0, students_len)

print(f'''{students[students_rand()].title()}\'s score is {score()}
{students[students_rand()].title()}\'s score is {score()}
{students[students_rand()].title()}\'s score is {score()}''')



print(colorama.Fore.GREEN + '\nProblem 3' + colorama.Fore.RESET)

movies = ['sharknado', 'lego batman', 'everything everywhere all at onece', 'the secret of kells']

movies_len = len(movies) - 1
movies_rand = random.randint(0, movies_len)

print(f'We\'re watching {movies[movies_rand].title()} tonight! (which is index #{movies_rand})')
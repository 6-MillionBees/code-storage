from random import randint


def d6():
    return randint(1, 6)

num = 0
num_list = []
while num < 5000:
    roll = [d6(), d6(), d6(), d6()]
    roll_sum = sum(roll) - min(roll)
    num_list.append(roll_sum)
    num += 1

if 3 in num_list:
    print(f'there is a 3 in index number {num_list.index(3)}')
print(num_list)
print(sum(num_list) / len(num_list))
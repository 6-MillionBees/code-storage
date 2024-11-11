# Arden Boettcher
# 10/28/24
# lists simple stats

chem_scores = [98, 75, 80, 90, 97, 87]

mean_chem_scores = round(sum(chem_scores) / len(chem_scores))

print(f'The average chem score is {mean_chem_scores}')

print()


# Lake Ann, Detroit, Lansing, Mackinaw City, and Chicago. In order
distance = [11.91, 149.46, 210.94, 82.09, 223.28]

print(f'The furthest drive is {max(distance)} miles away')
print(f'The closest drive is {min(distance)} miles away')
print(f'The average distance is {round(sum(distance) / len(distance))}')
# Arden Boettcher
# 12/2/24
# World Variables

days = 0
distance_traveled = 0

karma = 1

luck_bonus = 0

difficulty = 1 + days / 10 * karma

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)
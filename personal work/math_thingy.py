
max_v_list = [19436.2, 38872.4, 58308.6, 77744.8, 97181.0, 116617.3, 136053.5, 155489.7, 174925.9, 194362.1, 213798.3, 233234.5]

min_v_list = [12957.5, 25914.9, 38872.4, 51829.9, 64787.4, 77744.8, 90702.3, 103659.8, 116617.3, 129574.7, 142532.2, 155489.7]

astroid_mass = 1300000000000000
astroid_velocity = 4000
astroid_momentum = astroid_mass * astroid_velocity

ship_mass = 20003900

print('max velocities that work:')
for velocity in max_v_list:
    ship_momentum = ship_mass * velocity
    final_momentum = astroid_momentum - ship_momentum
    final_astroid_velocity = final_momentum / astroid_mass
    print(max_v_list.index(velocity) + 1, ':', final_astroid_velocity, final_momentum, ship_momentum)


print('min velocities that work:')
for velocity in min_v_list:
    ship_momentum = ship_mass * velocity
    final_momentum = astroid_momentum - ship_momentum
    final_astroid_velocity = final_momentum / astroid_mass


    print(min_v_list.index(velocity) + 1, ':', final_astroid_velocity, final_momentum, ship_momentum)
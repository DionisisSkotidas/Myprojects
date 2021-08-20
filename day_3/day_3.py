while True:
    print('Welcome to the Treasure island.Your mission is to find the treasure')
    cross_road = input('Would you like to go Left or Right?')
    if cross_road.upper() == 'LEFT':
        lake = input('You have come to a lake. '
                     'There is an island in the middle of the lake.'
                     'Type "wait" to wait for a boat.'
                     'Type "swim" to swim across. ')
        if lake.upper() == 'WAIT':
            doors = input('a boat come and it took you to an island with three doors'
                          'a red ,a yellow and blue one.'
                          'Type what door you want to go in')
            if doors.upper() == 'Yellow':
                print('You Win!!!')
            else:
                print('Game Over.')
        else:
            print('Game Over.')
    else:
        print('Game Over')
for i in range(2, 5):
    for j in range(1, 6):
        if i*j >= 10:
            print('{} * {} = {}'.format(i, j, i*j), end="   ")
        else:
            print('{} * {} =  {}'.format(i, j, i * j), end="   ")
    print()
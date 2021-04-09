from random import *
a=[
    'Green Knight',
    'Red Knight',
    'Blue Knight',
    'Orange Knight',
    'Gray Knight',
    'Barbarian',
    'Thief',
    'Fencer',
    'Killer Beekeeper',
    'Industrialist',
    'Alien Hominid',
    'The King',
    'Brute',
    'Snakey',
    'Saracen',
    'Royal Guard',
    'Stove Face',
    'Peasant',
    'Bear Shaman',
    'Necromancer',
    'Conehead',
    'Civilian',
    'Unmasked Gray Knight',
    'Fire Demon',
    'Skeleton',
    'Iceskimo',
    'Ninja',
    'Cult Minion',
    'Pink Knight',
    'Blacksmith',
    'Hatty Hattington']
while True:
    for i in range (randint(1000,10000)):
        i=randint(1,len(a)-1)
    input(a[i])

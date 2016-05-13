#!/usr/bin/env python

from Map import Map
from Mower import Mower

### MAIN ###

from sys import stdin, exit

mapSize = stdin.readline().strip().split(' ');
if len(mapSize) != 2:
    raise Exception('map size definition error');

map = Map(int(mapSize[0]), int(mapSize[1]));
mowers = [];

line = stdin.readline();
while line:
    mowerDef = line.strip().split(' ');
    if len(mowerDef) != 3:
        raise Exception('mower def error');
    mower = Mower(int(mowerDef[0]), int(mowerDef[1]), mowerDef[2][0]);
    if not map.onMap(mower):
        raise Exception('mower not in the map');
    actions = list(stdin.readline().strip());
    for action in actions:
        if (action == 'G'):
            mower.left();
        elif (action == 'D'):
            mower.right();
        elif (action == 'A'):
            mower.walk();
            if not map.onMap(mower):
                mower.back();
        else:
            raise Exception('mower bad action');
    print mower.x, mower.y, mower.getDirectionLetter();
    line = stdin.readline();

### END MAIN ###
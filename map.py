#! -*- coding: utf-8 -*-


'''
Created on Jan 26, 2018

@author: Jesús Molina
'''


import sys
import os
from hero import Hero

class Map(object):
    '''
    classdocs
    '''
    initialMap =      [[0,0,0,0,0,0,0], #0 represents a wall (#), 1 represents the floor (-) and 2 is the hero(@).
                       [0,1,1,1,1,1,3],
                       [0,1,1,1,1,1,0],
                       [0,1,1,1,1,1,0],
                       [0,3,0,0,0,0,0]]
    
    caveMap =            [[0,0,0,0,0,0], #0 represents a wall (#), 1 represents the floor (-) and 2 is the hero(@).
                          [3,1,1,1,4,0],
                          [0,1,1,1,1,0],
                          [0,0,0,0,0,0]]
    
    currentMap = initialMap
    
    
    def __init__(self):
        
        self.instanceHero = Hero()
        
    def generateMap(self, parameterMap=initialMap): #converts the integers of map into ASCII symbols.
        for x in range(len(parameterMap)):
            print "\n"
            for y in range(len(parameterMap[x])):
                if parameterMap[x][y] == 0:
                    sys.stdout.write('#')#wall.
                    sys.stdout.write(' ') #I had to insert spaces between each symbol, so the map won't be deformed on the screen.
                elif parameterMap[x][y] == 2:
                    sys.stdout.write('@') #@ is the hero's symbol.
                    sys.stdout.write(' ')
                elif parameterMap[x][y] == 3: #This is a door.
                    sys.stdout.write('+')
                    sys.stdout.write(' ')
                elif parameterMap[x][y] == 4:
                    sys.stdout.write('D') #this represents the monster.
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('-')#floor.
                    sys.stdout.write(' ')
    
                    
    def updateMap(self, heroMove):        
        instanceHeroPos = self.instanceHero.getHeroPos()
        updateInstanceHeroPosX = instanceHeroPos[0] + heroMove[0]
        updateInstanceHeroPosY = instanceHeroPos[1] + heroMove[1]
        
        clear = lambda: os.system('cls')
        clear() #the screen is wiped everytime the map updates.
        
        if self.currentMap[updateInstanceHeroPosX][updateInstanceHeroPosY] == 0:
            print "you've reached the wall"
        elif self.currentMap[updateInstanceHeroPosX][updateInstanceHeroPosY] == 3:
            self.currentMap = self.caveMap
            self.instanceHero.setHeroPos([1,1])
            self.generateMap(self.currentMap)
                        
        else:
            self.currentMap[updateInstanceHeroPosX][updateInstanceHeroPosY] = 2
            heroPos = [updateInstanceHeroPosX, updateInstanceHeroPosY]
            self.instanceHero.setHeroPos(heroPos)
            self.generateMap(self.currentMap)
        

#! -*- coding: utf-8 -*-

'''
Created on Jan 25, 2018

@author: Jesús Molina
'''
import os
from tittleScreen import TittleScreen
from map import Map
from control import Control


if __name__ == '__main__':
    
    clear = lambda: os.system('cls')#lambda function to clear the srceen.
    
    tittle = TittleScreen()
    tittle.startScreen()
    
    clear()
    
    mapInstance = Map()
    mapInstance.generateMap()
    
    instanceControl = Control()
    while True:
        heroMove = instanceControl.userMovement()
        mapInstance.updateMap(heroMove)
    
    
    

        
        
        
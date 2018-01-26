#! -*- coding: utf-8 -*-


'''
Created on Jan 26, 2018

@author: Jes�s Molina
'''

class Hero(object):
    '''
    classdocs
    '''
    def __init__(self, strength = 10, hp = 100):
        self.__strength = strength
        self.__hp = hp
        self.__heroPos = [1,1]
    
    
    def getHeroPos(self):
        return self.__heroPos
    def setHeroPos(self, heroPos):
        self.__heroPos = heroPos
        
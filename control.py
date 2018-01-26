#! -*- coding: utf-8 -*-


'''
Created on Jan 26, 2018

@author: Jesús Molina
'''


class Control(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    
    def userMovement(self):
        
        movement = raw_input('where to?')
        if movement == 'd':
            heroMove = [0,1]
            return heroMove 
        elif movement == 's':
            heroMove = [1,0]
            return heroMove
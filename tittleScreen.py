#! -*- coding: utf-8 -*-
'''
Created on Jan 26, 2018

@author: Jesús Molina
'''


import winsound
import time


class TittleScreen(object):
    '''
    classdocs
    '''
    __asciiTittle =     ['##############',
                          '#############',
                          '    #####    ########  #######      #       #######  #      #  ########  #######',
                          '    #####    #      #  #           # #      #        #      #  #      #  #      ',
                          '    #####    #######   #          #   #     #        #      #  #######   #      ',
                          '    #####    #  #      ######    ######     #######  #      #  #  #      ######',
                          '    #####    #   #     #        #       #         #  #      #  #   #     #      ',
                          '    #####    #    #    ######  #         #  #######  ########  #    #    #######',
                          '                                                                                ',
                          '                                               ########     #   #       # ######',
                          '                                               #           # #   #     #  #     ',
                          '                                               #          #   #   #   #   ##### ',
                          '                                               #         #######   # #    #     ',
                          '                                               ######## #       #   #     ###### ']

    
    
    def startScreen(self):
    
        for x in self.__asciiTittle:
            print x
        
        '''
        winsound.PlaySound("tittle_theme.wav", winsound.SND_ASYNC)#Plays a wav file for 6 seconds.
        time.sleep(1)
        winsound.PlaySound(None, winsound.SND_PURGE)#This stops the sound.
        '''    
    
    
    
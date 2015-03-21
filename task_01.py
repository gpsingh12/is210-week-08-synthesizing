#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
"""
def get_matches(players):
    """ 
    """
    player = []
    for myind1, myitem1 in enumerate(players):
        for myind2, myitem2 in enumerate(players):
         if myind1 < myind2:
             list1 = (myitem1, myitem2)
             player.append(list1)

    return player
 

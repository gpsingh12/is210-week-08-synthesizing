#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""Module creates versus matchup for players.
"""
def get_matches(players):
    """ Function takes input as a list of players names.
        Arg:
            players(list): Input value of players names.
        Return:
             returns newly created list of tuples.
        Examples:
              >>>  get_matches(['Jim', 'Jay', 'Max'])
                [('Jim', 'Jay'), ('Jim', 'Max'), ('Jay', 'Max')]
    """
    player = []
    for myind1, myitem1 in enumerate(players):
        for myind2, myitem2 in enumerate(players):
         if myind1 < myind2:
             list1 = (myitem1, myitem2)
             player.append(list1)

    return player
 

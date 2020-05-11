# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:36:35 2020

@author: hanse
"""


def solution(participant, completion):
    for i in participant:
        if i in completion:
            print(i)
            participant.remove(i)
            completion.remove(i)
            print(participant, completion)
        else:
            return print(i)
        
p1 = ['leo', 'kiki', 'eden']
c1 = ['eden', 'kiki']
p2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa'] 
c2 = ['josipa', 'filipa', 'marina', 'nikola']
p3 = ['mislav', 'stanko', 'mislav', 'ana']; c3 = ['stanko', 'ana', 'mislav']

#solution(p1, c1)
solution(p2, c2)
#solution(p3, c3)

#answer leo / vinko / mislav




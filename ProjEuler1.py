# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:11:32 2023

@author: drewa
"""

### Project Euler problem 1 solution ###

""" Problem statement: Find the sum of all the multiples
of 3 or 5 below 1000"""

Mult_3_5 = [n for n in range(1, 1000) if (n % 3 ==0) | (n % 5 == 0)]

sum(Mult_3_5)k
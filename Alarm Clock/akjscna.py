# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:43:53 2019

@author: Shankar Jadhav
"""
import time
CurrentTime = time.strftime("%H:%M")

mins=CurrentTime[-2]+CurrentTime[-1]
mins=int(mins)
if mins<=57:
    mins+=2
newtime=CurrentTime[:-2:]+str(mins)
print(mins)
print(CurrentTime)
print(newtime)
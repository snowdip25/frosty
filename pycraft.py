# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
t=0

while True:
    t=t+1
    mc.postToChat('第'+str(t)+'次')
    
   
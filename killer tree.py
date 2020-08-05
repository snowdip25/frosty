# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE

"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def plantTree(x,y,z):
    
    mc.setBlocks(x-1,y+3,z-1,x+1,y+4,z+1,79)
    mc.setBlocks(x,y+3,z,x,y,z,25)
x,y,z = mc.player.getTilePos()

for i in range(10):
    for j in range(10):
        for k in range(10):
            plantTree(x+i*5,y+i*j,z+i*k)
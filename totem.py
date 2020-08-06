# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE

"""
# 神秘圖騰

from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

for i in range(20):

    r = random.randrange(1, 5)
    
    if r == 1:
        mc.setBlocks(x, y, z, x+3, y, z,4 )
        x = x+3
    elif r == 2:
        mc.setBlocks(x, y, z, x-3, y, z, 4)
        x = x-3
    elif r == 3:
        mc.setBlocks(x, y, z, x, y, z+3,4 )
        z = z+3
    elif r == 4:
        mc.setBlocks(x, y, z, x, y, z-3,4 )
        z = z-3
    elif r == 5:
        mc.setBlocks(x, y, z, x, y+3, z,4 )
        y = y+3
    elif r == 6:
        mc.setBlocks(x, y, z, x, y-3, z,4 )
        y = y-3

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""

import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

a = 0
while a<3:   
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x-5,y-1,z,x+5,y-10,z,19)
    z = z+4
    a = a+1           
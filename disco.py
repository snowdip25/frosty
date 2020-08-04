# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
time.sleep(3)


x,y,z=mc.player.getTilePos()
while True:

    color = random.randrange(16)
    mc.setBlocks(x+23,y-1,z+23,x-23,y-1,z-23,95,color)
    time.sleep(0.5)


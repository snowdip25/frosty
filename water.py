# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y,z,19)
    time.sleep(10)


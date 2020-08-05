# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE

"""
import random
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos = mc.player.getTilePos()

while True:
    y = pos.y+30
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.5)
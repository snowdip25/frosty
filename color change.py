# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()


while True:
    x,y,z=mc.player.getTilePos()
    color = random.randrange(16)
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)
   


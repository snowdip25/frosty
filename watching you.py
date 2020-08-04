# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
t=0

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("you are located on x:"+str(x)+", y:"+str(y)+",z:"+str(z))
    
   
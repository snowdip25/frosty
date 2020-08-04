# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()



x,y,z=mc.player.getTilePos()

mc.setBlocks(x+23,y-1,z+23,x-23,y-1,z-23,100)


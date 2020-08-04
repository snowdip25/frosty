# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()



x,y,z=mc.player.getTilePos() mc.setBlock(x,y,z,102,5)
mc.setBlock(x,y+1,z,102,5)
mc.setBlock(x,y+2,z,102,5)
mc.setBlock(x,y+3,z,102,5) 
mc.setBlock(x,y+4,z,102,5)
mc.setBlock(x,y+5,z,102,5) 
mc.setBlock(x,y+6,z,102,5) 
mc.setBlock(x,y+7,z,102,5) 
mc.setBlock(x,y+8,z,102,5)
    
   
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getTilePos()

mc.setSign(x,y,z,63,0,"我愛","minecraft","也愛",'python')
           
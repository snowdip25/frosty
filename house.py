# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""
import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
width = 15
height = 6
length = 20

block = 168
air = 0
mc.setBlocks(x,y,z,x+length,y+height,z+width, block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,air)


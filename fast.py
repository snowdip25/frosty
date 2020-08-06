# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE

"""
# 神秘圖騰

from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

while True:
    mc.executeCommand("time add 100")
    sleep(0.05)
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:29:00 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

userName = input("請輸入姓名: ")
message = input("請輸入發言: ")
mc.postToChat(" ["+userName + "] " + message)
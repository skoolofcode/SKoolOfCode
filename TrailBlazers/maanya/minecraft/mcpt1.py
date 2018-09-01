from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Hello! This is Maanya's version of Raspberry Pi!")
sleep(7)
pos = mc.player.getPos()
x,y,z = mc.player.getPos()
mc.player.setPos(x + 200,y + 87, z + 2)

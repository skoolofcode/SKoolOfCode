from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
mc.postToChat("Hello, this is mudit 2 version of Minecraft")
mc.postToChat("This version will make a block(stoneonly) bigger ")

stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+13, y+13, z+13, stone)

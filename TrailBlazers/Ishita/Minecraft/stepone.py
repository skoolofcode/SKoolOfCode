from mcpi.minecraft import Minecraft
mc = Minecraft.create()
stone = 1
import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to find these blocks when I will teleport you every 20 seconds.")
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)

while True:
  mc.player.setPos(x+10, y+150, z+5) 
  time.sleep(60)
      



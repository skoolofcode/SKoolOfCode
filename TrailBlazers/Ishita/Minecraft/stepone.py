from mcpi import minecraft
mc = minecraft.Minecraft.create()
stone = 1
import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to find these blocks when I will teleport you every 20 seconds.")
x, y, z = mc.player.getPos()
mc.setBlocks(x +1, y+1, z+1, x+1, y+1, z+1, stone)

while True:
  mc.player.setPos(x+100, y+150, z+500) 
  a,b,c = mc. player.getPos()
  time.sleep(20)
  if x,y,z == a,b,c:
    mc.postToChat("Well done! You have won!!!")
      



from mcpi import minecraft
mc = minecraft.Minecraft.create()
stone = 1
import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to mke a structure in 20 seconds. Then I will teleport you. You have to try to find the structure that you built.") 
mc.postToCHat("GO quickly to find the position where you will build! You have exactoly 10 seconds!")
time.sleep(10)
x,y,z = mc.player.getPos()

mc.postToChat("Allright! 20 seconds to build!") 
time. sleep(20)
mc.player.setPos(x + 10,y + 100, z +9)

while True:
  time.sleep(10)
  a,b,c = mc. player.getPos()
  if x == a:
    if y == b:
      if z == c:
        mc.postToChat("Well done! You have won!!!")
        
    
    
    
    

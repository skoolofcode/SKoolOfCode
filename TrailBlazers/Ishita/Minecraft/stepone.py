from mcpi import minecraft
mc = minecraft.Minecraft.create()

import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to mke a structure in 10 seconds. Then I will teleport you. You have to try to find the structure that you built.") 
mc.postToChat("GO quickly to find the position where you will build! You have exactoly 10 seconds!")
time.sleep(10)
x,y,z = mc.player.getPos()

mc.postToChat("Allright! 10 seconds to build!") 
time. sleep(10)
mc.player.setPos(x + 1000,y + 1000, z +1000)

while True:
  time.sleep(10)
  a,b,c = mc. player.getPos()
  if x == a:
     mc.postToChat("Well done! You have won!!!")
  else:
    if y == b:
       mc.postToChat("Well done! You have won!!!")
    else:
      if z == c:
        mc.postToChat("Well done! You have won!!!")
        
    
    
    
    

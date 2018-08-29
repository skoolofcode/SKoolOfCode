from mcpi import minecraft
mc = minecraft.Minecraft.create()
stone = 1
import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to mke a structure in 20 seconds. Then I will teleport you. You have to try to find the structure that you built.") 
mc.postToChat("WHen you have chosen the location you want to build with, type 1.")
mc.postToCHat("GO quickly to find the position where you will build! You have exactoly 10 seconds!")

time.sleep(10)

pos = mc.player.getPos()
mc.postToChat("Allright! 20 seconds to build!") 
time. sleep(20)
mc.player.setPos(pos + 100)

while True:
  time.sleep(10)
  a = mc. player.getPos()
  if pos == a:
    mc.postToChat("Well done! You have won!!!")
      



from mcpi import minecraft
mc = minecraft.Minecraft.create()
stone = 1
import time

mc.postToChat("Hello Player! Welcome to my Minecraft version! You will try to mke a structure in 20 seconds. Then I will teleport you. You have to try to find the structure that you built.") 
mc.postToChat("WHen you have chosen the location you want to build with, type 1.")
m = input("Now don't you move move once you have typed 1. ")

if m == "1":
  pos = mc.player.getPos()
  
time. sleep(20)
mc.player.setPos(pos + 100)

while True:
  time.sleep(10)
  a = mc. player.getPos()
  if pos == a:
    mc.postToChat("Well done! You have won!!!")
      



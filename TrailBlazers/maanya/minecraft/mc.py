from mcpi import minecraft
from mcpi import block
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Hello! This is Maanya's version of Raspberry Pi!")
sleep(7)
pos = mc.player.getPos()
x,y,z = mc.player.getPos()
mc.player.setPos(x + 200,y + 87, z + 2)
mc.postToChat("Okay...Listen up. You have 15 seconds to build me a structure! READY? SET? GO!")
sleep(15)
mc.player.setPos(x + 768,y + 254, z + 7)
mc.postToChat("HaHaHa! I teleported you to another part of the terrain! Go on, continue wandering, you'll be teleported soon enough!")
sleep(12)
mc.player.setPos(x + 558,y + 77, z + 80)
mc.postToChat("DON'T MOVE! I have a surprise for you. If you don't see it, try spinning around.  ")
wool = 35
wood = 17
magenta = 2
mc.setBlock(x + 1, y, z, wool, magenta)
mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 11, z + 11, wood)
mc.postToChat("Did you like my little surprise? Anyway, I will teleport you now, when you get there look around for the TNT Block! Use your sword to left click the TNT Block! HAVE FUN!")
mc.player.setPos(x + 2357, y, z + 1234)
TNT = 46
mc.setBlock(x + 1, y, z, TNT, 1)
mc.postToChat("Ready to see something cool?")
mc.player.setPos(x + 342, y, z + 43)
lava = 10
water = 8
air = 0
mc.setBlock(x+3, y+5, z, lava)
sleep(20)
mc.setBlock(x+4,y+5, z, water)
sleep(5)
mc.setBlock(x+5, y+5, z, air)



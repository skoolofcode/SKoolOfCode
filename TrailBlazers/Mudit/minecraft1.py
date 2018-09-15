from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
mc.postToChat("Hello, this is mudit version of Minecraft")
mc.postToChat("This version will make granite drop wherever u go")
granite = 38

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, granite)
    sleep(0.1)

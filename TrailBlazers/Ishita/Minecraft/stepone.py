from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello Student! Welcome to my Minecraft version!")
x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z)

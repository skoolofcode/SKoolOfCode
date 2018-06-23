#Intoruction to Modules
##Create a mobile hello that has 2 functions. helloWorld() and helloWA()

#Diffirent way of importing the module
#1. Import module as is with its own name. Usage import <module>
import hello10
#hello10.helloWorld()
#hello10.counter = 40
#hello10.helloWorld()


#2. Import module and give it a name. Usage import <module> <given name>
import hello10 as myhelloMod
import hello10 as myhelloMod2
#myhelloMod.helloWA()
myhelloMod.helloWorld()
myhelloMod.counter = 40
myhelloMod2.helloWorld()

#3. Import specific items from a  module. 
from hello10 import helloWorld
#helloWorld()

#4 Import a specific item from a module and give it a name
from hello10 import helloWorld as myHelloWorld
#myHelloWorld()

## Variables in a module

##Modules are singleton i.e. diffirent aliases represent the same module

##Multiple modules
import config
import hello11 as myhelloMod11
myhelloMod11.helloWorld()
config.counter = 30
myhelloMod11.helloWorld()
myhelloMod.helloWorld()

#Global variables are shared across main and all pther modules
#Standard practice to define them is to given them a module of their own

print(dir(myhelloMod11))






















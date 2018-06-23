#introduction to Modules
#Let's create a module hello that has 2 function helloWorld() and helloRedmond()

#Diffirent ways of importing the module
#1. Import module as is with its name. Note the usage <module>.<function>
import hello 
hello.helloWorld()
hello.helloWorld()

#2. Import module and give it name. Usage <module given name>.<function>
import hello as myHelloMod
myHelloMod.helloRedmond()
myHelloMod.helloWorld()

#3. Import specific items in a module. Usage <function_name>()
from hello import helloRedmond
helloRedmond()

#4. Import specific items in a module and give it a name. Usage <module_given_name>()
from hello import helloRedmond as localHello
localHello()

#Note : Import statments can be placed just before usage. Not really start of file

#Accessing variables in a module.
#Lets have a variable called myvariable in hello module
import hello as helloM
import config as cfg
cfg.helloVar = 40
myHelloMod.helloRedmond()

#Python modules are singletons. Does not matter how many 
#times you import, you are referencing the same module
import hello as tello
tello.helloRedmond()


#2 diffirent modules. Let's have hello2 module. Can i have same name functions?
import hello2 as helloM2
helloM2.helloRedmond()

#Global variables that are shared across main and all the modules
#Standard practice is to have a module for variables. e.g. config or settings


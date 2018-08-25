
#introduction to Modules
#Let's create a module hello that has 2 function helloWorld() and helloRedmond()


#Diffirent ways of importing the module
#1. Import module as is with its name. Note the usage <module>.<function>
import hello 

hello.helloIssaquah()
hello.helloRedmond()
hello.helloSeattle()

hello.helloBangalore()

#2. Import module and give it name. Usage <module given name>.<function>
import hello as myHello

myHello.helloIssaquah()
myHello.helloRedmond()
myHello.helloSeattle()

myHello.helloBangalore()


#3. Import specific items in a module. Usage <function_name>()
from hello import helloSeattle
helloSeattle()

#4. Import specific items in a module and give it a name. Usage <module_given_name>()
from hello import helloRedmond as angadsHello
angadsHello()


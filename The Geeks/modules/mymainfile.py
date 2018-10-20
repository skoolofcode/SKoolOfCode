#We'll talk about Modules and how to use variables across diffirent modules.
import module1 as m1 
import module2 as m2
import myGlobals as g 

g.myVariable = 99999

m1.hello_module1()
m2.hello_module2()
print("The global variable here is ", g.myVariable)
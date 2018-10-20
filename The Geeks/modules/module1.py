import myGlobals as m1_g

def hello_module1():
    m1_g.myVariable = 88888
    print("Hello : I am module 1")
    print("M1 : I am accessing the global varaible ", m1_g.myVariable)
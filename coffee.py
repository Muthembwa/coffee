#coffee machine, pogramming logic practice
def make_coffee():
    """makes coffee"""
    ingredients= ["coffee", "Hot_Water"]
    print ("take a mug")
    print("Tear the coffee sachet ")
    print ("pour into the  {}".format (','.join(ingredients)))
    print ("stir your coffee for atleast 5 seconds")
    my_coffee = "Tasty coffee"
    return my_coffee
def serves_coffee(make_coffee, Person_served):
    """serves coffee"""
    print ("hello, have your {} {}".format(make_coffee,Person_served))

me= make_coffee()
serves_coffee(me, 'Jafi')

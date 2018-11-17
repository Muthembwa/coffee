#coffee machine, pogramming logic practice
def make_coffee(*options):
    """makes coffee"""
    ingredients= ["coffee", "Hot_Water"]
    if options:

        ingredients.append(','.join(options))
    print ("take a mug")
    print("Tear the coffee sachet ")
    print ("pour into the  {}".format (','.join(ingredients)))
    print ("stir your coffee for atleast 5 seconds")

    if options:
        my_coffee= "Tasty coffee with {}".format(','.join(options))
    else:
        my_coffee = "Tasty coffee"
    return my_coffee
def serves_coffee(make_coffee, Person_served):
    """serves coffee"""
    print ("hello, have your {} {}".format(make_coffee,Person_served))

plain=make_coffee()
withS=make_coffee('sugar')
withM=make_coffee('milk')
withMaS= make_coffee('milk','and sugar')
serves_coffee(plain, 'Jafi')
serves_coffee(withS, 'Jemo')
serves_coffee(withMaS, 'Jafi')

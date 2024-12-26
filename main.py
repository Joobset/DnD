from Characters.Character import Character

if __name__ == "__main__":
    race = input("What race do you want to be?")
    if race == "Mage":
        person = Mage("Joe", 14)
    me = Character()
    print(me.name)
    print(me.die()), 
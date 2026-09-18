import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here
    
    def attack(self):
        return self.strength
        # your code here

    def receiveDamage(self, damage):
        self.health -= damage
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        # your code here

    def battleCry(self):
        return "Odin Owns You All!"
        # your code here

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        # your code here

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        # your code here

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        # your code here

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        # your code here
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        # your code here
    
    def vikingAttack(self):
        import random
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return result 
        # your code here
    
    def saxonAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        result = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return result
        # your code here

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
        # your code here
    pass


# Import the classes from vikingsClasses.py
from vikingsClasses import Viking, Saxon, War

import random


def create_viking_team(war, names):
    """
    Create a Viking army and add the Vikings to the War.

    Each Viking receives:
        - a name from the names list
        - 100 health
        - 20 strength
    """

    for name in names:
        viking = Viking(name, 100, 20)
        war.addViking(viking)


def create_saxon_team(war, number):
    """
    Create a Saxon army.

    Each Saxon receives:
        - 100 health
        - 10 strength
    """

    for _ in range(number):
        saxon = Saxon(100, 10)
        war.addSaxon(saxon)


def run_game():
    """
    Create the two armies and run the battle until
    one of the armies has no soldiers left.
    """

    # Create a new War.
    war = War()

    # Names for our Viking army.
    viking_names = [
        "Ragnar",
        "Lagertha",
        "Bjorn",
        "Ivar",
        "Floki"
    ]

    # Create the Viking team.
    create_viking_team(war, viking_names)

    # Create a Saxon team with the same number of soldiers.
    create_saxon_team(war, len(viking_names))

    print("The war begins!")
    print("----------------")

    # Continue fighting while both armies have soldiers.
    while war.vikingArmy and war.saxonArmy:

        # Randomly decide which army attacks first.
        if random.choice([True, False]):

            # Viking attacks a random Saxon.
            result = war.vikingAttack()
            print(result)

            # If Saxons are still alive, they attack back.
            if war.saxonArmy:
                result = war.saxonAttack()
                print(result)

        else:

            # Saxon attacks a random Viking.
            result = war.saxonAttack()
            print(result)

            # If Vikings are still alive, they attack back.
            if war.vikingArmy:
                result = war.vikingAttack()
                print(result)

    # Display the final result of the war.
    print("----------------")
    print(war.showStatus())


# Start the game when this file is executed.
if __name__ == "__main__":
    run_game()
"""
This code counts the total amount of animal bones on a farm,
then computes the amount of bone sculptures McDonald can purchase
from the artist using the amount of bones on his farm.
"""

CHICKEN_BONES = 120
PIG_BONES = 223
COW_BONES = 208
GOAT_BONES = 189

TURTLE_SCULP = 100
BIRD_SCULP = 250
BUTTERFLY_SCULP = 600
WHALE_SCULP = 1500
ARRAY_SCULP = 4*TURTLE_SCULP + 3*BIRD_SCULP + 2*BUTTERFLY_SCULP + WHALE_SCULP

def total_number_of_bones(chickens, pigs, cows, goats):
    """
    Calculate the total number of legs among all of the animals
    """
    # Find the total number of legs per animal
    total_chickens = CHICKEN_BONES * chickens
    total_pigs = PIG_BONES * pigs
    total_cows = COW_BONES * cows
    total_goats = GOAT_BONES * goats

    return total_chickens + total_pigs + total_cows + total_goats

if __name__ == '__main__':
    chickens = int(input("How many chickens are there? "))
    pigs = int(input("How many pigs are there? "))
    cows = int(input("How many cows are there? "))
    goats = int(input("How many goats are there? "))

    if chickens < 0:
        print("Too small")
    elif chickens > 100:
        print("Too Many")

    if pigs < 0:
        print("Too small")
    elif pigs > 100:
        print("Too Many")

    if cows < 0:
        print("Too small")
    elif cows > 100:
        print("Too Many")

    if goats < 0:
        print("Too small")
    elif goats > 100:
        print("Too Many")


    total_bones = total_number_of_bones(chickens, pigs, cows, goats)
    turtle_sculptures = (total_bones // TURTLE_SCULP) 
    bird_sculptures = (total_bones // BIRD_SCULP) 
    butterfly_sculptures = (total_bones // BUTTERFLY_SCULP) 
    whale_sculptures = (total_bones // WHALE_SCULP) 
    array_sculptures = (total_bones // ARRAY_SCULP) 
    bones_remaining = int((total_bones / TURTLE_SCULP) % TURTLE_SCULP)
    print(f"""You have {total_bones} bones amongst all of the animals 
          which means you can purchase {turtle_sculptures} turtle sculptures 
          or {bird_sculptures} bird sculptures or {butterfly_sculptures} 
          butterfly sculptuers or {whale_sculptures} whale sculptures, 
          or {array_sculptures} array sculptures with {bones_remaining} 
          bones left over to give to my dog.""")
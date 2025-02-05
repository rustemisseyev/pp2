def solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2) / 2
    chickens = numheads - rabbits
    return rabbits, chickens

numheads = 35
numlegs = 94
print(solve(numheads, numlegs))
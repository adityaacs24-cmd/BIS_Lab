import random
import math

def fitness(x):
    return x ** 2

mode = "min" # Change to "max" for maximization

n = 20
iterations = 100
pa = 0.25
step_size = 0.1
low, high = -10, 10
beta = 1.5

def better(a, b):
    return a < b if mode == "min" else a > b

def levy():
    sigma = (
        math.gamma(1 + beta) * math.sin(math.pi * beta / 2)
        / (math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))
    ) ** (1 / beta)
    u = random.gauss(0, sigma)
    v = random.gauss(0, 1)
    return u / (abs(v) ** (1 / beta))

nests = [random.uniform(low, high) for _ in range(n)]

for _ in range(iterations):

    for i in range(n):
        new = nests[i] + step_size * levy()
        new = max(low, min(high, new))
        j = random.randrange(n)

        if better(fitness(new), fitness(nests[j])):
            nests[j] = new

    nests.sort(key=fitness, reverse=(mode == "min"))

    for i in range(math.ceil(pa * n)):
        nests[i] = random.uniform(low, high)

best = (min if mode == "min" else max)(nests, key=fitness)
print("Best solution:", best)
print("Best fitness:", fitness(best))
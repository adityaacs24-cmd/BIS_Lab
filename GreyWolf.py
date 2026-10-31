import random

def fitness(x):
    return x ** 2

mode = "min" # Change to "max" for maximization

wolves = 20
iterations = 100
low, high = -10, 10

def better(a, b):
    return a < b if mode == "min" else a > b

pos = [random.uniform(low, high) for _ in range(wolves)]

for t in range(iterations):

    ranked = sorted(pos, key=fitness, reverse=(mode == "max"))
    alpha = ranked[0]
    beta = ranked[1]
    delta = ranked[2]
    a = 2 - 2 * t / iterations

    for i in range(wolves):
        x = pos[i]
        new_positions = []

        for leader in [alpha, beta, delta]:
            r1 = random.random()
            r2 = random.random()
            A = 2 * a * r1 - a
            C = 2 * r2

            D = abs(C * leader - x)
            new_x = leader - A * D
            new_positions.append(new_x)

        pos[i] = sum(new_positions) / 3
        pos[i] = max(low, min(high, pos[i]))

best = (min if mode == "min" else max)(pos, key=fitness)
print("Best solution:", best)
print("Best fitness:", fitness(best))

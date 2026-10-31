import random

def fitness(x):
    return x ** 2

mode = "min"  # Change to "max" for maximization

particles = 20
iterations = 100
w = 0.5
c1 = 1.5
c2 = 1.5
low, high = -10, 10

def better(a, b):
    return a < b if mode == "min" else a > b

pos = [random.uniform(low, high) for _ in range(particles)]
vel = [random.uniform(-1, 1) for _ in range(particles)]
pbest = pos.copy()
gbest = (min if mode == "min" else max)(pos, key=fitness)

for _ in range(iterations):
    for i in range(particles):

        if better(fitness(pos[i]), fitness(pbest[i])):
            pbest[i] = pos[i]

        if better(fitness(pbest[i]), fitness(gbest)):
            gbest = pbest[i]

        r1, r2 = random.random(), random.random()

        vel[i] = (
                w * vel[i]
                + c1 * r1 * (pbest[i] - pos[i])
                + c2 * r2 * (gbest - pos[i])
        )

        pos[i] += vel[i]
        pos[i] = max(low, min(high, pos[i]))

print("Best position:", gbest)
print("Best fitness:", fitness(gbest))

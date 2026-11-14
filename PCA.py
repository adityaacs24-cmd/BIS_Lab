import random

def fitness(x):
    return x ** 2

mode = "min" # Change to "max" for maximization
cells = 20
iterations = 100
low, high = -10, 10
step_size = 0.

def better(a, b):
    return a < b if mode == "min" else a > b

population = [random.uniform(low, high) for _ in range(cells)]

best = (min if mode == "min" else max)(
    population, key=fitness
)

for _ in range(iterations):

    new_population = population.copy()

    for i in range(cells):
        left = population[(i - 1) % cells]
        right = population[(i + 1) % cells]
        candidates = [population[i], left, right]
        local_best = (min if mode == "min" else max)(
            candidates, key=fitness
        )

        new_position = population[i] + step_size * (
            local_best - population[i]
        )

        new_population[i] = max(low, min(high, new_position))

    population = new_population

    current_best = (min if mode == "min" else max)(
        population, key=fitness
    )

    if better(fitness(current_best), fitness(best)):
        best = current_best

print("Best solution:", best)
print("Best fitness:", fitness(best))

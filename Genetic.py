import random

def fitness(x):
    return x ** 2

population_size = 10
generations = 50
mutation_rate = 0.1
chromosome_length = 5

population = [
    [random.randint(0, 1) for _ in range(chromosome_length)]
    for _ in range(population_size)
]

def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)

for _ in range(generations):
    population.sort(key=lambda x: fitness(decode(x)), reverse=True)
    parents = population[:2]
    new_population = parents.copy()

    while len(new_population) < population_size:
        p1, p2 = random.sample(parents, 2)
        point = random.randint(1, chromosome_length - 1)
        child = p1[:point] + p2[point:]

        for i in range(chromosome_length):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population

best = max(population, key=lambda x: fitness(decode(x)))
print("Best chromosome:", best)
print("Best solution:", decode(best))
print("Maximum fitness:", fitness(decode(best)))

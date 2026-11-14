import random

def fitness(x):
    return x ** 2

population_size = 10
generations = 50
gene_length = 5
mutation_rate = 0.1
crossover_rate = 0.8

population = [
    [random.randint(0, 1) for _ in range(gene_length)]
    for _ in range(population_size)
]

def express(genes):
    return int("".join(map(str, genes)), 2)

for _ in range(generations):

    population.sort(
        key=lambda genes: fitness(express(genes)),
        reverse=True
    )

    parents = population[:2]
    new_population = parents.copy()

    while len(new_population) < population_size:

        p1, p2 = random.sample(parents, 2)

        if random.random() < crossover_rate:
            point = random.randint(1, gene_length - 1)
            child = p1[:point] + p2[point:]
        else:
            child = p1.copy()

        for i in range(gene_length):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population

best = max(population, key=lambda genes: fitness(express(genes)))
solution = express(best)
print("Best genetic sequence:", best)
print("Best solution:", solution)
print("Maximum fitness:", fitness(solution))